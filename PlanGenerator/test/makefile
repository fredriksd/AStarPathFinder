
#AR := $(AR.STATIC)

.SUFFIXES: 

CPPFLAGS += -isystem ../googletest/googletest/include -isystem ../googletest/googlemock/include
CXXFLAGS += -g -Wall -Wextra -pthread -std=c++14

.PHONY: x
x: PlanGeneratorTest.o PlanGenerator.o gtest_main.a gmock_main.a 
	$(strip $(CXX) ${CXXFLAGS} ${CPPFLAGS} -lpthread $^ -o $@)

PlanGeneratorTest.o: PlanGeneratorTest.cpp
	$(strip $(CXX) -c ${CPPFLAGS} $<)

PlanGenerator.o:
	$(strip $(MAKE) -C ../source pkg)
	cp ../source/PlanGenerator.o .

gtest_main.a:
	$(strip $(MAKE) -C ../googletest GTEST)
	cp ../googletest/gtest_main.a .

gmock_main.a:
	$(strip $(MAKE) -C ../googletest GMOCK)
	cp ../googletest/gmock_main.a .

.PHONY: clean
clean: 
	rm -f *.o x gmock.a gmock_main.a gtest_main.a
	$(strip $(MAKE) -C ../source clean)
	$(strip $(MAKE) -C ../googletest clean)

