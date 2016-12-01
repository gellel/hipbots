#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import random sentences
from sentence import Sentence
### import hipchat messages
from hipchat import Messages
### import json
import json
### import system
import sys
### import os
import os
### import regular expressions
import re




class Secrets:

	def __open (self, filename):
		### @description: private function for opening file type as JSON
		### @parameter: <filename>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# attempt to fetch file
		try:
			return json.loads(open(filename, 'w'))
		# handle exception
		except:
			# set base dictionary
			return { 'auth_token': '1234SamPLEAuTHToKEN', 'auth_domain': 'organisation', 'auth_room': '123456' }

	def __file (self, directory, file):
		### @description: private function for create system file string
		### @parameter: <directory>, @type: <str>, @default: <str>
		### @parameter: <file>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# set base directory string
		directory = directory[:-1] if directory[-1:] is '/' else directory
		# set base file string
		file = String.Cconcat([directory, file], '/')

	@staticmethod
	def Get (**kwargs):
		### @description: public function for importing secret credentials
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base directory
		# @parameter: <directory>, @type: <str>, @default: <str>
		directory = String.SetStrType(kwargs.get('directory')) or os.path.dirname(os.path.realpath('__file__'))
		# set base file secrets name
		# @parameter: <file>, @type: <str>, @default: <str>
		file = String.SetStrType(kwargs.get('file')) or 'secrets.json'
		# fetch file
		return Secrets()._Secrets__file(directory, file)





if __name__ == '__main__':

	print Secrets.Get()

