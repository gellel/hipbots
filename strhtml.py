#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class STRHTML (String):

	#############################################
	### public class for HTML string creation ###
	#############################################

	@staticmethod
	def SetTag (node = None):
		### @description: private function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base node
		node = STRHTML.SetStrType(node) or 'div'
		# encase supplied string with HTML syntax
		return STRHTML.Cconcat(['<', node, '%s', '>', '%s', '</', node, '>'])

	@staticmethod
	def SetAttributes (attributes = None):
		### @description: private function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = attributes or { 'id': None }
		# set each key in attributes to be joined by equals and quotations
		return STRHTML.Cconcat([' ', STRHTML.Cconcat([STRHTML.Cconcat([attr, '=', '"', STRHTML.SetStrType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")])
	
	
	@staticmethod
	def HTML (**kwargs):
		### @description: public function for creating a template HTML string
		### @parameter: <node>, @type: <str>, @default: <None>
		### @parameter: <attributes>, @type: <dict>, @default: <str>
		### @parameter: <contents>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# set base attributes
		attributes = kwargs.get('attributes', '')
		# set base contents
		contents = kwargs.get('contents', '')
		# set base HTML string
		node = STRHTML.SetTag(kwargs.get('node', None)) % (STRHTML.SetAttributes(attributes), '%s')
		# construct
		return node % (contents if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print STRHTML.HTML(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = STRHTML.SetTag) % ('', 'callback!')
	