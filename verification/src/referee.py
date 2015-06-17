from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations, ENV_NAME


import settings_env
from tests import TESTS


def py_representation(test, function_name):
    return '{}("{}", {})'.format(function_name, test["input"][0], set(test["input"][1]))

py_cover = """def cover(f, data):
    return f(data[0], set(data[1]))
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "count_words"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "countWords"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: py_cover,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: py_representation,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
