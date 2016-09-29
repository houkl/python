# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
__author__ = 'houkl'

from flask.ext.sqlalchemy import SQLAlchemy
from qb_cmdb import app
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)


db = SQLAlchemy(app)

class Idc(db.Model):
    __tablename__ = 'idc'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    contact = db.Column(db.String(64))
    address = db.Column(db.String(512))
    tel_phone = db.Column(db.String(32),nullable=True)

    def __init__(self,name,contact,address,tel_phone):
        self.name = name
        self.contact = contact
        self.address = address
        self.tel_phone = tel_phone

    def __repr__(self):
        return "<Idc %r>" % self.name

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

# admin = Idc(name="shahe",contact="111111",address="address")
# db.session.add(admin)
# from flask import Flask
# import setting
# from flask.ext.sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = setting.SQLALCHEMY_DATABASE_URI
# # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# db.create_all()
