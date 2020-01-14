from app import db

class School(db.Model):
    """ School table definition """

    _tablename_ = "school"

    # fields of the Student table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False, default="")
    cut_off_points = db.Column(db.Integer(100), nullable=False, default="")
    number_of_students = db.Column(db.Integer(1000), nullable=False, default="")

    def __init__(self, name, cut_off_points, number_of_students):
        """ initialize with name, cut off points and no. of Students """
        self.name = name
        self.cut_off_points = cut_off_points
        self.number_of_students = number_of_students
