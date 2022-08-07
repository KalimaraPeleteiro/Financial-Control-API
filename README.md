<h1 align="center"> FinancialControlAPI </h1>

An API created for familiar financial control, allowing the user to register incomes and expenses, for a better tracking and understanding
of their finances. After the registers are made, it's possible to order a monthly summary, discribing all financial changes in the month.
<br></br>

## 👨‍💻 Technologies
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" width=50 height=50/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width=50 height=50/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain-wordmark.svg" width=50 height=50/>
<br></br>

## 🚀 Project
The API is available in https://drf-financial-api.herokuapp.com/. To acess it, however, it'll be needed an authentication.
I've created a "default" user, for open acess.
- Username = *default*
- Password = *defaultpassword123*

If you wish to learn more about how the API works, and what are the specific commands, you can acess the documentation in 
https://drf-financial-api.herokuapp.com/doc/.
<br></br>

## 💻 Downloading the Project
If you wish to download the files and work on the project, a few steps are going to be needed.
You need to make sure that you have Python installed, such as some few libraries, that will be listed in *requirements.txt*. To download all libraries,
use the following command.
```
pip install -r requirements.txt
```
> It's of major importance that you only download such libraries _after_ inside the virtual environment. To enter the venv, use the code 
> `source "path-to-venv/venv/bin/activate"`. It's also of major importance that you have the Python Package Installer (pip) to run the command.

With the libraries installed you will also need two other things. The first one is PostgreSQL, and the second one is to modify, in _FinancialControlAPI/settings.py_
the database configurations to fit your created database. The final setting should be something close to this.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DatabaseName',
        'USER': 'UserName',
        'PASSWORD': 'UserPassword',
        'HOST': 'localhost'
    }
}
```
After the database is configured, use the commands `python manage.py makemigrations` and `python manage.py migrate` to create the needed tables
in your database.
With this out of the way, you can build the server with `python manage.py runserver`. The app will be available in http://127.0.0.1:8000.

## 🙇‍♂️ Any Suggestions?
In case of any suggestions, opinions or criticism, please, contact me. I'm looking forward to keeping improving always, and feedback
is always precious.
