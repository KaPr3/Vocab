from flask import Flask


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '1d62e19e549cb64528900add12e05b87'
	from web.main.routes import main
	from web.errors.handlers import errors
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app