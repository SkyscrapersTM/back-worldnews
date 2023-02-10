# World News API
World News is an api made in Django. Allows you to manage news.
## Requirements
You need to have Git and Python installed.
***

## Using
    # Clone this project ✅
    git clone https://github.com/SkyscrapersTM/back-worldnews.git

    # Create a virtual environment✅
    py -m venv venv

    # Activate virtual environment ✅
    source venv/Scripts/Activate (Terminal linux)

    # Install dependencies ✅
    pip install -r requirements.txt

    # Create database ✅
    create database worldnews;

    # Set your mysql in settings.py ✅
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'worldnews',
            'USER': '...',
            'PASSWORD': '...',
            'HOST': '...',
            'PORT': 3306,
        }
    }

    # Set your CORS ✅
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://192.168.1.4:3000",
    ]

    # Create migrations files ✅
    py manage.py makemigration

    # Execute the changes detected in the models ✅
    py manage.py migrate

    # Create user admin ✅
    $ py manage.py createsuperuser
    
    # Run the server ✅
    py manage.py runserver

Go  to _locahost:port/admin_ and import _data-category.json_, _data-article.json_

[![admin.jpg](https://i.postimg.cc/zXyTWdLy/admin.jpg)](https://postimg.cc/GH1BnxxR)

ENDPOINTS:

[![endpoints.png](https://i.postimg.cc/mkD5f0bY/endpoints.png)](https://postimg.cc/ZBGc6svn)

## License 

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

