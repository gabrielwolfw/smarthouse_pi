SUMMARY = "A simple framework for building complex web applications."
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=ffeffa59c90c9c4a033c7574f8f3fb75"

SRC_URI = "file://markupsafe-3.0.2.tar.gz"
SRC_URI[md5sum] = "8fe7227653f2fb9b1ffe7f9f2058998a"
SRC_URI[sha256sum] = "d283d37a890ba4c1ae73ffadf8046435c76e7bc2247bbb63c00bd1a709c6544b"

S = "${WORKDIR}/markupsafe-3.0.2"

inherit setuptools3


