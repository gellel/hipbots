#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import json
import json
### import system
import sys
### import os
import os
### import regular expressions
import re
### set root folder path
sys.path.append('../../')
### import pretty strings
from lib.strings import String
### import random sentences
from lib.sentence import Sentence
### import HipChat REST
from lib.hipchat import Support
### import http requests
from lib.http import HTTP
### import files
from lib.file import File


class Room (Support):

	##########################################################################
	### extended class of hipchat.Support, sends messages to HipChat Rooms ###
	##########################################################################

	@staticmethod
	def SetRequestEndpoint (**kwargs):
		### @description: public function of class, creates base HipChat Rooms API URL string
		### @return: @type: <str>

		# set default HipChat subdomain string
		# @parameter: <kwargs:subdomain>, @type: <str>, @default: <str>
		subdomain = String.SetStringType(kwargs.get('subdomain')) or 'SUBDOMAIN'
		# set default HipChat api version string
		# @parameter: <kwargs:version>, @type: <str>, @default: <str>
		version = re.sub(r'\D', '', String.SetStringType(kwargs.get('version'))) or '2'
		# set default HipChat room id string
		# @parameter: <kwargs:room>, @type: <str>, @default: <str>
		room = re.sub(r'\D', '', String.SetStringType(kwargs.get('room'))) or '01010101'
		# set default HipChat api endpoint for rooms
		# @parameter: <kwargs:endpoint>, @type: <str>, @default: <str>
		endpoint = String.SetStringType(kwargs.get('endpoint')) or 'room'

		# construct HipChat Rooms API from arguments and defaults
		return String.Cconcat(['https://', subdomain, '.', 'hipchat', '.', 'com', '/', 'v', version, '/', 'room', '/', room, '/', endpoint])

	@staticmethod
	def SetRequestBody (**kwargs):
		### @description: public function of class, creates HTTP data request object structure
		### @return: @type: <dict>

		# set default HipChat notification colour string
		# @parameter: <kwargs:colour>, @type: <str>, @default: <str>
		colour = String.SetStringType(kwargs.get('colour'))
		# set default HipChat notification message contents
		# @parameter: <kwargs:message>, @type: <str>, @default: <str>
		message = String.SetStringType(kwargs.get('message'))
		# set default HipChat notification alert string
		# @parameter: <kwargs:notify>, @type: <str>, @default: <str>
		notify = String.SetStringType(kwargs.get('notify'))
		# set default HipChat notification data format type
		# @parameter: <kwargs:format>, @type: <str>, @default: <str>
		datatype = String.SetStringType(kwargs.get('format'))

		# construct HTTP body for HipChat Messenger API
		return { 'color': Room.SetColour(colour = colour), 'message': message, 'notify': str(bool(notify)).lower(), 'message_format': Room.SetFormat(datatype = datatype) }

	def message (self):
		### @description: protected function of class, disptaches HTTP request to HipChat Messenger
		### @return: @type: <instance:requests>

		# set base URL string
		URL = Room.SetRequestEndpoint(subdomain = self.subdomain, version = self.version, room = self.room, endpoint = self.endpoint)
		# set base request object 
		data = Room.SetRequestBody(**self.content)

		# set request requirements and dispatch
		return HTTP(URL = URL, method = self.method, headers = self.headers, query = { 'auth_token': self.token }, data = dict(data, **{ '__json__': True})).HTTP()

	def __init__ (self, **kwargs):
		### @description: class constructor

		# set default HipChat Messenger subdomain string
		# @parameter: <kwargs:subdomain>, @type: <str>, @default: <None>
		self.subdomain = String.SetStringType(kwargs.get('subdomain', None))
		# set default HipChat Messenger api version string
		# @parameter: <version>, @type: <str>, @default: <None>
		self.version = String.SetStringType(kwargs.get('version', None))
		# set default HipChat Messenger room id string
		# @parameter: <room>, @type: <str>, @default: <None>
		self.room = String.SetStringType(kwargs.get('room', None))
		# set default HipChat Messenger api endpoint string
		# @parameter: <room>, @type: <str>, @default: <None>
		self.endpoint = String.SetStringType(kwargs.get('endpoint', 'notification'))
		# set default HipChat Messenger api token string
		# @parameter: <token>, @type: <str>, @default: <None>
		self.token = String.SetStringType(kwargs.get('token', None))
		# set default HipChat HTTP method type
		# @parameter: <method>, @type: <str>, @default: <str>
		self.method = String.SetStringType(kwargs.get('method', 'POST'))
		# set default HipChat API headers
		# @parameter: <headers>, @type: <dict>, @default: <dict>
		self.headers = kwargs.get('headers', { 'Content-Type': 'application/json' })
		# set default HipChat API body
		# @parameter: <content>, @type: <dict>, @default: <dict>
		self.content = Room.SetRequestBody(**kwargs.get('content', {}))
		



if __name__ == '__main__':

	# create HipChat messenger bot
	print Room(**dict(json.loads(File.Open(name = 'secrets', extension = 'json', directory = '../../json/oauth/').read()), **{ 'content': { 'message':'hello world!' }})).message()
	