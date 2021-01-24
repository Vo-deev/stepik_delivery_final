from src.config import app, db
from src import models
import src.routes
import admin


@app.before_first_request
def create_table():
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': models.User,
        'Order': models.Order, 'Category': models.Category,
        'Meal': models.Meal
    }


if __name__ == "__main__":
    app.run(debug=True)
