#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/sdr/Capstone/gr-redtooth/python
export PATH=/home/sdr/Capstone/gr-redtooth/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/sdr/Capstone/gr-redtooth/build/swig:$PYTHONPATH
/usr/bin/python2 /home/sdr/Capstone/gr-redtooth/python/qa_btofloat.py 
