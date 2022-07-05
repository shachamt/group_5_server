from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')


# Routes

@sign_up.route('/sign_up_mani')
def def_sign_up_mani():
    return render_template('sign_up_mani.html')

@sign_up.route('/sign_up_customer')
def def_sign_up_customer():
    return render_template('sign_up_customer.html')