from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
business_profile = Blueprint('business_profile', __name__, static_folder='static', static_url_path='/business_profile', template_folder='templates')
from utilities.db.db_manager import dbManager



# Routes

@business_profile.route('/business_profile')
def def_business_profile():
    return render_template('business_profile.html')

@business_profile.route('/business_edit')
def def_business_edit():
    query_result = dbManager.fetch('SELECT * FROM customers')
    print('hi')
    if query_result:
        for record in query_result:
            print(record.Email)  # prints the record's ID
    return render_template('business_edit.html')

###### DB

