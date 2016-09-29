#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'houkl'
from flask import render_template,url_for,make_response,request,session,redirect,escape
from sqlalchemy import or_,and_
from qb_cmdb import app
from models import db,Idc,User

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/',methods=['POST','GET'])
def login():
    if request.method == "POST":
        # if User.query.filter(User.username==request.form["username"],User.password==request.form["password"]).all():
        if User.query.filter(and_(User.username==request.form["username"],User.password==request.form["password"])).all():
            session["username"] = request.form['username']
            return redirect(url_for("index"))
        else:
            return redirect(url_for("login"))
    else:
        return render_template('login.html')

@app.route("/index/")
def index():
    idc_result = Idc.query.all()
    if "username" in session:
        # return 'Logged in as %s' % escape(session['username'])
        return render_template("index.html",username=session['username'],idc_result=idc_result)
    else:
        return redirect(url_for("login"))

@app.route("/add_idc/",methods=["POST","GET"])
def add_idc():
    if request.method == "POST":
        if not Idc.query.filter(Idc.name==request.form["name"]).first():
            sql = Idc(request.form["name"],request.form["contact"],request.form["address"],request.form["tel_phone"])
            db.session.add(sql)
            db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("assets/add_idc.html")

@app.route("/logout/",methods=["POST","GET"])
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404


