from flask import render_template, session
from src.models import User
from src.config import app


@app.route('/account/', methods=["GET", "POST"])
def account():
    if session.get("id") is not None:
        user = User.query.filter(User.id == session.get("id")).first()
        return render_template('account.html', user=user)
    else:
        return redirect(url_for("login"))
