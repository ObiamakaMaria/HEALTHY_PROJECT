#!/usr/bin/env python3
"""
This is the module for Article created on the website
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

class Article(BaseModel, Base):
    __tablename__ = 'articles'

    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(String(60), ForeignKey('users.id'), nullable=False)


