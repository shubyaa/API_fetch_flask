
# CRUD Api using FLask

Getting data via APIs into MySQL database and then creating new APIs using python Flask to perform CRUD operations
<p float="center">
<img src="https://github.com/jalbertsr/logo-badge-images/blob/master/img/rsz_flask.png?raw=true" width="100" />
</p>

## Badges

![Flask](https://img.shields.io/badge/Flask-2.0-green.svg) 
![Python](https://img.shields.io/badge/Python-3.9.5-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)

## API Reference

#### Get users data

```http
  GET https://jsonplaceholder.typicode.com/users
```

#### Get posts data

```http
  GET https://jsonplaceholder.typicode.com/posts
```

#### Get comments data

```http
  GET https://jsonplaceholder.typicode.com/comments
```

## Features

- Multi Api functionalities
- Fetch user details by giving input queries
- Structured SQL database



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`passwd`

`database_name`


## Run Locally

Clone the project

```bash
  git clone https://github.com/shubyaa/API_fetch_flask
```

Go to the project directory

```bash
  cd API_fetch_flask
```

Install dependencies

```bash
  pip install flask
  pip install sql-alchemy
  pip install dotenv
  pip install pymysql
```

Start the server

```python
    from crud_api import app
    app.run()

```


## Tech Stack

**Test:** Postman

**Server:** Flask, Python


## Screenshots

![Screenshot 1](https://github.com/shubyaa/API_fetch_flask/blob/main/screenshots/1.png)
![Screenshot 2](https://github.com/shubyaa/API_fetch_flask/blob/main/screenshots/2.png)
![Screenshot 3](https://github.com/shubyaa/API_fetch_flask/blob/main/screenshots/3.png)


## Lessons Learned

- Building REST APIs using Flask
- Fetch Data froam APIs and store it in SQL Database
- Parsing JSON files
- Database Connectivity using URI
- Basic funcionalities of Flask

## 🛠 Skills
Python, Java, Kotlin, Javascript, HTML, Bootstrap, Firebase, SQL, SQLite


## 👍🏻 Support

For support, email shubya8451@gmail.com .
