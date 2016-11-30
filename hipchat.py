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

	HIPELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	HIPATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}

	@staticmethod
	def HasTag (element = 'A'):
		### @description: public function to confirm HTML tag supported in HipChat
		### @parameter: <element>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# confirm HTML tag is supported 
		return True if HIPHTML.SetStrType(element).upper() in HIPHTML.HIPELEMENTS else False

	@staticmethod
	def HasAttribute (**kwargs):
		### @description: public function to confirm HTML attribute supported in HipChat
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <bool>
		
		# set base element
		# @parameter: <element>, @type: <str>, @default: <str>
		element = HIPHTML.SetStrType(kwargs.get('element')) or 'A'
		# set base attribute
		# @parameter: <node>, @type: <str>, @default: <str>
		attribute = HIPHTML.SetStrType(kwargs.get('attribute')) or 'HREF'
		# confirm attribute is supported
		return True if element.upper() in HIPHTML.HIPELEMENTS and attribute in HIPHTML.HIPATTRIBUTES[element.upper()] else False

	@staticmethod
	def Base (**kwargs):
		### @description: public function to select suitable substitute from allowed HTML tags
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base method
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = HIPHTML.SetStrType(kwargs.get('tag'))
		# set default HTML tag
		tag = tag if HIPHTML.HasTag(tag) else 'SPAN'
		# set HTML
		return { 'HTML_TAG': tag, 'TAG_ATTRIBUTES': HIPHTML.HIPATTRIBUTES[tag] } 



class REST (String):

	###################################################
	### public class to construct REST API endpoint ###
	###################################################

	CONTENT = ['APPLICATION/JSON', 'APPLICATION/X-WWW-FORM-URLENCODED', 'TEXT/HTML', 'TEXT/PLAIN']
	METHOD = ['GET', 'POST', 'PUT', 'HEAD', 'OPTIONS', 'PATCH', 'DELETE']

	@staticmethod
	def Method (arg = 'GET'):
		### @description: public function to confirm HTTP method is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP method support
		return True if REST.SetStrType(arg) in REST.METHOD else False

	@staticmethod
	def Content (arg = 'APPLICATION/JSON'):
		### @description: public function to confirm HTTP content-type header is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP content-type method supported
		return True if REST.SetStrType(arg) in REST.CONTENT else False

	@staticmethod
	def Set (**kwargs):
		### @description: public function to select suitable substitute from allowed HTTP methods
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base method
		# @parameter: <method>, @type: <str>, @default: <None>
		method = kwargs.get('method')
		# set base content
		# @parameter: <content>, @type: <str>, @default: <None>
		content = kwargs.get('content')
		# set HTTP 
		return { 'HTTP_METHOD': method if REST.Method(method) else 'POST', 'CONTENT_TYPE': content if REST.Content(content) else 'APPLICATION/JSON' }


class API (REST):

	ORIGIN = 'EXAMPLE'
	VERSION = 2
	ROOM = '000000'
	DEFAULT_API = "{{sample/api}}"



if __name__ == '__main__':
	
	# format HipChat HTML tag
	print HIPHTML.Base(tag = 'IMG')
	# format HipChat HTTP request 
	print REST.Set(method = 'FAKE')
