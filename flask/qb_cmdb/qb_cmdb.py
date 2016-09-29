from flask import Flask
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = setting.SQLALCHEMY_DATABASE_URI
app.config.from_object("setting")
from views.login import *

if __name__ == '__main__':
    app.run(debug=True,port=8000)
