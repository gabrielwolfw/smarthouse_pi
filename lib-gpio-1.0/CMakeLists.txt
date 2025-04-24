cmake_minimum_required(VERSION 3.10)

# Nombre del proyecto
project(gpio_library VERSION 1.0 LANGUAGES C)

# Asegurarse de que estamos en compilación cruzada
if(CMAKE_CROSSCOMPILING)
    message(STATUS "Doing cross compilation")
endif()

# Configurar opciones de compilación
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

# Habilitar la generación de biblioteca compartida
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Crear la biblioteca compartida
add_library(gpio SHARED
    src/gpio.c
)

# Configurar los includes
target_include_directories(gpio
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

# Crear el ejecutable de prueba
add_executable(test_gpio
    src/test_gpio.c
)

# Vincular la biblioteca al ejecutable de prueba
target_link_libraries(test_gpio
    PRIVATE gpio
)

# Configurar la instalación
include(GNUInstallDirs)
set(INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/cmake/gpio)

install(TARGETS gpio test_gpio
    EXPORT gpio-targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(FILES
    include/gpio.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/gpio
)

# Exportar los targets
install(EXPORT gpio-targets
    FILE gpio-targets.cmake
    NAMESPACE gpio::
    DESTINATION ${INSTALL_CONFIGDIR}
)