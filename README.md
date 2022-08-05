#QuestionBox

This is a api for a question and answer type project focused on video games.

It has User creation and login/logout functions.

Categorys can be made then can have games tagged to them.

You can create questions with a game tagged with it. Answer questions. Users can also favorite questions/answers.

You can view all questions through the games and all answers through the questions.

## Installation

This project uses Python 3.10.

To run this app locally, you can clone this repository and do the following.

1. start your virtual enviroment:

```console
pipenv shell
```

2. Run the following to install all packeges that were used in this project:

```console
$ pipenv install
```

3. Create a local PostgreSQL database:

#### Install PostgreSQL
```console
brew install postgresql
```

#### Start PostgreSQL
```console
brew services start postgresql
```

#### Create a user
```console
createuser -d <username>
```

#### create a database
```console
createdb -U <username> <dbname>
```

4. Install a Python PostgreSQL adapter:

```console
pipenv intall psycopq2-binary
```

3. Create a .env file with a postgres database URL, secret key, and a Debug=True

```ini
DATABASE_URL=<local Postgresql database URL here>
SECRET_KEY=<A personally secret key here>
DEBUG=<This should be set to True>
```

3. Next run the server:

```console
$ python manage.py runserver
```

4. These are all the endpoints, methods they use, and small description of what they can do.

URL          | Method | Function
:-------------|:--------:|--------------------:
/api/auth/users/ |  POST  | Create User 
/api/auth/token/login/ | POST | Login
/api/auth/token/logout/ | POST | Logout
/api/game/<int:pk>/question/ | GET | All questions
/api/questions/ | POST | Create Question
/api/question/<int:pk>/delete/ | DELETE | Delete Question
/api/questions/<int:pk>/ | GET | Question Details
/api/questions/<int:question_pk>/favorites/ | POST, DELETE | Favorite Question, Unfavorite Question
/api/question/<int:pk>/answer/ | GET, POST | List Answers, Create Answer
/api/answer/<int:pk>/delete/ | DELETE | Delete Answer
/api/answers/<int:answer_pk>/favorites/ | POST, DELETE | Favorite Answer, Unfavorite Answer
/api/user/<int:pk>/question/ | GET | All Questions Submitted By User
/api/user/<int:pk>/answer/ | GET | All Answers Submitted By User
/api/categories/ | GET | View Categories
/api/category/<int:pk>/delete/ | DELETE | Deleting Categories
/api/add/game/ | POST | Create Game
/api/games/ | GET | List All Games
/api/category/<int:pk>/game/ | GET | List Games in Specific Category