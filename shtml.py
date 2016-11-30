#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class SHTML (String):

	#############################################
	### public class for HTML string creation ###
	#############################################

	@staticmethod
	def Tag (node = None):
		### @description: private function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base node
		node = SHTML.SetStrType(node) or 'div'
		# encase supplied string with HTML syntax
		return SHTML.Cconcat(['<', node, '%s', '>', '%s', '</', node, '>'])

	@staticmethod
	def Attr (attributes = None):
		### @description: private function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = attributes or { 'id': None }
		# set each key in attributes to be joined by equals and quotations
		return SHTML.Cconcat([' ', SHTML.Cconcat([SHTML.Cconcat([attr, '=', '"', SHTML.SetStrType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")])
	
	
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
		node = SHTML.Tag(kwargs.get('node', None)) % (SHTML.Attr(attributes), '%s')
		# construct
		return node % (contents if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print SHTML.HTML(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = SHTML.Tag) % ('', 'callback!')
	