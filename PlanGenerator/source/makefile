
SOURCES = *.cpp
HEADERS = *.h

.SUFFIXES: 

CXXFLAGS += -g -Wall -Wextra -pthread -std=c++14

.PHONY: PlanGenerator

.PHONY: pkg
pkg: PlanGenerator.o

PlanGenerator.o: PlanGenerator.cpp PlanGenerator.h
	$(CXX) -c ${CPPFLAGS} $<

.PHONY: clean
clean: 
	rm -rf *.o PlanGenerator