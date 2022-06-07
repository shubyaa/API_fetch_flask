from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask import Flask
import socket, os
from dotenv import load_dotenv

load_dotenv()

passwd = os.getenv("passwd")                # Your db password
database_name = os.getenv("database_name")  # Your db name

socket.getaddrinfo('localhost', 25)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/' % quote(passwd) + database_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PASSWORD'] = '8451841454aA@'
# app.config['MYSQL_DB'] = 'database_interactions'

db = SQLAlchemy(app)    # initialize db



# create db models with their default constructors to make their objects
# and add them in database using sqlalchemy.
class Users(db.Model):
    id_users = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    address = db.relationship('Address', backref='users', lazy=True)
    phone = db.Column(db.String(25), nullable=False)
    website = db.Column(db.String(25), nullable=True)
    company = db.relationship('Company', backref='users', lazy=True)
    

    def __init__(self, id_users, name, username, email_address, phone, website, address, company):
        self.id_users = id_users
        self.name = name
        self.username = username
        self.email_address = email_address
        self.phone = phone
        self.website = website
        self.address = address
        self.company = company


class Comments(db.Model):
    id_comments = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id_posts'))
    name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False, unique=True)
    body = db.Column(db.String(300), nullable=False, unique=True)

    def __init__(self, id_comments, post_id, name, email_address, body):
        self.id_comments = id_comments
        self.post_id = post_id
        self.name = name
        self.email_address = email_address
        self.body = body




class posts(db.Model):
    id_posts = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    title = db.Column(db.String(100), nullable=False, unique=True)
    body = db.Column(db.String(300), nullable=False, unique=True)

    def __init__(self, id_posts, users_id, title, body):
        self.id_posts = id_posts
        self.users_id = users_id
        self.title = title
        self.body = body




class Address(db.Model):
    id_address = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(50), nullable=False)
    lat = db.Column(db.String(50), nullable=False)
    long = db.Column(db.String(50), nullable=False)

    def __init__(self, id_address, users_id, street, city, zipcode, lat, long):
        self.id_address = id_address
        self.users_id = users_id
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.lat = lat
        self.long = long





class Company(db.Model):
    id_company = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    name = db.Column(db.String(100), nullable=False)
    catch_phrase = db.Column(db.String(200), nullable=False)
    bs = db.Column(db.String(200), nullable=False)

    def __init__(self, id_company, users_id, name, catch_phrase, bs):
        self.id_company = id_company
        self.users_id = users_id
        self.name = name
        self.catch_phrase = catch_phrase
        self.bs = bs
