CCLIBS=-lopencv_highgui -lopencv_core
RELDIR=bin
CCFLAGS=-Wall
GCC=g++
OCVDIR=opencv

basic: ${OCVDIR}/basic.cpp
	$(GCC) ${CCFLAGS} ${CCLIBS} $^ -o ${RELDIR}/$@

clean:
	rm ${RELDIR}/*

.phony: clean

all: cvex
