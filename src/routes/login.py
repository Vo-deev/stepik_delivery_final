from flask import render_template, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash
from src.forms import AuthForm
from src.models import User
from src.config import app


@app.route('/login/', methods=["GET", "POST"])
def login():
    form = AuthForm()
    if form.validate_on_submit():
        email, password = form.email.data, form.password.data
        user = User.query.filter(User.email == email).first()
        if user is not None:
            if user.password_valid(password):
                session.clear()
                session["id"] = user.id
                session["email"] = user.email
                return redirect(url_for("account"))
            else:
                flash("Неправильный пароль")
        else:
            flash("Почта отсутствует, сперва зарегистрируйтесь")
    return render_template('auth.html', form=form)
