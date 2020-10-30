# -*- coding: utf-8 -*-
from werkzeug.exceptions import NotFound

from flask import current_app, jsonify

from app.docs.setup import swaggerui_api_blueprint

# Set up public URLs.
public_urls = [
    '/',
    f"{current_app.config['SWAGGER_API_URL']}/",
    f"{current_app.config['SWAGGER_API_URL']}/swagger-ui.css",
    f"{current_app.config['SWAGGER_API_URL']}/swagger-ui-bundle.js",
    f"{current_app.config['SWAGGER_API_URL']}/swagger-ui-standalone-preset.js"
]

# Register blueprints.
# # Documentation.
current_app.register_blueprint(swaggerui_api_blueprint, url_prefix=current_app.config["SWAGGER_API_URL"])
# # Endpoints.
# # # TODO


@current_app.route('/')
def hello():
    return jsonify({"message": "Welcome to Direct Line Group!"}), 200


@current_app.errorhandler(NotFound)
def wsgi_tool_error_handler(e):
    """
    Error handler for a HTTP Exception raised by the APP.
    """
    status_code = e.code
    result = {
        "error_message": e.description,
        "error_code": e.name.upper().replace(" ", "_")
    }
    return jsonify(result), status_code


@current_app.errorhandler(Exception)
def handle_uncaught_error(e):
    """
    Error handler for unexpected internal server error exceptions. This exceptions must be fixed in case we got one.
    The purpose of this error handler is not to return any sensitive information while an error is not expected, like
    for example a user credentials.
    """
    status_code = 500

    result = {
        "error_message": "Unknown or unexpected error.",
        "error_code": "INTERNAL_SERVER_ERROR"
    }
    return jsonify(result), status_code
