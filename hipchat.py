#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import HTML strings
from strhtml import STRHTML


class HIPHTML (STRHTML):

	########################################################
	### public class for testing support HTML in HipChat ###
	########################################################

	ELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	ATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}

	@staticmethod
	def HasTag (tag = 'A'):
		### @description: public function to confirm HTML tag supported in HipChat
		### @parameter: <element>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# confirm HTML tag is supported 
		return True if HIPHTML.SetStrType(tag).upper() in HIPHTML.ELEMENTS else False

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
		return True if tag.upper() in HIPHTML.ELEMENTS and attribute in HIPHTML.ATTRIBUTES[tag.upper()] else False

	@staticmethod
	def GetTagAttributes (tag = 'A'):
		### @description: public function to select suitable attributes from allowed HTML tags
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @return: @type: <dict>

		# set base HTML tag
		tag = HIPHTML.SetStrType(tag)
		# set base HTML tag attributes
		attributes = HIPHTML.ATTRIBUTES[tag.upper()] if tag.upper() in HIPHTML.ATTRIBUTES else []
		# get attribute information
		return { 'HTML_ELEMENT': tag.upper(), 'HTML_ATTRIBUTES': attributes, 'HTML_SUPPORTED': HIPHTML.HasTag(tag.upper()) } 


class REST (String):

	###################################################
	### public class to construct REST API endpoint ###
	###################################################

	CONTENT_HEADERS = ['APPLICATION/JSON', 'APPLICATION/X-WWW-FORM-URLENCODED', 'TEXT/HTML', 'TEXT/PLAIN']
	METHOD_TYPES = ['GET', 'POST', 'PUT', 'HEAD', 'OPTIONS', 'PATCH', 'DELETE']

	@staticmethod
	def HasContentType (arg = 'APPLICATION/JSON'):
		### @description: public function to confirm HTTP content-type header is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP content-type method supported
		return True if REST.SetStrType(arg) in REST.CONTENT_HEADERS else False

	@staticmethod
	def HasMethodType (arg = 'GET'):
		### @description: public function to confirm HTTP method is supported
		### @parameter: <arg>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# confirm HTTP method support
		return True if REST.SetStrType(arg) in REST.METHOD_TYPES else False


class Message (HIPHTML):

	##################################################
	### public class to construct HipChat messages ###
	##################################################

	COLOURS = ['YELLOW', 'GREEN', 'RED', 'PURPLE', 'GRAY', 'RANDOM']

	@staticmethod
	def HasColour (colour = 'YELLOW'):
		pass

	@staticmethod
	def HasFormat (format = 'HTML'):
		pass

	def __init__ (self, **kwargs):
		pass




if __name__ == '__main__':
	
	# get example attributes for tag
	print dir(Message)
