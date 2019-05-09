
#ifneq ($(MAKECMSGOALS), clean)
#		include $(SRCS:.C=.)

CC = g++
ROOT =$(shell root-config --cflags --glibs)

CFLAGS = -fpic -g $(ROOT)
LDFLAGS = -shared $(ROOT)
DEPS = $(shell echo *.h)
FBASE = /Users/tabris/frameLite/
LPATH =$(FBASE)/lib/ 
PYTHIA8PATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc700/external/pythia8/240
MOREPYTHIA8=-I $(PYTHIA8PATH)/include -L $(PYTHIA8PATH)/lib -lpythia8

FASTJETPATH = /cvmfs/cms.cern.ch/slc6_amd64_gcc700/external/fastjet/3.3.0/bin
FASTJET=$(shell $(FASTJETPATH)/fastjet-config --cxxflags --libs --plugins)

SRCS=$(wildcard *.C)
OBJS=$(SRCS:%.C=%.o)
BINS=$(SRCS:%.C=%)

all: $(OBJS) $(BINS)

$(OBJS): $(SRCS) 
	@echo $(SRCS)
	$(CC) $(ROOT) $(MOREPYTHIA8) $(INCLUDE) $(FASTJET) -c $< -o $@ 

$(BINS): $(OBJS) 
	$(CC) $(ROOT) $(MOREPYTHIA8) $(FASTJET) $(INCLUDE) $< -o $@

.PHONY: clean

clean:
	@echo $(MOREPYTHIA8)
	rm -rf *.o *.*~ ../plugin/*.*~
