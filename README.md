#  Django CMS API
 - This is a simple CMS web application built using Django and Django Rest Framework.
 - The application allows users to save blogs,like blogs,login and register user.
 - Provides a set of API endpoints for authentication and CRUD operations on Blog,User and Like.

## Features
The Django CMS API App provides the following features:

## Authentication API
- **Login API**: Allows users to authenticate user name and password.
## CRUD APIs
- **Get all blogs**: Provides the total count of likes for each blog.
- **Create API**: Allows users to create a new user,blog,like by providing the necessary information. The  data is then saved to the database.
- **Detail API**: Displays the details of a specific user,blog,like .
- **Update API**: Allows users to update the information of an existing user,blog,like . The API returns the updated user,blog,like  details as a response.
- **Delete API**: Enables users to delete selected user,blog,like.
  
# Installation and Setup
   To run the Django CMS Web App locally, follow these steps:

### Clone the GitHub repository:
     https://github.com/sanjayjc97/cms-api-django.git
    
    
### Navigate to the project directory
     cd cms-api-django
    
### Create a virtual environment:
     virtualenv venv
    
### Activate the virtual environment:
     source venv/bin/activate
    
### Install the required dependencies:
     pip install -r requirements.txt
### Apply the database migrations:
     python manage.py makemigrations   
### Apply the database migrations:
     python manage.py migrate
### Start the development server:
     python manage.py runserver
### Access the web application in your browser
     http://localhost:8000.


#### postman collection >  CMS-API-ENDPOINTS.postman_collection.json




