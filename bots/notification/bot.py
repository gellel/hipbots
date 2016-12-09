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


class Room:

	##########################################################################
	### extended class of hipchat.Support, sends messages to HipChat Rooms ###
	##########################################################################

	@staticmethod
	def SetBaseEndpoint (**kwargs):
		### @description: public function of class, creates base HipChat Rooms API URL string
		### @return: @type: <str>

		# set default HipChat subdomain string
		# @parameter: <kwargs:subdomain>, @type: <str>, @default: <str>
		subdomain = String.SetStringType(kwargs.get('subdomain')) or 'SUBDOMAIN'
		# set default HipChat api version string
		# @parameter: <kwargs:version>, @type: <str>, @default: <str>
		version = re.sub(r'\w*', '', String.SetStringType(kwargs.get('version'))) or '2'
		# set default HipChat room id string
		# @parameter: <kwargs:room>, @type: <str>, @default: <str>
		room = re.sub(r'\w*', '', String.SetStringType(kwargs.get('room'))) or '01010101'
		# set default HipChat api endpoint for rooms
		# @parameter: <kwargs:endpoint>, @type: <str>, @default: <str>
		endpoint = String.SetStringType(kwargs.get('endpoint')) or 'room'

		# construct HipChat Rooms API from arguments and defaults
		return String.Cconcat(['https://', subdomain, '.', 'hipchat', '.', 'com', '/', 'v', version, '/', 'room', '/', room, '/', endpoint])

	@staticmethod
	def SetRequestBody (**kwargs):
		### @description: public function of class, creates HTTP data request object structure
		### @return: @type: <dict>

		# set default colour string for object
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = kwargs.get('colour') if Support.Colour(String.SetStringType(kwargs.get('colour'))) else 'random'
		# set default message for object
		# @parameter: <message>, @type: <str>, @default: <str>
		message = String.SetStringType(kwargs.get('message'))
		# set default notification alert for object
		# @parameter: <notify>, @type: <bool>, @default: <bool>
		notify = str(bool(kwargs.get('notify', False))).lower()
		# set default message format for object
		# @parameter: <format>, @type: <str>, @default: <str>
		format_type = kwargs.get('format') if Support.Format(kwargs.get('format')) else 'html'
		
		# construct HTTP body for HipChat Messenger API
		return { 'color': colour, 'message': message, 'notify': notify, 'message_format': format_type }

	def __init__ (self, **kwargs):
		### @description: class constructor

		# set default HipChat Messenger room string
		# @parameter: <room>, @type: <str>, @default: <None>
		self.room = String.SetStringType(kwargs.get('room', None))
		# set default HipChat Messenger subdomain string
		# @parameter: <subdomain>, @type: <str>, @default: <None>
		self.subdomain = String.SetStringType(kwargs.get('subdomain', None))
		# set default HipChat API token string
		# @parameter: <token>, @type: <str>, @default: <None>
		self.token = String.SetStringType(kwargs.get('token', None))
		# set default HipChat API headers
		# @parameter: <headers>, @type: <dict>, @default: <dict>
		self.headers = kwargs.get('headers', { 'Content-Type': 'application/json' })
		# set default HipChat API body
		# @parameter: <content>, @type: <dict>, @default: <dict>
		self.content = Room.SetRequestBody(**kwargs.get('content', {}))
		# set default HipChat HTTP method type
		# @parameter: <method>, @type: <str>, @default: <str>
		self.method = String.SetStringType(kwargs.get('method', 'POST'))




if __name__ == '__main__':

	# create HipChat messenger bot
	print Room(**dict(json.loads(File.Open(name = 'secrets', extension = 'json', directory = '../../json/oauth/').read()), **{ 'content': { 'message':'hello world!' }}))
	