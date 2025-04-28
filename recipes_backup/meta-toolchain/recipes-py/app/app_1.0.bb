SUMMARY = "Servidor Flask para Casa Inteligente"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

SRC_URI = "file://app-1.0.tar.gz"
S = "${WORKDIR}/app-1.0"

inherit systemd

RDEPENDS:${PN} += "python3 python3-flask python3-werkzeug markupsafe python3-click python3-jinja2 python3-blinker python3-itsdangerous python3-flask-cors"

SYSTEMD_SERVICE:${PN} = "smarthouse.service"

do_install:append() {
    install -d ${D}/usr/smarthouse
    cp -r ${S}/* ${D}/usr/smarthouse/
    install -D -m 0644 ${S}/smarthouse.service ${D}${systemd_system_unitdir}/smarthouse.service
}

FILES:${PN} += "/usr/smarthouse"
