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

	def __node (self, node = None):
		### @description: private function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base node
		node = HTML.SetStrType(node) or 'div'
		# encase supplied string with HTML syntax
		return HTML.Cconcat(['<', node, '%s', '>', '%s', '</', node, '>'])

	def __attributes (self, attributes = None):
		### @description: private function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = attributes or { 'id': None }
		# set each key in attributes to be joined by equals and quotations
		return HTML.Cconcat([' ', HTML.Cconcat([HTML.Cconcat([attr, '=', '"', HTML.SetStrType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")])
	
	@staticmethod
	def GetNodeString (node = None):
		### @description: public function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# create HTML element
		return HTML()._HTML__node(node)

	@staticmethod
	def GetAttributeString (attributes = None):
		### @description: private function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# create HTML element
		return HTML()._HTML__attributes(attributes)

	@staticmethod
	def String (**kwargs):
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
		node = HTML()._HTML__node(kwargs.get('node', None)) % (HTML()._HTML__attributes(attributes), '%s')
		# construct
		return node % (contents if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print HTML.String(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = HTML.GetNodeString) % ('', 'callback!')
	