SUMMARY = "A fast and expressive template engine for Python"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.rst;md5=5dc88300786f1c214c1e9827a5229462"

SRC_URI = "file://jinja2-3.1.3.tar.gz"
SRC_URI[sha256sum] = "6f7d4f3fd1d7d0319d92a974b7dcad3bb6a8f6f3e19c92a5e7d82a5a2ae3e3b0"

S = "${WORKDIR}/jinja2-3.1.3"

inherit setuptools3
