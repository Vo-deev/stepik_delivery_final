from flask import render_template, redirect, url_for, session
from src.forms import RegisterForm
from src.config import app, db
from src.models import User


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        email, password = form.email.data, form.password.data
        db.session.add(User(email=email, password=password))
        db.session.commit()
        return redirect(url_for("main"))

    return render_template("register.html", form=form)
