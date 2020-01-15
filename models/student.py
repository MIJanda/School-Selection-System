from app import db

from models.parent import Parent
from models.school import School

class Student(db.Model, Parent):
    """ Student table definition """

    _tablename_ = "student"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    aggregate = db.Column(db.Integer, nullable=False)
    """ student choices """
    first_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    second_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    third_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)        
    fourth_choice = db.Column("first_choice", db.Integer, db.ForeignKey(School.id, ondelete='CASCADE'), nullable=False)
    is_assigned = db.Column("is_assigned", db.Integer, default=0)

    def __init__(self, name, aggregate):
        """ initialize with name and aggregate """
        self.name = name
        self.aggregate = aggregate

   
