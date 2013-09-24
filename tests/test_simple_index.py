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


def test_api_version(request):
    """
    Tests that the Repository's simple index uses an appropriate api-version.

    At this time the only acceptable value is "2".
    """
    resp = request.get("/simple/")

    assert resp.status_code == 200
    assert resp.headers["Content-Type"].split(";")[0] == "text/html"
    assert resp.html.xpath("//meta[@name='api-version']/@value") == ["2"]
