#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String


class HTML (String):

	##############################################################
	### extended class of strings.String, creates HTML strings ###
	##############################################################
	
	@staticmethod
	def Tag (tag = 'div'):
		### @description: public function of class, creates HTML element string
		### @return: @type: <str>

		# set default HTML element tag string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = HTML.SetStringType(tag).lower()
		
		# encase tag string using HTML element syntax using String.Cconcat
		return HTML.Cconcat(['<', tag, '%s', '>', '%s', '</', tag, '>']) if not tag in ['area', 'default', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'] else String.Cconcat(['<', tag, '%s', '/>', '%s'])

	@staticmethod
	def FormatAttributes (attributes = {}):
		### @description: public function of class, converts dictionary key value pairs into valid HTML attribute string
		### @return: @type: <str>

		# set default attributes dict
		# @parameter: <attributes>, @type: <dict>, @default: <dict>
		attributes = attributes if type(attributes) is dict and bool(attributes) else {}

		# set each dictionary key in attributes to be joined by equals and quotations to format supplied attributes
		return HTML.Cconcat([' ', HTML.Cconcat([HTML.Cconcat([attr, '=', '"', HTML.SetStringType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")]) if bool(attributes) else ''

	@staticmethod
	def SetAttributes (**kwargs):
		### @description: public function of class, applies attribute string to HTML elment string
		### @return: @type: <str>

		# set default HTML element tag string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = HTML.Tag(kwargs.get('tag'))
		# set default HTML element attributes
		# @parameter: <attributes>, @type: <dict>, @default: <dict>
		attributes = HTML.FormatAttributes(kwargs.get('attributes'))
		
		# set attributes for HTML string
		return tag % (attributes, '%s')

	@staticmethod
	def Create (**kwargs):
		### @description: public function of class, creates string HTML structures that include attributes and nesting of other strings
		### @return: @type: <str>

		# set default HTML element tag string
		# @parameter: <kwargs:tag>, @type: <str>, @default: <str>
		tag = HTML.SetStringType(kwargs.get('tag'))
		# set default HTML attributes
		# @parameter: <kwargs:attributes>, @type: <dict>, @default: <dict>
		attributes = kwargs.get('attributes')
		# set default content for internal lambda string
		# @parameter: <kwargs:contents>, @type: <str/function>, @default: <str>
		contents = kwargs.get('contents')

		# apply nesting
		return HTML.SetAttributes(tag = tag, attributes = attributes) % (HTML.SetStringType(contents) if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print HTML.Create(tag = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = HTML.Tag) % ('', HTML.Create(tag = 'p', attributes = { 'id': 'nested' }, contents = '%s') % ('callback!')), '\n', HTML.Create(tag = 'img', attributes = { 'src': 'path/to/img/.gif', 'width': '10px', 'height': '10px' })
	