#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String
### import HTML strings
from strhtml import STRHTML


class HIPHTML (STRHTML):

	########################################################
	### public class for testing support HTML in HipChat ###
	########################################################

	HIP_ELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	HIP_ATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}

	@staticmethod
	def HasTag (tag = 'A'):
		### @description: public function to confirm HTML tag supported in HipChat
		### @parameter: <element>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# confirm HTML tag is supported 
		return True if HIPHTML.SetStrType(tag).upper() in HIPHTML.HIP_ELEMENTS else False

	@staticmethod
	def HasAttribute (**kwargs):
		### @description: public function to confirm HTML attribute supported in HipChat
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <bool>
		
		# set base element
		# @parameter: <element>, @type: <str>, @default: <str>
		tag = HIPHTML.SetStrType(kwargs.get('tag')) or 'A'
		# set base attribute
		# @parameter: <node>, @type: <str>, @default: <str>
		attribute = HIPHTML.SetStrType(kwargs.get('attribute')) or 'HREF'
		# confirm attribute is supported
		return True if tag.upper() in HIPHTML.HIP_ELEMENTS and attribute in HIPHTML.HIP_ATTRIBUTES[tag.upper()] else False

	@staticmethod
	def GetTagAttributes (tag = 'A'):
		### @description: public function to select suitable attributes from allowed HTML tags
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# set base HTML tag
		tag = HIPHTML.SetStrType(tag)
		# set base HTML tag attributes
		attributes = HIPHTML.HIP_ATTRIBUTES[tag.upper()] if tag.upper() in HIPHTML.HIP_ATTRIBUTES else []
		# get attribute information
		return { 'HTML_TAG': tag.upper(), 'TAG_ATTRIBUTES': attributes, 'TAG_SUPPORTED': HIPHTML.HasTag(tag.upper()) } 



class REST (String):

	###################################################
	### public class to construct REST API endpoint ###
	###################################################

	HIP_CONTENT_TYPES = ['APPLICATION/JSON', 'APPLICATION/X-WWW-FORM-URLENCODED', 'TEXT/HTML', 'TEXT/PLAIN']
	HIP_METHOD_TYPES = ['GET', 'POST', 'PUT', 'HEAD', 'OPTIONS', 'PATCH', 'DELETE']
	HIP_DEFAULT_SUBDOMAIN = 'FAKECOMPANY'
	HIP_DEFAULT_VERSION = '2'
	HIP_DEFAULT_ROOM = '0110110'
	HIP_DEFAULT_API = 'PATH/TO/API/ENDPOINT'

	@staticmethod
	def HasMethodType (arg = 'GET'):
		### @description: public function to confirm HTTP method is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP method support
		return True if REST.SetStrType(arg) in REST.HIP_METHOD_TYPES else False

	@staticmethod
	def HasContentType (arg = 'APPLICATION/JSON'):
		### @description: public function to confirm HTTP content-type header is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP content-type method supported
		return True if REST.SetStrType(arg) in REST.HIP_CONTENT_TYPES else False

	@staticmethod
	def GetNotifyURL (**kwargs):
		### @description: public function to configure REST API string
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set subdomain for HipChat client
		# @parameter: <subdomain>, @type: <str>, @default: <None>
		subdomain = REST.SetStrType(kwargs.get('subdomain')) or REST.HIP_DEFAULT_SUBDOMAIN
		# set api version for HipChat API
		# @parameter: <version>, @type: <str>, @default: <None>
		version = REST.SetStrType(kwargs.get('version')) or REST.HIP_DEFAULT_VERSION
		# set room for HipChat API
		# @parameter: <room>, @type: <str>, @default: <None>
		room = REST.SetStrType(kwargs.get('room')) or REST.HIP_DEFAULT_ROOM
		# set base endpoint for HipChat API
		# @parameter: <api>, @type: <str>, @default: <None>
		api = REST.SetStrType(kwargs.get('api')) or  REST.HIP_DEFAULT_API
		# set REST API URL
		return REST.Cconcat([REST.Cconcat([REST.Cconcat(['https://', subdomain]), 'hipchat', 'com'], '.'), '/', REST.Cconcat(['v', version]), '/', 'room', '/', room, '/', api])




if __name__ == '__main__':
	
	# get example attributes for tag
	print HIPHTML.GetTagAttributes('LI')
	# get api endpoint for notifications
	print REST.GetNotifyURL()
