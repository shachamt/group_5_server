from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
sign_in = Blueprint('sign_in', __name__, static_folder='static', static_url_path='/sign_in', template_folder='templates')


# Routes

@sign_in.route('/sign_in')
def def_sign_in():
    return render_template('sign_in.html')