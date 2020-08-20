vpath %.cpp source test
vpath %.h source

GTEST_DIR = googletest/googletest
GMOCK_DIR = googletest/googlemock

GTEST_HEADERS = ${GTEST_DIR}/include/gtest/*.h \
		${GTEST_DIR}/include/gtest/internal/*.h 

GMOCK_HEADERS = ${GMOCK_DIR}/include/gmock/*.h \
		${GMOCK_DIR}/include/gmock/internal/*.h \
		${GTEST_HEADERS}

GTEST_SRC_ = ${GTEST_DIR}/src/*.cc ${GTEST_DIR}/src/*.h ${GTEST_HEADERS}
GMOCK_SRC_ = ${GMOCK_DIR}/src/*.cc ${GMOCK_HEADERS}

CPPFLAGS += -isystem ${GTEST_DIR}/include -isystem ${GMOCK_DIR}/include 
CXXFLAGS += -g -Wall -Wextra -pthread -std=c++14

.PHONY: x
x: PlanGeneratorTest.o PlanGenerator.o gmock_main.a
	g++ ${CXXFLAGS} ${CPPFLAGS} -lpthread $^ -o $@

PlanGeneratorTest.o: PlanGeneratorTest.cpp
	g++ -c ${CPPFLAGS} $<

PlanGenerator.o: PlanGenerator.cpp PlanGenerator.h
	g++ -c ${CPPFLAGS} $<


gtest-all.o: $(GTEST_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) -I$(GMOCK_DIR) $(CXXFLAGS) -c $(GTEST_DIR)/src/gtest-all.cc

gmock-all.o: $(GMOCK_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) -I$(GMOCK_DIR) $(CXXFLAGS) -c $(GMOCK_DIR)/src/gmock-all.cc

gmock_main.o: $(GMOCK_SRCS_)
	$(CXX) $(CPPFLAGS) -I$(GTEST_DIR) -I$(GMOCK_DIR) $(CXXFLAGS) -c $(GMOCK_DIR)/src/gmock_main.cc

gmock.a: gmock-all.o gtest-all.o
	${AR} ${ARFLAGS} $@ $^

gmock_main.a: gmock-all.o gtest-all.o gmock_main.o
	${AR} ${ARFLAGS} $@ $^

.PHONY: clean
clean: 
	rm -f *.o x gmock.a gmock_main.a

