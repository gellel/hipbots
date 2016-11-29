#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class HTML:

	########################################################
	### public class for testing support HTML in HipChat ###
	########################################################

	ELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	ATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}

	@staticmethod
	def Element (element = 'A'):
		### @description: public function to confirm HTML tag supported in HipChat
		### @parameter: <element>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# confirm HTML tag is supported 
		return True if HTML()._HTML__str(element).upper() in HTML.ELEMENTS else False

	@staticmethod
	def Attributes (**kwargs):
		### @description: public function to confirm HTML attribute supported in HipChat
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <bool>
		
		# set base element
		# @parameter: <element>, @type: <str>, @default: <str>
		element = HTML()._HTML__str(kwargs.get('element', 'A'))
		# set base attribute
		# @parameter: <node>, @type: <str>, @default: <str>
		attribute = HTML()._HTML__str(kwargs.get('attribute', 'HREF'))
		# confirm attribute is supported
		return True if element.upper() in HTML.ELEMENTS and attribute in HTML.ATTRIBUTES[element.upper()] else False

	@staticmethod
	def Base (**kwargs):
		### @description: public function to select suitable substitute from allowed HTML tags
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base method
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = HTML()._HTML__str(kwargs.get('HTML'))
		# set default HTML tag
		tag = tag if HTML.Element(tag) else 'SPAN'
		# set HTML
		return { 'HTML': tag, 'attributes': HTML.ATTRIBUTES[tag] } 

	def __str (self, arg):
		### @description: private function to handle None arguments to string
		### @parameter: <arg>, @type: <*>, @default: <None>
		### @return: @type: <str>

		# set base string
		return str(arg) if type(arg) in [int, float, unicode, str] else ''
	


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
		return True if arg in REST.METHOD else False

	@staticmethod
	def Content (arg = 'APPLICATION/JSON'):
		### @description: public function to confirm HTTP content-type header is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP content-type method supported
		return True if arg in REST.CONTENT else False

	@staticmethod
	def Base (**kwargs):
		### @description: public function to select suitable substitute from allowed HTTP methods
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base method
		# @parameter: <element>, @type: <str>, @default: <None>
		request = kwargs.get('method')
		# set base content
		# @parameter: <element>, @type: <str>, @default: <None>
		content = kwargs.get('content')
		# set HTTP 
		return { 'HTTP_METHOD': request if REST.Method(request) else 'POST', 'CONTENT_TYPE': content if REST.Content(content) else 'APPLICATION/JSON' }


class API (String):

	pass


if __name__ == '__main__':
	
	# format HipChat HTML tag
	print HTML.Base()
	# format HipChat HTTP request 
	print REST.Base()
