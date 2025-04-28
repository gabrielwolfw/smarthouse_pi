SUMMARY = "A simple wrapper around optparse for powerful command line utilities"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.rst;md5=42cd19c88fc13d1307a4efd64ee90e4e"

SRC_URI = "file://blinker-1.7.0.tar.gz"
SRC_URI[sha256sum] = "e6820ff6fa4e4d1d8e2747c2283749c3f547e4fee112b98555cdcdae32996182"


S = "${WORKDIR}/blinker-1.7.0"

inherit pypi setuptools3
