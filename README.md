#![logo](https://github.com/user-attachments/assets/fad177d7-080b-423f-859b-d59c12020f18)
 Django-application

 # MealMate

MealMate is a simple Django-powered web application for managing and sharing recipes. Users can sign up, create and manage their recipes, comment on others’ recipes, and link to original sources.

## Features

- **User Authentication**  
  Sign up, log in, and log out using Django’s built-in auth system.

- **Recipe CRUD**  
  - Create new recipes with fields: **Title**, **Cuisine**, **Cooking Time**, **Skill Level**, **External Link**.  
  - View a list of all recipes.  
  - View detailed recipe pages with comments.  
  - Edit or delete your own recipes.

- **Comments**  
  - Post comments on recipe detail pages.  
  - Edit or delete your own comments.

- **External Links**  
  Optionally link each recipe to an original source URL.

- **Bootstrap 5**  
  Responsive front-end styling.

## Tech Stack

- Python 3.x  
- Django 4.2.x  
- SQLite (default) or PostgreSQL  
- Bootstrap 5

## Getting Started

### Prerequisites

- Python 3.x  
- pip  
- virtualenv (optional but recommended)

###Installation

1. Clone the repository

```
git clone <your-repo-url>
cd mealmate
```

2. Create and activate a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate     # macOS/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Configure the database

By default, MealMate uses SQLite. If you prefer PostgreSQL, update settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': '<db_user>',
        'PASSWORD': '<db_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Run migrations
   
```
python manage.py migrate
```

6. Create a superuser (for admin access)

```
python manage.py createsuperuser
```

7. Start the development server

```
python manage.py runserver
```

8. Access the app
   
```
Open your browser and go to http://127.0.0.1:8000/
```

### Usage

Sign Up: Click 'Sign Up' in the navbar to register a new account.

Log In: Use 'Login' to access your account.

Create Recipe: Click '+ New Recipe' on the home page, fill out the form, and save.

Edit/Delete Recipe: On your recipe's detail page, use 'Edit' or 'Delete'.

Comment: On any recipe, add comments or manage your own comments.
