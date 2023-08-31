#!/usr/bin/env python3

#   Defining a persisting a simple schema (db) using sqlAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine  # create_engine: This is a function provided by SQLAlchemy that creates a database engine. The database engine acts as the interface between your Python code and the actual database. It manages the connections and communication with the database.

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    __tablename__ = 'Students'

    id = Column(Integer(), primary_key = True)
    name = Column(String())


if __name__ == '__main__':
    # Create a SQLite database engine
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine) # Create the tables in the database based on the defined models