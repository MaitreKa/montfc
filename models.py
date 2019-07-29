from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


"""class User(db.Document, UserMixin):
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(default='')
    password = db.StringField()
    # User information
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')

    # Relationships
    roles = db.ListField(db.StringField(), default=[])

    # Setup Flask-User and specify the User data-model


user_manager = UserManager(app, db, User)
"""
class Employee(UserMixin, db.Document):

    __tablename__ = 'employees'
    email = db.StringField(max_length=120, required=True)
    username = db.StringField()
    first_name = db.StringField()
    last_name = db.StringField()
    password_hash = db.StringField()
    department_id = db.ListField(db.StringField())
    role_id = db.ListField(db.StringField())
    is_admin = db.BooleanField(default=False)

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

    # Set up user_loader
    def load_user(user_id):
        return Employee.query.get(int(user_id))

class Department(db.Document):
    __tablename__ = 'departments'
    nom = db.StringField(required= True)
    description = db.StringField(max_length=200)
    employees = db.ReferenceField('Employee', required=True)

    def __repr__(self):
        return '<Department: {}>'.format(self.name)

class Role(db.Document):
    __tablename__ = 'roles'
    nom = db.StringField(required=True)
    description = db.StringField()
    employees = db.ReferenceField('Employee', required=True)

    def __repr__(self):
        return '<Role: {}>'.format(self.name)