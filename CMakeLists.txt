cmake_minimum_required(VERSION 2.6)

project(natpmp)

add_definitions( -DENABLE_STRNATPMPERR )
if (WIN32)
	add_definitions( -DNATPMP_STATICLIB )
endif (WIN32)
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set (NATPMP_SOURCES
        natpmp.c
        getgateway.c
)

if (WIN32)
    set (NATPMP_SOURCES ${NATPMP_SOURCES} wingettimeofday.c)
endif (WIN32)

add_library(natpmp STATIC ${NATPMP_SOURCES})

add_executable(natpmpc natpmpc.c)
target_link_libraries(natpmpc natpmp)

add_executable(testgetgateway
	testgetgateway.c
	getgateway.c)
