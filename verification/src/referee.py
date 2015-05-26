from checkio_referee import RefereeBase
from checkio_referee import covercodes, representations


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
    ENV_COVERCODE = {
        "python_3": py_cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_3": py_representation,
    }
