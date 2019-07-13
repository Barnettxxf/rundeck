import click

from .web import create_app, config


@click.command(help='Start web server for rundeck')
@click.option('--host', '-a', help='web server host', default='localhost')
@click.option('--wport', '-wp', help='web server port', default=5000, type=int)
@click.option('--server', '-s', help='rundeck server', default='localhost')
@click.option('--port', '-p', help='rundeck server port', default=4440, type=int)
@click.option('--username', '-u', help='rundeck server username', default='admin')
@click.option('--password', '-p', help='rundeck server password', default='admin')
@click.option('--token', '-t', help='rundeck server token', default=None)
@click.option('--cfg', '-c', help='rundeck server config type', default='prod')
def run(host, wport, server, port, username, password, token, cfg):
    _cfg = {
        'prod': config.ProductionConfig,
        'test': config.TestingConfig,
        'dev': config.DevelopmentConfig,
    }
    app = create_app(_cfg[cfg])

    app.config['RUNDECK_SERVER'] = server
    app.config['RUNDECK_PORT'] = port
    app.config['RUNDECK_USERNAME'] = username
    app.config['RUNDECK_PASSWORD'] = password
    app.config['RUNDECK_TOKEN'] = token

    app.run(host=host, port=wport)


@click.group()
def cli():
    pass


cli.add_command(run)
