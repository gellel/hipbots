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
from lib.api import REST
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


class File:

	###########################################
	### class for finding and opening files ###
	###########################################

	@staticmethod
	def Directory ():
		### @description: public function of class, create string to local directory
		### @return: @type: <str>

		# create file path string
		return os.path.dirname(os.path.realpath('__file__'))

	@staticmethod
	def Exists (file = ''):
		### @description: public function of class, confirms file exists on drive
		### @return: @type: <bool>

		# set default file string
		# @parameter: <file>, @type: <str>, @default: <str>
		file = String.SetStringType(file)

		# confirm file exists on drive
		return True if os.path.exists(file) or os.path.exists(String.Cconcat([File.Directory(), '/', file])) else False

	@staticmethod
	def Open (file = '', method = 'r'):
		### @description: public function of class, reads files on drive
		### @return: @type: <dict>

		# set default file string
		# @parameter: <file>, @type: <str>, @default: <str>
		file = String.SetStringType(file) or None
		# set default file read status
		# @parameter: <method>, @type: <str>, @default: <str>
		method = String.SetStringType(method)

		# attempt to fetch file from drive
		return open(file, method) if bool(file) and File.Exists(file) else None



class Robot:

	#####################################################################
	### class to construct and send HipChat messages from defined bot ###
	#####################################################################

	def message (self):
		### @description: protected function for dispatching bot message to HipChat
		### @return: @type: <instance:requests>

		# dispatch HTTP
		return HTTP(**self.__dict__).HTTP()

	def __url (self, **kwargs):
		### @description: private function for creating REST API URL for HipChat rooms
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set subdomain string
		# @parameter: <auth_subdomain>, @type: <str>, @default: <str>
		auth_subdomain = String.SetStringType(kwargs.get('auth_subdomain')) or 'github'
		# set room string
		# @parameter: <auth_room>, @type: <str>, @default: <str>
		auth_room = String.SetStringType(kwargs.get('auth_room')) or '000000'
		# set api endpoint string
		# @parameter: <auth_api>, @type: <str>, @default: <str>
		endpoint = String.SetStringType(kwargs.get('endpoint')) or 'notification'
		# set api version string
		# @parameter: <version>, @type: <str>, @default: <str>
		version = String.SetStringType(kwargs.get('version')) or '2'
		# set API URL
		return String.Cconcat([String.Cconcat([String.Cconcat(['https://', auth_subdomain]), 'hipchat', 'com'], '.'), '/', String.Cconcat(['v', version]), '/', 'room', '/', auth_room, '/', endpoint])

	def __auth (self, **kwargs):
		### @description: private function for setting HTTP request to include OAuth2 token in query string
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set query to include
		return { 'auth_token': String.SetStringType(kwargs.get('auth_token')) }

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
		self.URL = self.__url(**kwargs)
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

	print File.Open("json/message_bot/chat.json")

	#print json.load(open(String.Cconcat([os.path.dirname(os.path.realpath('__file__')), '/', 'json/message_bot/chat.json']), 'r'))

	#print JSON.Get(file = "json/message_bot/chat.json")

	#print Sentence(*JSON.Get(file = "dialogue.json", directory = "json/message_bot")[str(sys.argv[1:][0]) or "default"]).randomise()
	

	# create example HipChat room HTTP messager bot
	#print Robot(**dict({ 'message': Sentence(*JSON.Get(file = "dialogue.json", directory = "json/message_bot")[sys.argv[1:] or "greeting"]).randomise(), "notify": True }, **JSON.Get(directory = 'json/oauth/', file = 'client_secrets.json'))).message().content
