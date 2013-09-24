#!/usr/bin/env python
# Copyright 2013 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import urllib.parse

import lxml.html
import pytest
import requests


class TestSession(requests.Session):

    def request(self, method, url, *args, **kwargs):
        if url.startswith("/"):
            url = urllib.parse.urljoin(self.base_url, url)

        resp = super(TestSession, self).request(method, url, *args, **kwargs)

        if resp.headers["Content-Type"] in {"text/html"}:
            resp.html = lxml.html.fromstring(resp.content)

        return resp


def pytest_addoption(parser):
    group = parser.getgroup("warehouse")
    group._addoption(
        "--base-url",
        dest="base_url",
        help="The url that the acceptance tests should be run against.",
    )


@pytest.fixture
def request(pytestconfig):
    session = TestSession()
    session.base_url = pytestconfig.option.base_url
    return session
