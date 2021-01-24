from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from src.config import db


orders_meals_association = db.Table(
    "orders_meals",
    Column("order_id", Integer, ForeignKey("order.id")),
    Column("meal_id", Integer, ForeignKey("meal.id"))
)


class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(64))
    password_hash = Column(String(128), nullable=False)
    orders = relationship("Order", back_populates="user")

    @property
    def password(self):
        raise AttributeError("Model User has no attribute <password>")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_valid(self, password):
        return check_password_hash(self.password_hash, password)


class Order(db.Model):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    total = Column(Integer)
    status = Column(Boolean, default=False)
    mail = Column(String(64))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="orders")
    phone = Column(String(32))
    address = Column(String(128))
    meals = relationship(
        "Meal", secondary=orders_meals_association, back_populates="orders"
    )


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    meals = relationship("Meal", back_populates="category")


class Meal(db.Model):
    __tablename__ = "meal"
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    price = Column(Integer)
    description = Column(Text)
    picture = Column(String, unique=True)
    orders = relationship(
        "Order", secondary=orders_meals_association, back_populates="meals"
    )
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="meals")
