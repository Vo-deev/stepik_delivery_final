from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
    email = StringField("Электронная почта", validators=[
        DataRequired(), Email()
    ])
    password = PasswordField("Пароль", validators=[
        DataRequired(),
        Length(min=5, message="Пароль должен быть не менее 5 символов")
    ])
    submit = SubmitField("Зарегистрироваться")
