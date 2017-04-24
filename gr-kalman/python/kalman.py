#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 
# Based on Kalman_Example_2.py by Jason Bonior
# Modified by Jacob Vittitow, Sheldon Burks and Greyson Asthon
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

SAMP_RATE = 10
Q = 1e-5 # process variance
PMINUS = 0.0
XHATMINUS = 0.0
XHAT = 0.0
X_PREV = 0.0
V = 0.0
P = 0.1
DT = 1/SAMP_RATE
R = 0.3**2 # estimate of measurement variance, change to see effect

class kalman(gr.sync_block):
    """
    docstring for block kalman
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Kalman_Filter",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
	global XHAT
        global XHATMINUS #previous state estimate
        global PMINUS #previous prediction error global XHAT #current state estimate
        global X_PREV #previous observed state
        global V # Current Noise Measurement
	global P
        
        in_data = input_items[0]

	print 'Input Data'
	print in_data
        
        # time update
        XHATMINUS = XHAT + V * DT
        PMINUS = P + Q
        
        # measurement update
        K = PMINUS / ( PMINUS + R )
        XHAT = X_PREV + K * (in_data[0] - X_PREV)
        P = (1 - K) * PMINUS
        V = (XHAT - X_PREV)/DT
        X_PREV = XHAT
        
        output_items[0][:] = XHAT
	print 'Output Items'
        print output_items[0][0]
	print len(output_items[0])
        #return len(output_items[0])
	return output_items[0]
