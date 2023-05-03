# Capstone1-L3
This repo serves to hold my Capstone project 1 of Level 3 tasks

Description
This django project is meant to be a e-commerce site that uses django. It has a functional Login and Registration section, with a responsive static webpage.

Prerequisites
Docker installed on the machine where you want to run the project.

Installation
Clone the repository to your local machine.
git clone https://github.com/your-username/Capstone1-L3.git
Install Python 3.x if you haven't already.
Install virtualenv if you haven't already: pip install virtualenv.
Navigate to the project root directory in the command line.
Create a virtual environment: python -m venv env.
Activate the virtual environment: source env/bin/activate (Linux/macOS) or env\Scripts\activate (Windows).
Install the required packages: pip install -r requirements.txt.
Run the application: python manage.py runserver.

Using Docker:
Install Docker if you haven't already.
Navigate to the project root directory in the command line.
Build the Docker image: docker build -t GetIt:v1.0 ..
Run the Docker container: docker run -p 8000:8000 GetIt:v1.0
Navigate to http://localhost:8000 in your web browser to view the Django app.

Dependancies
The dependancies can be viewed in the requirements.txt file.

Configuration
Environment Variables
The following environment variables are used in the application:

DATABASE_URL: The URL of the database to use. Defaults to a local SQLite database.
SECRET_KEY: 'django-insecure-3j#qp%6cpzo7)eho(chny55m459!%5cz54w=45nh#d*)z^*ts$'
