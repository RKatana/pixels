# Pixels

###  Author
Marvin Chomba Kangangi

### Description
A personal gallery application that I display photos for others to see.

### User Stories :family:
1. View different photos that interest me.
1. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
1. Search for different categories of photos. (ie. Travel, Food)
1. Copy a link to the photo to share with my friends.
1. View photos based on the location they were taken.

### How to use :rocket:
When the user opens the website, he/she will see the recent photos.
The user can enlarge the photos and copy the url link for the photo.
The user can also search for photos in a certian category e.g food.
The user can also view photos based on the photos' locations e.g Africa


### Tech used :computer: 
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```
### Requirements
1. config==0.4.0
1. dj-database-url==0.5.0
1. Django==1.11
1. django-bootstrap3==11.0.0
1. django-bootstrap4==0.0.7
1. django-heroku==0.3.1
1. gunicorn==19.9.0
1. Jinja2==2.10
1. MarkupSafe==1.1.0
1. Pillow==5.3.0
1. psycopg2==2.7.6.1
1. python-decouple==3.1
1. pytz==2018.7
### .ENV file
1. SECRET_KEY='<SECRET_KEY>'
1. DEBUG=True #set to false in production
1. DB_NAME='tribune'
1. DB_USER='user'
1. DB_PASSWORD='password'
1. DB_HOST='127.0.0.1'
1. MODE='dev' #set to 'prod' in production
1. ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
1. DISABLE_COLLECTSTATIC=1

### Installation
1. To access this application on your command line, you need to clone it 
`git clone https://github.com/marvinChomba/pixels.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations photos`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test photos`

### Known Bugs :x:
Currently, there are no known bugs

### Live link
You can view the live site [here]()
### Licence
This project is under the [MIT](https://github.com/marvinChomba/pixels/blob/master/LICENSE) licence

Copyright (c) 2018 marvinchomba
