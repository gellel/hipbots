#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from lib.strings import String
### import random sentences
from lib.sentence import Sentence
### import hipchat notifications
from lib.api import Notification
### import http requests
from lib.http import HTTP
### import json
import json
### import system
import sys
### import os
import os
### import regular expressions
import re




class Secrets:

	########################################################
	### public class get JSON client Secrets for HipChat ###
	########################################################

	def __open (self, filename):
		### @description: private function for opening file type as JSON
		### @parameter: <filename>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# attempt to fetch file
		try:
			# assumg file is json and set to dict
			return json.load(open(filename, 'r'))
		# handle exception
		except:
			# set base dictionary
			return { 'auth_token': '1234SamPLEAuTHToKEN', 'auth_subdomain': 'organisation', 'auth_room': '123456' }

	def __file (self, directory, file):
		### @description: private function for create system file string
		### @parameter: <directory>, @type: <str>, @default: <str>
		### @parameter: <file>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# set base directory string
		directory = directory[:-1] if directory[-1:] is '/' else directory
		# set base file string
		file = String.Cconcat([directory, file], '/')
		# attemp to fetch
		return Secrets()._Secrets__open(file)

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




class Robot:

	def message (self):
		return self.__dict__

	def __init__ (self, **kwargs):

		print Notification.Object(**kwargs)
		
		





if __name__ == '__main__':

	print Robot(message = Sentence().randomize()).message()
