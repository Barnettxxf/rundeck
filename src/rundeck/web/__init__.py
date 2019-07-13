from flask import Flask
from .config import ProductionConfig
from ..client import Rundeck


def create_app(cfg=ProductionConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(cfg)

    @app.before_request
    def open_rd():
        if not g.get('rd'):
            username = app.config['RUNDECK_USERNAME']
            password = app.config['RUNDECK_PASSWORD']
            port = app.config['RUNDECK_PORT']
            server = app.config['RUNDECK_SERVER']
            token = app.config['RUNDECK_TOKEN']
            g.rd = Rundeck(server=server, port=port, username=username, password=password, token=token)

    @app.teardown_appcontext
    def close_rd(r):
        rd = g.pop('rd', None)
        if rd:
            rd.close()

    from .index import bp
    app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='index')

    return app
