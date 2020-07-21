cmake_minimum_required(VERSION 3.15)

set(THIS Product)

project(${THIS} C CXX)

set(CMAKE_C_STANDARD 99
    CMAKE_CXX_STANDARD 14)

enable_testing()

add_subdirectory(googletest)
add_subdirectory(test)
