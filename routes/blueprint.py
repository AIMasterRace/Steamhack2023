from flask import Blueprint
from controllers.controller import home_page, map_page, rank_page, about_page, create_db, insert_db

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(home_page)
blueprint.route('/map', methods=['GET'])(map_page)
blueprint.route('/rank', methods=['GET'])(rank_page)
blueprint.route('/about', methods=['GET'])(about_page)

blueprint.route('/create', methods=['GET'])(create_db)
blueprint.route('/insert', methods=['GET'])(insert_db)