INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_REDTOOTH redtooth)

FIND_PATH(
    REDTOOTH_INCLUDE_DIRS
    NAMES redtooth/api.h
    HINTS $ENV{REDTOOTH_DIR}/include
        ${PC_REDTOOTH_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    REDTOOTH_LIBRARIES
    NAMES gnuradio-redtooth
    HINTS $ENV{REDTOOTH_DIR}/lib
        ${PC_REDTOOTH_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(REDTOOTH DEFAULT_MSG REDTOOTH_LIBRARIES REDTOOTH_INCLUDE_DIRS)
MARK_AS_ADVANCED(REDTOOTH_LIBRARIES REDTOOTH_INCLUDE_DIRS)

