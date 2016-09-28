# Django Login Tutorial with Register

Prerequisite
===
```
Python 3.5+
MySQL
virtualenv
```
## Don't forget to create database first

Prepare for Battle
===
1. Start with create the virtual environment, install django and mysqlclient
```
$ virtualenv [project_name]
$ cd [project_name]
$ source ./bin/activate
$ pip install Django
$ pip install mysqlclient
```

2. After that create your own project
```
$ django-admin startproject [project_name]
$ cd [project_name]
```

 Test that Django was installed successfully
```
$ python manage.py runserver
```

3. Create app
```
$ python manage.py startapp [app_name]
```

4. Change your DBMS in `[project_name]/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': './my.cnf'
        },
    }
}
```
You can separate your database information to `cnf` file and tell the path here **The path is start from folder that contains `manage.py`**

    **my.cnf**
```
[client]
database = [database_name]
user = [username]
password = [password]
default-character-set = utf8
```
Then Migrate database
```
$ python manage.py migrate
```

5. Connect your **app** to **project** in `[project_name]/settings.py`
```
INSTALLED_APPS = [
    '[app_name].apps.[Appname(start with capitalize)]Config',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
