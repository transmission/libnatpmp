cmake_minimum_required(VERSION 2.6)

project(natpmp)

add_definitions( -DENABLE_STRNATPMPERR )
add_definitions( -DNATPMP_STATICLIB )
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_library(natpmp STATIC
        natpmp.c
        getgateway.c
        wingettimeofday.c
)