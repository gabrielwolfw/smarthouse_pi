lib_LTLIBRARIES = libgpio.la
libgpio_la_SOURCES = gpio.c
libgpio_la_CFLAGS = -I$(top_srcdir)/include
libgpio_la_LDFLAGS = -version-info 0:0:0

bin_PROGRAMS = test_gpio
test_gpio_SOURCES = test_gpio.c
test_gpio_LDADD = libgpio.la
test_gpio_CFLAGS = -I$(top_srcdir)/include