# Metadata de la receta
SUMMARY = "Recipe Library GPIO"
DESCRIPTION = "Recipe created by bitbake-layers for gpio"

SECTION = "libs"
LICENSE = "GPL-2.0-only"
LIC_FILES_CHKSUM = "file://COPYING;md5=570a9b3749dd0463a1778803b12a6dce"

# Origen del código fuente
SRC_URI = "file://libgpio-1.0.tar.gz"

S = "${WORKDIR}/${PN}-${PV}"

inherit autotools

EXTRA_OECONF += " --enable-shared"

PROVIDES += "${PN}-staticdev"

FILES:${PN} = "${libdir}/*.so* ${bindir}/* "
FILES:${PN}-staticdev = "${includedir} ${datadir}"



