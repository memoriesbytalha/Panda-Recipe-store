from django.shortcuts import render,redirect,get_object_or_404
from recipe.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout


def recipe(request):
    data =request.POST
    if request.method == 'POST':
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
       
        Recipe.objects.create(name=name, description=description, image=image)

        return redirect('/recipe')
        
   
    queryset = Recipe.objects.all()

    context = {
    'page': 'Recipe',
    'recipes': queryset
    }
    return render(request, 'recipe.html',context=context)

def delete_recipe(request, id):
    Recipe.objects.filter(id=id).delete()
    return redirect('/recipe')


def update_recipe(request, id):
   
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name', recipe.name)
        description = data.get('description', recipe.description)
        image = request.FILES.get('image') 

        
        recipe.name = name if name else recipe.name
        recipe.description = description if description else recipe.description

        if image:
            recipe.image = image
    
        recipe.save()
        return redirect('/recipe')


    context = {'recipe': recipe,
               'page': 'Recipe',}
    
    return render(request, 'update_recipe.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"Username: {username}")
        print(f"Password: {password}")


        # Check if username is empty
        if not username:
            messages.error(request, "Username is required.")
            return redirect("register")  # Redirect to clear the form

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        # User.set_password(password)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")  

    context = {
        "page": "Register"
    }
    return render(request, "register.html",context=context)


def logout(request):
    logout(request)
    return redirect('/index')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"Attempting login with Username: {username} and Password: {password}")

        
        # Check if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username does not exist")
            return redirect('/login')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        print(f"Attempting login with Username: {username} and Password: {password}")

        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/recipe')
        else:
            messages.error(request, "Incorrect password")
            return redirect('/login')
        
    context = {
        "page": "Login"
    }

    return render(request, 'login.html', context=context)



