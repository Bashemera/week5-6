from flask import Blueprint

from mydiary.diary_api import DiaryApi

index = Blueprint('index_view', __name__)

diary_app = Blueprint('diary_app', __name__)

diary_templates = DiaryApi.as_view('mydiary')

@index.route('/diary/api/v1/mydiary/', methods=['GET',])
def index():
    return "This Shot"

@index.route('/diary/api/v1/mydiary/hello')
def api_works():
    return "Hay this really works"

diary_app.add_url_rule('/diary/api/v1/mydiary/', defaults={'diary_page_id': None},
                     view_func=diary_templates, methods=['GET',])
diary_app.add_url_rule('/diary/api/v1/mydiary/', view_func=diary_templates, methods=['POST',])
diary_app.add_url_rule('/diary/api/v1/mydiary/<int:diary_page_id>', view_func=diary_templates,
                     methods=['GET', 'PUT', 'DELETE',])
