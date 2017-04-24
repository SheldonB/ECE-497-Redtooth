INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_KALMAN kalman)

FIND_PATH(
    KALMAN_INCLUDE_DIRS
    NAMES kalman/api.h
    HINTS $ENV{KALMAN_DIR}/include
        ${PC_KALMAN_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    KALMAN_LIBRARIES
    NAMES gnuradio-kalman
    HINTS $ENV{KALMAN_DIR}/lib
        ${PC_KALMAN_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(KALMAN DEFAULT_MSG KALMAN_LIBRARIES KALMAN_INCLUDE_DIRS)
MARK_AS_ADVANCED(KALMAN_LIBRARIES KALMAN_INCLUDE_DIRS)

