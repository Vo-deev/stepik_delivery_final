from src.models import Meal, Category
from src.config import db
import csv


def add_meals(f_obj):
    reader = csv.reader(f_obj)
    for row in reader:
        if row[0] == "id":
            continue
        meal = Meal(
            title=row[1],
            price=int(row[2]),
            description=row[3],
            picture=row[4],
            category_id=row[5]
        )
        db.session.add(meal)
    db.session.commit()


def add_categories():
    for c in ["Суши", "Стритфуд", "Пицца", "Паста", "Новинки"]:
        category = Category(name=c)
        db.session.add(category)
    db.session.commit()


if __name__ == "__main__":
    csv_path = "delivery_items.csv"
    with open(csv_path, "r") as f_obj:
        add_meals(f_obj)
    add_categories()
