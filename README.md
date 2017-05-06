# TubelistApi
Rest Api for webapp [Tubelist](https://tubelists.herokuapp.com) which enables users to create and share custom playlists using youtube videos.

## Techonolgies
* Python 3
* Django 1.10
* Django Rest Framework
* Json Web Token Authentication

### Instructions

Make Migrations

`python manage.py makemigrations`

`python manage.py migrate`

Create Admin Account

`python manage.py createsuperuser`

Starting The Server

`python manage.py runserver`

#### Note

Make sure to replace `YOUR_YOUTUBE_API_KEY` with your `youtube api key` in `api/util.py`
