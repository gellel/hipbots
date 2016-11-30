#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class HTML:

	#############################################
	### public class for HTML string creation ###
	#############################################
	
	@staticmethod
	def Tag (tag = None):
		### @description: public function to create HTML string tag
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# set base string type
		tag = String.SetStrType(tag, default = 'div').lower()
		# encase tag string
		return String.Cconcat(['<', tag, '%s', '>', '%s', '</', tag, '>'])

	@staticmethod
	def FormatAttributes (attributes = {}):
		### @description: public function to expand dict to HTML attribute syntax
		### @parameter: <attributes>, @type: <dict>, @default: <dict>
		### @return: @type: <str>

		# set base attributes dict
		attributes = attributes if type(attributes) is dict and bool(attributes) else { 'id': None }
		# set each dict key in attributes to be joined by equals and quotations
		return String.Cconcat([' ', String.Cconcat([String.Cconcat([attr, '=', '"', String.SetStrType(attributes[attr]) or 'SAMPLE', '"']) for attr in attributes], " ")])

	@staticmethod
	def SetAttributes (**kwargs):
		### @description: public function to apply attributes to HTML string tag without removing contents lambda
		### @parameter: <dict>, @type: <dict>
		### @return: @type: <str>

		# set base HTML tag
		# @parameter: <tag>, @type: <str>, @default: <None>
		tag = HTML.Tag(kwargs.get('tag'))
		# set base HTML attributes
		# @parameter: <attributes>, @type: <dict>, @default: <None>
		attributes = HTML.FormatAttributes(kwargs.get('attributes'))
		# apply string to first lambda
		return tag % (attributes, '%s')

	@staticmethod
	def Create (**kwargs):
		### @description: public function to create HTML tag, while applying HTML attributes with the option to nest content
		### @parameter: <dict>, @type: <dict>
		### @return: @type: <str>

		# set base HTML tag
		# @parameter: <tag>, @type: <str>, @default: <None>
		# set base HTML attributes
		# @parameter: <attributes>, @type: <dict>, @default: <None>
		# set base content for internal lambda string
		# @parameter: <contents>, @type: <str>, @default: <str>
		contents = kwargs.get('contents')
		# set attributed HTML
		node = HTML.SetAttributes(tag = kwargs.get('tag'), attributes = kwargs.get('attributes'))
		# apply nesting
		return node % (String.SetStrType(contents) if not hasattr(contents, '__call__') else contents())




if __name__ == '__main__':

	# build example HTML
	print HTML.Create(node = 'aside', attributes = { 'id': 'sample', 'class': 'col-xs-3 col-sm-6 col-md-9' }, contents = HTML.Tag) % ('', 'callback!')
