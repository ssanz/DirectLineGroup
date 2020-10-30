# -*- coding: utf-8 -*-
from flask import Flask, request


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('./config.py')

    def before_request():
        """
        This method will be executed before each request.
        It will authenticate the user (unless the path is in a list of unrestricted URLs).
        It will also initialise the start time which will be used for monitoring
        the execution time of the request.
        """
        if request.method == 'OPTIONS' or request.path in views.public_urls:
            return

    with app.app_context():
        # Import APP libraries.
        from app import views

        # Set before requests.
        app.before_request(before_request)

    return app
