## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)

## Description

The Expense Tracker App is a Django-based web application designed to help users track their expenses efficiently. Users can log / edit / delete their expenses in addition to collecting data on expenses by date / category / timeline.

**Tech Stack: Python / ORM with Django, JS / chartJS / tailwindcss**

## Installation

1. Clone the repository:

   ```bash
   gh repo clone wells1989/expense_tracker 

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Apply database migrations:

   ```bash
   python manage.py migrate 

4. Run the development Server:

   ```bash
   python manage.py runserver 

Access the app at http://localhost:8000 in your web browser.

## Usage
- Log expenses into the Django Form on the homepage:
![Screenshot (518)](https://github.com/wells1989/Full-stack-blog/assets/122035759/a94f751f-2f73-4888-865f-533f8cf2270e)

- Edit or delete Expenses in the table in addition to seeing total statistics:
![Screenshot (519)](https://github.com/wells1989/Full-stack-blog/assets/122035759/e6006521-a95a-4191-99a9-afa5185d65bd)

- Also can see statistics in ChartJS format:

![Screenshot (520)](https://github.com/wells1989/Full-stack-blog/assets/122035759/3e2f51d5-1a8c-4f0d-8e8e-6307569f2086)

### Notes
- The aim of the project was to utilise more complex Django views, using ORM in the backend to provide more specific data, whilst using tailwindCSS to create a more streamlined UI in the Frontend. 

#### Future development:
- The next step of the project if going into deployment would be to add user registration / login functionality via django's built-in user authentication system. Then the User model could be used in conjunction with the views.py to filter expenses by user. As this was a development project focusing on complex Django data fetching and UI display these functionalities were not included in this version.
