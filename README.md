# Project usage guide
## How to run the project locally?

### 💾 Downloading the project to the computer
#### Git clone
```bash
git clone https://github.com/dev-KPI/iatp-dev-website-backend-python.git
```


### 🔨 Dependency installation
To use this project without installation of everything by yourself just use
#### Libs installation
```bash
pip3 install -r requirements.txt
```

### ⚡️ Connect your database
Create your database. And make changes to the settings
##### Connect to DB 
```bash
sudo -u postgres psql 
```
##### Create DB
```bash
CREATE DATABASE my_database; 
```
##### Changes settings
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "my_database",
        "USER": "<your user>",
        "PASSWORD": "<password 'your user'>",
        "HOST": "<localhost>",
        "PORT": "<port>",
    }
}
```


### 🔐 Get your secret key
Get your secret key. And make changes to the settings
##### Get your secret key
```
https://djecrety.ir/
```
##### Changes settings
###### Before
```
SECRET_KEY = os.getenv("SECRET_KEY")
```
###### After
```
SECRET_KEY = "<generated secret key>"
```


### 🗃️ Makemigrations
Run the command in the directory with file manage.py
##### Makemigrations writes model changes to separate migration files, similar to commits. Create makemigrations
```bash
python manage.py makemigrations
```

### 🗄️ Migrate
Run the command in the directory with file manage.py
##### Migrate applies these changes to the database. Create migrate
```bash
python manage.py migrate
```


### 👑 Superuser
Run the command in the directory with file manage.py. Follow the instructions
##### Create superuser
```bash
python manage.py createsuperuser
```

### 🚀 Start
Run the command in the directory with file manage.py
##### Run project
```bash
python manage.py runserver
```

## How to deploy a project remotely?

### 💽 Install flyctl
Flyctl is a command-line utility that lets you work with the Fly.io platform, from creating your account to deploying your applications
##### Install flyctl
```bash
curl -L https://fly.io/install.sh | sh
```


### 📖 Sign up
If it’s your first time using Fly.io, you’ll need to sign up for an account.
##### Sign up
```bash
flyctl auth signup
```

### 📮 Preparing Django application
To prepare for the fly.io you don’t normally need anything.
The fly.io cli will take care of everything.
From creating the docker file to fly configuration file.
##### Preparing Django application
```bash
flyctl launch
```

### 🚀 Deploy
So for the deployment steps all we need to do is
put our .env files into fly instance and 
then issue a deploy command.
##### Deploy
```
flyctl secrets import < .env
```
```bash
flyctl deploy
```