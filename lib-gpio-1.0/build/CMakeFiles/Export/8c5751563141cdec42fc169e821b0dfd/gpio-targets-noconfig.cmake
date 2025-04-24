#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gpio::gpio" for configuration ""
set_property(TARGET gpio::gpio APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(gpio::gpio PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libgpio.so"
  IMPORTED_SONAME_NOCONFIG "libgpio.so"
  )

list(APPEND _cmake_import_check_targets gpio::gpio )
list(APPEND _cmake_import_check_files_for_gpio::gpio "${_IMPORT_PREFIX}/lib/libgpio.so" )

# Import target "gpio::test_gpio" for configuration ""
set_property(TARGET gpio::test_gpio APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(gpio::test_gpio PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/bin/test_gpio"
  )

list(APPEND _cmake_import_check_targets gpio::test_gpio )
list(APPEND _cmake_import_check_files_for_gpio::test_gpio "${_IMPORT_PREFIX}/bin/test_gpio" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
