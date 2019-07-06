from flask import Flask
from .config import ProductionConfig


def create_app(cfg=ProductionConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(cfg)

    from .index import bp
    app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='index')

    return app
