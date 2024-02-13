#!/usr/bin/env python3

"""
Module for the Website users registered through authenticaiton
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Representation of users"""

    __tablename__ = 'users'

    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(60), nullable=False)

    articles = relationship('Article', backref='users', cascade="all, delete, delete-orphan")


