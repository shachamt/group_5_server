from flask import Blueprint, render_template, redirect, url_for
# sign_in blueprint definition
search_mani = Blueprint('search_mani', __name__, static_folder='static', static_url_path='/search_mani', template_folder='templates')


# Routes

@search_mani.route('/search_mani')
def def_search_mani():
    return render_template('search_mani.html')