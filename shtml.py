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

	ATTRIBUTES = { 'id': 'id', 'class': 'class' }
	TAG = 'div'

	@staticmethod
	def node (node = None):
		### @description: public function for creating basic HTML tag
		### @parameter: <node>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base node
		node = node or HTML.TAG
		# encase supplied string with HTML syntax
		return String.cconcat(['<', node, '%s', '>', '%s', '</', node, '>'])

	@staticmethod
	def attributes (attributes = None):
		### @description: public function for creating attributes string for HTML tags
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = attributes or HTML.ATTRIBUTES
		# set each key in attributes to be joined by equals and quotations
		return String.cconcat([' ', String.cconcat([String.cconcat([str(attr), '=', '"', attributes[attr], '"']) for attr in attributes], " ")])
	
	@staticmethod
	def create (**kwargs):
		### @description: public function for creating a template HTML string
		### @parameter: <node>, @type: <str>, @default: <None>
		### @parameter: <attributes>, @type: <dict>, @default: <None>
		### @parameter: <contents>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# set base attributes
		attributes = kwargs.get('attributes', '')
		# set base node
		node = kwargs.get('node', None)
		# set base contents
		contents = kwargs.get('contents')
		# set HTML string
		node = HTML.node(node) % (HTML.attributes(attributes), '%s')
		# construct
		return node % (contents if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print HTML.create(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = HTML.node) % ('', 'callback!')
	