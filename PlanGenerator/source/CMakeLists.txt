cmake_minimum_required(VERSION 3.15)

set(THIS PlanGenerator)
set(SOURCES
   PlanGenerator.cpp
)
set(HEADERS
   PlanGenerator.h
   Qgc_Mission.h
)

add_library(${THIS} ${SOURCES} ${HEADERS})
