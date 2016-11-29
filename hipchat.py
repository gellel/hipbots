#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################

class HTML:

	########################################################
	### public class for testing support HTML in HipChat ###
	########################################################

	ELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	ATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}

	@staticmethod
	def element (element = 'A'):
		### @description: public function confirms HTML tag supported in HipChat
		### @parameter: <element>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# confirm tag is supported 
		return True if str(element).upper() in HTML.ELEMENTS else False

	@staticmethod
	def attributes (**kwargs):
		### @description: public function confirms HTML attribute supported in HipChat
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



class REST:

	###################################################
	### public class to construct REST API endpoint ###
	###################################################

	@staticmethod
	def default (**kwargs):
		### @description: public function to select suitable substitute from allowed
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base request
		request = kwargs.get('request', None)
		# confirm request 






if __name__ == '__main__':
	
	print HTML.attributes(element = 'SPAN')
