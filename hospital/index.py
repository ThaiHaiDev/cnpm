from flask import render_template, request, session, jsonify, redirect
from hospital import app, admin_Login
from hospital.models import Account
from flask_login import login_user
import hashlib
from admin import *


@app.route("/")
def home():
    return render_template("home.html")


@admin_Login.user_loader
def user_load(user_id):
    return Account.query.get(user_id)


@app.route("/login", methods=['post'])
def login_exe():
    username = request.form.get("username")
    password = request.form.get("password")

    password = str(hashlib.md5(password.encode("utf-8")).digest())

    user = Account.query.filter(Account.username == username,
                                Account.password == password).first()
    if user:
        login_user(user)

    return redirect("/admin")


if __name__ == '__main__':
    app.run(debug=True)