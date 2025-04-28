SUMMARY = "A simple framework for building complex web applications."
LICENSE = "BSD-3-Clause"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=5dc88300786f1c214c1e9827a5229462"

SRC_URI = "file://python3-werkzeug-3.1.3.tar.gz"
SRC_URI[md5sum] = "b6005d403d01d08b9fe2330a0cfea05a"
SRC_URI[sha256sum] = "0723ce945c19328679790e3282cc758aa4a6040e4bb330f53d30fa546d44746"

S = "${WORKDIR}/python3-werkzeug-3.1.3"

inherit setuptools3


