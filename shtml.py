#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class HTML (String):

	#############################################
	### public class for HTML string creation ###
	#############################################

	@staticmethod
	def Node (node = None):
		### @description: public function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base node
		node = node if bool(HTML.SetStrType(node)) else 'div'
		# encase supplied string with HTML syntax
		return HTML.cconcat(['<', node, '%s', '>', '%s', '</', node, '>'])

	@staticmethod
	def Attributes (attributes = None):
		### @description: public function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = attributes or { 'id': None }
		# set each key in attributes to be joined by equals and quotations
		return HTML.cconcat([' ', HTML.cconcat([HTML.cconcat([str(attr), '=', '"', HTML.SetStrType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")])
	
	@staticmethod
	def Create (**kwargs):
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
		node = HTML.Node(kwargs.get('node', None)) % (HTML.Attributes(attributes), '%s')
		# construct
		return node % (contents if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print HTML.Create(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = HTML.Node) % ('', 'callback!')
	