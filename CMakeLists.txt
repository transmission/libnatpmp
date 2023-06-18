cmake_minimum_required(VERSION 2.8.12)

if(POLICY CMP0048)
	cmake_policy(SET CMP0048 NEW)
endif()

file(STRINGS VERSION PVER)

project(natpmp
        LANGUAGES C
        VERSION ${PVER}
        DESCRIPTION "A portable and fully compliant implementation of the NAT-PMP protocol"
        HOMEPAGE_URL "https://github.com/miniupnp/libnatpmp"
)

set (NATPMP_SOURCES
        natpmp.c
        getgateway.c
)

if (WIN32)
    set (NATPMP_SOURCES ${NATPMP_SOURCES} wingettimeofday.c)
endif (WIN32)

# Library itself
add_library(natpmp STATIC ${NATPMP_SOURCES})
target_include_directories(natpmp PUBLIC ${CMAKE_CURRENT_LIST_DIR})
target_compile_definitions(natpmp PRIVATE -DENABLE_STRNATPMPERR)

if (WIN32)
	target_link_libraries(natpmp PUBLIC ws2_32 iphlpapi)
	target_compile_definitions(natpmp PUBLIC -DNATPMP_STATICLIB)
endif (WIN32)

# Executables
add_executable(natpmpc natpmpc.c)
target_link_libraries(natpmpc natpmp)

add_executable(testgetgateway
	testgetgateway.c
	getgateway.c)
target_link_libraries(testgetgateway natpmp)

# install
include(GNUInstallDirs)

install(TARGETS natpmp natpmpc
	RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})

install(FILES natpmp.h
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

