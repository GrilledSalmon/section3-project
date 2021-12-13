import os
from flask import Flask

CSV_FILEPATH = os.path.join(os.getcwd(), __name__, 'users.csv') 
TMP_FILEPATH = os.path.join(os.getcwd(), __name__, 'tmp.csv') 

def create_app(config=None):

    app = Flask(__name__)

    if config is not None:
        app.config.update(config)

    from flask_app.views.main_views import main_bp
    from flask_app.views.user_views import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)