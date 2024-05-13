Blog API with Django REST Framework

Overview
This project is a RESTful API for managing and serving blog content, implemented using Django REST Framework. It provides endpoints for creating, reading, updating, and deleting blog posts, categories, tags, and comments.

Features
User Authentication: Register, log in, and manage user profiles. Token-based authentication secures API endpoints.
Post Management: CRUD operations for blog posts, including fields such as title, content, author, categories, tags, and comments.
Category : Manage categories for organizing blog posts.
Comments: Allow users to leave comments on blog posts, with features such as content, author, and approval status.
Likes: Allow users to like and dislike the post


Installation
To use the blog API locally, follow these steps:

Clone the repository:
Copy code
git clone https://github.com/Alen-Sabu/Blog_API.git


Install dependencies:
bash
Copy code
pip install -r requirements.txt

Configure database settings in settings.py.

Apply migrations:
python manage.py makemigrations


Copy code
python manage.py migrate



Run the development server:
bash
Copy code
python manage.py runserver
Access the API at http://localhost:8000
