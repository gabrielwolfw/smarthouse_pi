SUMMARY = "A fast and expressive template engine for Python"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.rst;md5=4cda9a0ebd516714f360b0e9418cfb37"

SRC_URI = "file://itsdangerous-2.1.2.tar.gz"
SRC_URI[sha256sum] = "8fa99a7841e6c2d1e1d1e6c2c3e2e3e2d1e6c2e3e2e3e2e3e2e3e2e3e2e3e2e"

S = "${WORKDIR}/itsdangerous-2.1.2"

inherit setuptools3
