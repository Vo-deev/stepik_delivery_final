from flask import render_template, request, session
import os
from src.models import Category, Meal
from src.config import app


@app.route('/', methods=["GET", "POST"])
def main():
    data = {
        category.name: category.meals for category in Category.query.all()
    }
    current_cart = session.get("cart")
    cart_status = bool(current_cart)
    if cart_status:
        all_meals = current_cart.split(",")
        meals_amount = len(all_meals)
        meals_sum = sum([Meal.query.filter(Meal.id == meal).first().price for meal in all_meals])
        return render_template(
            "main.html", data=data, cart_status=cart_status,
            meals_amount=meals_amount, meals_sum=meals_sum
        )
    return render_template('main.html', data=data, cart_status=cart_status)


@app.route("/clear")
def clear():
    session.clear()
    return render_template('main.html')

