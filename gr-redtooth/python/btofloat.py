
import numpy as np
from gnuradio import gr

from bitarray import bitarray

preamble = []
access_code = []
header = []
float_output = []
payload_rest = []
i = 0
file = []
packet = []
indices = []


class btofloat(gr.sync_block):
	"""
	docstring for block btofloat
	"""
	def __init__(self):
		gr.sync_block.__init__(self,
			name="btofloat",
			in_sig=[], #no input items
			out_sig=[np.int8])
			
	def work(self, input_items, output_items):
		global preamble
		global access_code
		global header
		global float_output
		global payload_rest
		global i
		global file
		global packet
		global indices
		
		#do work
		
		file = open("/home/sdr/Capstone/packet.txt")
		packet = file.readlines()[0]
			
		#indices = range(129, 161) #start at 0+4+72+54-1, end 32 bits later

		bin_repr = packet[0:2167]
		ba = bitarray(bin_repr)
		
		out_index = 0
		while ba.length() > 0:
			data = ba[0:7]
			out = 0
			for bit in data:
				out = (out << 1) | bit
			del ba[0:7]
			output_items[0][out_index] = np.int8(out)
			out_index = out_index + 1
	
		print(output_items[0])
		return len(output_items[0])
