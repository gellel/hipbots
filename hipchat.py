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
		return True if str(element).upper() in HTML.ELEMENTS else False

	@staticmethod
	def Attributes (**kwargs):
		### @description: public function to confirm HTML attribute supported in HipChat
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <bool>
		
		# set base element
		# @parameter: <element>, @type: <str>, @default: <str>
		element = kwargs.get('element', 'A')
		# set base attribute
		# @parameter: <node>, @type: <str>, @default: <str>
		attribute = kwargs.get('attribute', 'HREF')
		# confirm attribute is supported
		return True if str(element).upper() in HTML.ELEMENTS and attribute in HTML.ATTRIBUTES[str(element).upper()] else False



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
	def Default (**kwargs):
		### @description: public function to select suitable substitute from allowed
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base method
		# @parameter: <element>, @type: <str>, @default: <None>
		request = kwargs.get('method')
		# set base content
		# @parameter: <element>, @type: <str>, @default: <None>
		content = kwargs.get('content')
		# set HTTP 
		return { 'HTTP_METHOD': request if REST.Method, 'CONTENT_TYPE': content }




if __name__ == '__main__':
	
	print HTML.Attributes(element = 'SPAN')
