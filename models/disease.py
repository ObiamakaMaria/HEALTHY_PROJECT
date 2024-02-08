#!/usr/bin/env python3

"""
This is the module for Diseases that are talked about on the website
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table


class Disease(BaseModel, Base):
    __tablename__ = 'diseases'

    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    symptoms = Column(String(500), nullable=False)
    prevention_methods = Column(String(500), nullable=False)


