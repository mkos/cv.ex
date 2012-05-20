LIBS=-lopencv_highgui -lopencv_core
BINDIR=bin
CCFLAGS=-Wall
CC=g++

cvex: cvex.cpp
	${CC} ${CFLAGS} cvex.cpp -o ${BINDIR}/cvex ${LIBS}

all: cvex
