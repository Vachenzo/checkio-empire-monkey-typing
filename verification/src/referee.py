from checkio_referee import RefereeBase
from checkio_referee import covercodes


import settings_env
from tests import TESTS


py_cover = """def cover(data, f):
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
