from flask import Blueprint, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from app.api.aws import upload_file_to_s3, get_unique_filename, remove_file_from_s3

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'message': 'Authentication required'}, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    if "email" in form.errors:
        if form.errors["email"][0] == "Email provided not found.":
            return {"message": "Invalid credentials"}, 401
    if "password" in form.errors:
        if form.errors["password"][0] == 'Password was incorrect.':
            return {"message": "Invalid credentials"}, 401
    return {"message": "Bad Request", "errors": form.errors}, 400



@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()

    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        image = form.image_url.data
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
            # if the dictionary doesn't have a url key
            form.errors['image'][0] == 'File upload failed'

        url = upload["url"]

        user = User(
            name=form.data['name'],
            email=form.data['email'],
            password=form.data['password'],
            image_url=url,
            is_artist=form.data['is_artist']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    # return form.errors, 401
    if form.errors["email"][0] == "Email address is already in use.":
        return {"message": "Email already exists", "errors": form.errors}, 500
    else:
        return form.errors, 400


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'message': 'Forbidden'}, 403