SUMMARY = "A simple wrapper around optparse for powerful command line utilities"
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.rst;md5=1fa98232fd645608937a0fdc82e999b8"

SRC_URI = "file://click-8.1.7.tar.gz"
SRC_URI[sha256sum] = "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"

S = "${WORKDIR}/click-8.1.7"

inherit pypi setuptools3
