# Quizz App - Backend
### App developed for iClinic's technical challenge

## Installation
For the installation of the backend server of our QuizzApp, it is necessary to have the packages: Git, Python3, VirtualEnv and Pip installed on your machine. If you are using Linux/Ubuntu, do:

```
#apt-get install git
#apt-get install python3
#apt-get install python3-pip
#apt-get install libpq-dev
#pip3 install virtualenv
```

Now, download our repository, create and active the virtualenv and install the dependences:
```
git clone https://github.com/vinicius-issa/quizz_backend.git
cd quizz_backend
virtualenv -p . venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Now, create a `.env` file in root with postgress db configurations:
```
DB_NAME = <your_db_name>
DB_USER = <your_db_user>
DB_PSWD = <your_db_password>
DB_HOST = <your_db_host>
DB_PORT = <your_db_port>
```
Nice, lets go to migrate the database:

```
python3 manage.py migrate
```

Fine! Now, run the app using manage.py and enjoy:
```
python3 manage.py runserver
```

