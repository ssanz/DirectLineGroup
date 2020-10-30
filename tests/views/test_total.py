# -*- coding: utf-8 -*-
import json

from app.views.total import ERROR_MISSING_REQUIRED, ERROR_WRONG_TYPE
# 'test_session' is a PyTest fixture to be used in the tests. Do not remove.
from tests.conftests import test_session


def test_total_succeed(test_session):
    """
    Test total succeed.
    The total endpoint must return a 200 response with the correct value and format.
    """
    url = "/total"
    body = {
        'numbers_to_add': list(range(10000001))
    }

    # Run the request.
    response = test_session.post(url, data=json.dumps(body), content_type="application/json")

    assert response.status_code == 200
    assert response.json["total"] == 50000005000000


def test_total_missing_field(test_session):
    """
    Test total missing field.
    The total endpoint must return a 400 response if a required field is missing.
    """
    url = "/total"
    body = {}

    # Run the request.
    response = test_session.post(url, data=json.dumps(body), content_type="application/json")

    assert response.status_code == 400
    assert response.json["error_message"] == ERROR_MISSING_REQUIRED


def test_total_wrong_type(test_session):
    """
    Test total wrong type.
    The total endpoint must return a 400 response if the fields are in an unexpected type.
    """
    url = "/total"
    bodies = [
        {'numbers_to_add': "test"},
        {'numbers_to_add': ["t", "e", "s", "t"]},
        {'numbers_to_add': ["t", "e", "s", "t", 1]}
    ]

    for body in bodies:
        # Run the request.
        response = test_session.post(url, data=json.dumps(body), content_type="application/json")

        assert response.status_code == 400
        assert response.json["error_message"] == ERROR_WRONG_TYPE
