CCLIBS=-lopencv_highgui -lopencv_core
RELDIR=bin
CCFLAGS=-Wall
GCC=g++
OCVDIR=opencv

cvex: ${OCVDIR}/cvex.cpp
	$(GCC) ${CCFLAGS} ${CCLIBS} $^ -o ${RELDIR}/$@

all: cvex
