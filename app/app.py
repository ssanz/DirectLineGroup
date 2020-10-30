# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        pass

    return app
