cmake_minimum_required(VERSION 3.15)

set(THIS PlanGeneratorTest)

set(SOURCES
   PlanGeneratorTest.cpp
)

add_executable(${THIS} ${SOURCES})
target_link_libraries(${THIS} PUBLIC
   gtest_main
   gmock_main
   PlanGenerator
)

add_test(
   NAME ${THIS}
   COMMAND ${THIS}
)
