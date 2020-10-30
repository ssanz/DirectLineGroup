# -*- coding: utf-8 -*-
from functools import reduce
from werkzeug.exceptions import BadRequest

from flask import current_app, request

ERROR_MISSING_REQUIRED = "Missing 'numbers_to_add' in the body which is a required field. Please review the docs."
ERROR_WRONG_TYPE = "Provided field 'numbers_to_add' must be a not empty iterable of numbers. Please review the docs."


@current_app.route("/total", methods=['POST'])
def get_total_sum():
    """
    Requests to calculate the total sum of the provided numbers.
    """
    body = request.get_json()

    try:
        numbers_to_add = body["numbers_to_add"]
    except KeyError:
        raise BadRequest(ERROR_MISSING_REQUIRED)

    try:
        total = reduce(lambda x, y: x + y, numbers_to_add)
    except TypeError:
        raise BadRequest(ERROR_WRONG_TYPE)

    if not isinstance(total, (int, float)):
        raise BadRequest(ERROR_WRONG_TYPE)

    response = {
        "total": total
    }

    return response, 200
