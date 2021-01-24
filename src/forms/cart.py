from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CartForm(FlaskForm):
    name = StringField("Ваше имя", validators=[DataRequired()])
    address = StringField("Адрес", validators=[DataRequired()])
    email = StringField("Электронная почта", validators=[DataRequired()])
    phone = StringField("Телефон", validators=[DataRequired()])
    submit = SubmitField("Оформить заказ")
