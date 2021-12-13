import os
from flask import Flask

MODEL_FILEPATH = os.path.join(os.getcwd(), __name__, 'stock_pred_model.pkl') 
DB_FILEPATH = os.path.join(os.getcwd(), __name__, 'stock_DB.db') 

def create_app(config=None):

    app = Flask(__name__)

    if config is not None:
        app.config.update(config)

    from flask_app.views.main_views import main_bp
    from flask_app.views.pred_views import pred_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(pred_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)