from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}

@user_routes.route('/current')
def present_user():
    """
    Populates the current user from flask_login package
    """
    if current_user.is_anonymous:
        return {"user": None}
    return {"user": current_user.to_dict()}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    if not user:
        return {'errors': {'message': 'User not found'}}, 404
    return user.to_dict()
