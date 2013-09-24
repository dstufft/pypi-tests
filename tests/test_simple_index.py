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


def test_api_version(request):
    """
    Tests that the Repository's simple index uses an appropriate api-version.

    At this time the only acceptable value is "2".
    """
    resp = request.get("")

    assert resp.status_code == 200
    assert resp.headers["Content-Type"].split(";")[0] == "text/html"
    assert resp.html.xpath("//meta[@name='api-version']/@value") == ["2"]


def test_simple_index_looks_like_list_of_names(request):
    resp = request.get("")

    assert resp.status_code == 200
    assert resp.headers["Content-Type"].split(";")[0] == "text/html"
    assert "pypi.testpkg" in resp.html.xpath("//a[@href]/text()")


def test_api_version_package_page(request):
    resp = request.get("pypi.testpkg/")

    assert resp.status_code == 200
    assert resp.headers["Content-Type"].split(";")[0] == "text/html"
    assert resp.html.xpath("//meta[@name='api-version']/@value") == ["2"]


def test_package_page_redirect(request):
    resp = request.get("pypi.testpkg", allow_redirects=False)

    assert resp.status_code in {301, 302, 303, 307}
    assert resp.headers["Location"].endswith("/pypi.testpkg/")


def test_package_page_version_urls(request):
    resp = request.get("pypi.testpkg/")

    filenames = set(
        urllib.parse.urlparse(url).path.rsplit("/", 1)[-1]
        for url in resp.html.xpath("//a[@rel='internal']/@href")
    )

    assert resp.status_code == 200
    assert resp.headers["Content-Type"].split(";")[0] == "text/html"
    assert filenames == {
        "pypi.testpkg-1.0.tar.gz",
        "pypi.testpkg-1.5.tar.gz",
        "pypi.testpkg-2.0.tar.gz",
    }
