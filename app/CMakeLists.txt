cmake_minimum_required(VERSION 3.10)
project(SmartHome)

# Habilitar soporte para compilación cruzada (esto dependerá de tu toolchain)
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_C_COMPILER arm-poky-linux-gnueabi-gcc)
set(CMAKE_CXX_COMPILER arm-poky-linux-gnueabi-g++)

# Agregar subdirectorios para las bibliotecas
add_subdirectory(liblight)
add_subdirectory(libdoor)
add_subdirectory(libcamera)

# Crear el ejecutable principal
add_executable(smart_home app/main.c)

# Enlazar las bibliotecas con el ejecutable
target_link_libraries(smart_home PRIVATE light door camera)