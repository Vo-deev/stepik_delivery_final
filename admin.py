from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.config import db, app
from src.models import User, Order, Category, Meal

admin = Admin(app, name="Stepik Delivery", template_mode="bootstrap3")


# Добавить представление к каждой модели
admin.add_view(ModelView(User, db.session, category="User Settings"))
admin.add_sub_category(name="Order", parent_name="User Settings")
admin.add_view(ModelView(Order, db.session, category="Order"))
admin.add_view(ModelView(Category, db.session, category="Order"))
admin.add_view(ModelView(Meal, db.session, category="Order"))
