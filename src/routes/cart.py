from flask import render_template, request, redirect, url_for, session
from datetime import datetime
from src.models import Meal, Order, User
from src.forms import CartForm
from src.config import app, db


@app.route('/cart/', methods=["GET", "POST"])
def cart():
    form = CartForm()

    current_cart = session.get("cart")
    cart_status = bool(current_cart)

    if form.validate_on_submit():
        if session.get("id") is None:
            return redirect(url_for("login"))

        user = User.query.filter(User.id == session["id"]).first()
        name, address, email, phone = [value for key, value in form.data.items()][:4]
        order = Order(
            date=datetime.now(),
            total=request.form.get("order_sum"),
            mail=email,
            phone=phone,
            address=address,
            user_id=user.id,
        )

        for meal in session["cart"].split(","):
            order.meals.append(Meal.query.filter(Meal.id == meal).first())

        db.session.add(order)
        db.session.commit()
        session.pop("cart")
        return render_template("ordered.html")

    if cart_status:
        all_meals = [Meal.query.filter(Meal.id == meal).first() for meal in current_cart.split(",")]
        meals_sum = sum([meal.price for meal in all_meals])

        counted_meals = {}
        for meal in all_meals:
            current_meal_amount = all_meals.count(meal)
            counted_meals.update({meal: current_meal_amount})

        return render_template(
            "cart.html",
            meals_amount=len(current_cart.split(",")),
            meals_sum=meals_sum,
            all_meals=counted_meals,
            cart_status=cart_status,
            form=form
        )

    return render_template(
        'cart.html',
        cart_status=cart_status,
    )
