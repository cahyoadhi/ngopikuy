# Coffee Shop Website (Django)
![homepage](https://user-images.githubusercontent.com/90748704/191624416-249da180-5a9f-47d6-8d30-a6e0fa1028a9.png)


## Demo
### Realtime dashboard
![demo-ngopikuy](https://user-images.githubusercontent.com/90748704/191624120-c3ff7955-7f39-4844-a347-5ddfabe39b63.gif)

every time there is a new order that comes in, the staff and admin will immediately find out through the realtime dashboard

### Difference between Admin, Staff, and Customer
![demo-ngopikuy2](https://github.com/cahyoadhi/ngopikuy/blob/main/readme-asset.gif)
- admin has access to read, edit and delete.
- staff have access to read and edit data.
- customer can't enter dashboard page. will be redirect to the homepage.

## Installation

It's recommended that you setup a virtualenv before development.
```sh
\venv\Scripts\activate.bat 
```

Then just install requirements, migrate, and runserver to get started:
```sh
git clone https://github.com/cahyoadhi/ngopikuy.git
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

*This project is developed for demo purpose and it's not supposed to be used in real application.*
