# -*- coding: utf-8 -*-
"""Stream processing"""
# :copyright: (c) 2017, Robinhood Markets
#             All rights reserved.
# :license:   BSD (3 Clause), see LICENSE for more details.
import re
from typing import NamedTuple

__version__ = '1.0.0'
__author__ = 'Robinhood Markets'
__contact__ = 'asksol@robinhood.com'
__homepage__ = 'https://github.com/robinhoodmarkets/faust'
__docformat__ = 'restructuredtext'

# -eof meta-


class version_info_t(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: str


# bumpversion can only search for {current_version}
# so we have to parse the version here.
_temp = re.match(
    r'(\d+)\.(\d+).(\d+)(.+)?', __version__).groups()
VERSION = version_info = version_info_t(
    int(_temp[0]), int(_temp[1]), int(_temp[2]), _temp[3] or '', '')
del(_temp)
del(re)

from .app import App                         # noqa: E402
from .models import Record                   # noqa: E402
from .streams import Stream, topic           # noqa: E402
from .tables import Table                    # noqa: E402

__all__ = [
    'App', 'Record', 'Stream', 'Table', 'topic',
]
