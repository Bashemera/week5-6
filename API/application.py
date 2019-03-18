from flask import Flask


def create_api():
    # create and configure api
    app = Flask(__name__)
    app.config.from_pyfile('refactor.py')

    # import blueprints
    from mydiary.templates import index
    from mydiary.templates import diary_app

    # register blueprints
    app.register_blueprint(index)
    app.register_blueprint(diary_app)

    return app
