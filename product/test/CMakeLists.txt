cmake_minimum_required(VERSION 3.15)

set(THIS ExampleTests)

set(SOURCES
   ExampleTests.cpp
)

add_executable(${THIS} ${SOURCES})
target_link_libraries(${THIS} PUBLIC 
   gtest_main 
)

add_test(
   NAME ${THIS}
   COMMAND ${THIS}
)
