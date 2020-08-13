# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:32:59 2020

@author: rkbra
"""

from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


class FlightDataRequestSchema(Schema):
    Airline = fields.Str(allow_none=True)
    Date_of_Journey = fields.Str(allow_none=True)
    Source = fields.Str(allow_none=True)
    Destination = fields.Str(allow_none=True)
    Route = fields.Str(allow_none=True)
    Dep_Time = fields.Str(allow_none=True)
    Arrival_Time = fields.Str(allow_none=True)
    Duration = fields.Str(allow_none=True)
    Total_Stops = fields.Str(allow_none=True)
    Additional_Info = fields.Str(allow_none=True)


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = FlightDataRequestSchema(strict=True, many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
