from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from hospital import db
from datetime import datetime


class Account(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    masterShip = Column(Integer, nullable=False)


class Medicine(db.Model):
    STT = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10))
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    unit = Column(String(10), nullable=False)
    image = Column(String(100), nullable=True)

    # def __str__(self):
    #     return self.name


class Patient(db.Model):
    idPatient = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    idCard = Column(Integer, nullable=False)

    # def __str__(self):
    #     return self.name


class Policy(db.Model):
    idPolicy = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)

    # def __str__(self):
    #     return self.name


class Questions(db.Model):
    idQuestion = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)

    # def __str__(self):
    #     return self.name

if __name__ == '__main__':
    db.create_all()