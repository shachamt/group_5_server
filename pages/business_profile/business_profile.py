from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
business_profile = Blueprint('business_profile', __name__, static_folder='static', static_url_path='/business_profile', template_folder='templates')


# Routes

@business_profile.route('/business_profile')
def def_business_profile():
    return render_template('business_profile.html')

@business_profile.route('/business_edit')
def def_business_edit():
    return render_template('business_edit.html')