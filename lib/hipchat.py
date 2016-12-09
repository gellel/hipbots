#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import html strings
from html import HTML
### import pseudo random 
import random


class Support (HTML):

	###############################################################################
	### extended class of html.HTML, manages requirements for HipChat Messenger ###
	###############################################################################

	@staticmethod
	def HasHTML (tag = 'span'):
		### @description: public function of class, confirms supplied HTML element string is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = Support.SetStringType(tag).lower()

		# confirm HTML element tag is supported by HipChat Messenger client
		return True if tag in Support.GetHTML() else False

	@staticmethod
	def HasCSS (style = 'color'):
		### @description: public function of class, confirms if CSS style property is supported in HipChat Messenger
		### @return: @type: <bool>

		# set default CSS property string
		# @parameter: <style>, @type: <str>, @default: <str>
		style = Support.SetStringType(style).lower()

		# confirm CSS style is supported by HipChat Messenger client
		return True if style in Support.GetCSS() else False

	@staticmethod
	def HasAttribute (tag = 'a', attribute = 'href'):
		### @description: public function of class, confirms HTML attribute is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = Support.SetStringType(tag)
		# set default HTML element attribute string
		# @parameter: <attribute>, @type: <str>, @default: <str>
		attribute = Support.SetStringType(attribute)

		# confirm HTML element and tag attribute is supported by HipChat Messenger client
		return True if Support.HasHTML(tag) and attribute in Support.GetHTML()[tag] else False
	
	@staticmethod
	def HasColour (colour = 'red'):
		### @description: public function of class, confirms colour string is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default colour string
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = Support.SetStringType(colour)

		# confirm supplied colour string is supported by HipChat Messenger client
		return True if colour.lower() in Support.GetColours() else False

	@staticmethod
	def HasFormat (datatype = 'html'):
		### @description: public function of class, confirms HipChat data format supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default message format type
		# @parameter: <datatype>, @type: <str>, @default: <str>
		datatype = Support.SetStringType(datatype).lower()

		# confirm message data type is supported by HipChat Messenger client
		return True if datatype in Support.GetFormats() else False

	@staticmethod
	def GetHTML ():
		### @description: public function of class, sets dictionary of supported HTML tags in HipChat Messenger client
		### @return: @type: <dict>

		# create dictionary containing supported HTML tags and attributes
		return { 'a':['style', 'href', 'rel', 'data-target', 'data-target-options'], 'b':[], 'i':[], 'strong':[], 'em':[], 'br':[], 'img':['style', 'src', 'alt', 'width', 'height', 'align'], 'pre':[], 'code':[], 'span':['style'], 'ol':[], 'ul':[], 'li':[], 'table':[], 'thead':[], 'tbody':[], 'tr':['valign'], 'th':['colspan', 'rowspan', 'valign'], 'td':['colspan', 'rowspan', 'valign'] }

	@staticmethod
	def GetAttributes (tag = None):
		### @description: public function of class, gets attributes of supported HTML tag in HipChat Messenger client
		### @return: @type: <list>

		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <None>
		tag = Support.SetStringType(tag)

		# set default supported HTML elements
		elements = Support.GetHTML()
		# find attributes for supported HTML otherwise use set empty list
		return elements[a] if Support.HasHTML(a) else []

	@staticmethod
	def GetCSS ():
		### @description: public function of class, sets list of supported CSS attributes in HipChat Messenger client
		### @return: @type: <list>

		# create list containing supported CSS style property attributes in HipChat Messenger client
		return ['font-weight', 'color', 'text-decoration', 'height', 'width']

	@staticmethod
	def GetColours ():
		### @description: public function of class, sets list of supported colours in HipChat Messenger client
		### @return: @type: <list>

		# create list containing supported colour strings in HipChat Messenger
		return ['yellow', 'green', 'red', 'purple', 'gray', 'random']

	@staticmethod
	def GetFormats ():
		### @description: public function of class, sets list of supported message formats in HipChat Messenger client
		### @return: @type: <list>

		# create list containing supported data formated in HipChat Messenger client
		return ['html', 'text']

	@staticmethod
	def SetHTML (tag = None, default = None):
		### @description: public function of class, sets default HTML element string if supplied not supported 
		### @return: @type: <str>

		# set default supported HTML elements
		elements = Support.GetHTML()
		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <None>
		tag = Support.SetStringType(tag)
		# set default supported HTML string
		# @parameter: <default>, @type: <str>, @default: <None>
		default = Support.SetStringType(default) if default in elements else 'span'

		# set default HTML element string
		return tag if tag in elements else default

	@staticmethod
	def SetAttribute (tag = None, attribute = None):
		### @description: public function of class, sets supported attribute string for HTML tag if not supported
		### @return: @type: <str>

		# set default supported HTML elements
		elements = Support.GetHTML()
		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <None>
		tag = Support.SetHTML(tag)
		# set default HTML attribute string
		# @parameter: <default>, @type: <str>, @default: <None>
		attribute = Support.SetStringType(attribute)

		# set default HTML element attribute string
		return attribute if Support.HasAttribute(tag, attribute) else ''

	@staticmethod
	def SetColour (colour = None, default = None):
		### @description: public function of class, sets default colour string if not supported 
		### @return: @type: <str>

		# set default supported colours elements
		colours = Support.GetColours()
		# set default colour string
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = Support.SetStringType(colour)
		# set default supported colour string
		# @parameter: <default>, @type: <str>, @default: <None>
		default = Support.SetStringType(default) if default in colours else 'random'

		# set default colour string
		return colour if colour in colours else default

	@staticmethod
	def SetFormat (datatype = None, default = None):
		### @description: public function of class, sets default data format string if not supported 
		### @return: @type: <str>

		# set default supported data formats
		formats = Support.GetFormats()
		# set default format string
		# @parameter: <datatype>, @type: <str>, @default: <str>
		datatype = Support.SetStringType(datatype)
		# set default supported format string
		# @parameter: <default>, @type: <str>, @default: <None>
		default = Support.SetStringType(default) if default in formats else 'html'

		# set default format string
		return datatype if datatype in formats else default


if __name__ == '__main__':

	# fetch supported HipChat HTML
	print Support.SetHTML()
	