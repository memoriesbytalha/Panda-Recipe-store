# Panda Recipe Store

A Django-based recipe management application where users can view, add, update, and delete recipes. The app includes user authentication (login and registration) and features a user-friendly interface for managing recipe information.

## Screenshots

![Login Page](UI/login.png)
*Login Page - User authentication interface*

![Add Recipe](UI/add_recipe.png)
*Add Recipe - Form to create new recipes*

![Recipe Detail](UI/recipe_detail.png)
*Recipe Detail - View complete recipe information*

## Features

- **User Authentication**: Login, register, and logout functionality using Django's built-in user model.
- **Recipe Management**: Users can add, view, update, and delete recipes with attributes like name, description, and image.
- **Responsive UI**: The app has a simple, intuitive design to easily navigate through recipes and manage your profile.
  
## Technologies Used

- **Django**: The web framework used to develop this application.
- **Python**: The programming language used for backend development.
- **HTML/CSS**: For creating and styling the front-end templates.
- **SQLite**: The default database used by Django for development.
- **Git & GitHub**: For version control and project collaboration.

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/memoriesbytalha/Panda-Recipe-store.git
   cd Panda-Recipe-store
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. Open a browser and go to `http://127.0.0.1:8000` to access the app.


## Future Improvements

- **Authentication**: Implement password reset functionality and email verification for added security.
- **Recipe Search**: Add a search bar to allow users to easily find recipes by name or description.
- **Recipe Categories**: Introduce categories (e.g., vegetarian, non-vegetarian) to organize recipes.
- **User Profiles**: Allow users to manage their profiles and store their favorite recipes.

