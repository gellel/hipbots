#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings class
from strings import String




class Sentence (String):

	###################################################################
	### creates complete string from pseudo randomly selected parts ###
	###################################################################

	def create (self):
		pass
		
	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: fragment, @type: <list>
		self.fragments = kwargs.get("fragments", [{"string":"{{sample}}","optional":False,"attributes":["BOLD"]}])



if __name__ == '__main__':

	print Sentence().create()