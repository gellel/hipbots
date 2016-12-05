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

	#################################################
	### class get JSON client Secrets for HipChat ###
	#################################################

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
		### @description: protected function for dispatching bot message to HipChat
		### @return: @type: <instance:requests>

		# dispatch HTTP
		return HTTP(**self.__dict__).HTTP()

	def __URL (self, **kwargs):
		### @description: private function for creating REST API URL for HipChat rooms
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set subdomain string
		# @parameter: <auth_subdomain>, @type: <str>, @default: <str>
		auth_subdomain = String.SetStrType(kwargs.get('auth_subdomain')) or 'github'
		# set room string
		# @parameter: <auth_room>, @type: <str>, @default: <str>
		auth_room = String.SetStrType(kwargs.get('auth_room')) or '000000'
		# set api endpoint string
		# @parameter: <auth_api>, @type: <str>, @default: <str>
		endpoint = String.SetStrType(kwargs.get('endpoint')) or 'notification'
		# set api version string
		# @parameter: <version>, @type: <str>, @default: <str>
		version = String.SetStrType(kwargs.get('version')) or '2'
		# set API URL
		return String.Cconcat([String.Cconcat([String.Cconcat(['https://', auth_subdomain]), 'hipchat', 'com'], '.'), '/', String.Cconcat(['v', version]), '/', 'room', '/', auth_room, '/', endpoint])

	def __auth (self, **kwargs):
		### @description: private function for setting HTTP request to include OAuth2 token in query string
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set query to include
		return { 'auth_token': String.SetStrType(kwargs.get('auth_token')) }

	def __data (self, **kwargs):
		### @description: private function for stringifying data arguments for HTTP request
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set base colour for object
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = kwargs.get('colour')
		# set base colour for object
		# @parameter: <message>, @type: <str>, @default: <str>
		message = kwargs.get('message') 
		# set base colour for object
		# @parameter: <notify>, @type: <bool>, @default: <False>
		notify = kwargs.get('notify')
		# set base colour for object
		# @parameter: <format>, @type: <str>, @default: <str>
		format_type = kwargs.get('format')
		# set base object
		return dict({ '__json__': True }, **Notification.Object(colour = colour, message = message, notify = notify, format = format_type))

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameter: <kwargs>, @type: <dict>

		# set http request url 
		# @parameter: <kwargs>, @type: <dict>
		self.URL = self.__URL(**kwargs)
		# set http request method
		# @parameter: <method>, @type: <str>, @default: <str>
		self.method = kwargs.get('method', 'POST')
		# set http headers 
		# @parameter: <headers>, @type: <dict>, @default: <dict>
		self.headers = kwargs.get('headers', {})
		# set http request query string
		# @parameter: <kwargs>, @type: <dict>
		self.query = self.__auth(auth_token = kwargs.get('auth_token'))
		# set http data request
		# @parameter: <kwargs>, @type: <dict>
		self.data = self.__data(color = kwargs.get('color'), message = kwargs.get('message'), format = kwargs.get('format'), notify = kwargs.get('notify'))

		
		


if __name__ == '__main__':

	# create example HipChat room HTTP messager bot
	print Robot(**dict({ 'message': Sentence(["Guten Tag", "Bonjour", "Hello"], "I am running another", Sentence(["test", "experiment", "program"], ".", separator = ""), "Please", ["ignore", "don't mind"], "me").randomise() }, **Secrets.Get(directory = 'json/oauth/', file = 'client_secrets.json'))).message().content
	