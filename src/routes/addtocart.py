from flask import session, redirect, url_for
from src.config import app


@app.route("/addtocart/<product_id>")
def add_to_cart(product_id):
    if session.get("cart") is not None:
        current_cart = session["cart"].split(",")
        current_cart.append(product_id)
        session["cart"] = ",".join(current_cart)
    else:
        session["cart"] = product_id

    return redirect(url_for("cart"))
