AC_PREREQ([2.69])
AC_INIT([libgpio], [1.0], [gabrielwolfw@example.com])

# Directorios auxiliares (deben ir ANTES de AM_INIT_AUTOMAKE)
AC_CONFIG_AUX_DIR([build-aux])
AC_CONFIG_MACRO_DIRS([m4])

# Inicialización de automake
AM_INIT_AUTOMAKE([-Wall -Werror foreign])

# Verificación del código fuente
AC_CONFIG_SRCDIR([src/gpio.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET

# Agregar soporte para archivador (requerido por el warning)
AM_PROG_AR

# Inicialización de libtool
LT_INIT

# Checks for libraries
AC_CHECK_LIB([pthread], [pthread_create])

# Checks for header files
AC_CHECK_HEADERS([stdlib.h unistd.h])

# Set installation directories
AC_PREFIX_DEFAULT([/usr])

AC_CONFIG_FILES([
    Makefile
    src/Makefile
])
AC_OUTPUT