#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ''

        @property
        def cities(self):
            """Getter"""
            city_lst = []
            states = storage.all(State)
            for state_id, state in states.items():
                print(state)
