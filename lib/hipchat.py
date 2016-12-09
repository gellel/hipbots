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
	def HTML (tag = 'span'):
		### @description: public function of class, confirms supplied HTML element string is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = Support.SetStringType(tag).lower()

		# confirm HTML element tag is supported by HipChat Messenger client
		return True if tag in Support.GetHTML() else False

	@staticmethod
	def CSS (style = 'color'):
		### @description: public function of class, confirms if CSS style property is supported in HipChat Messenger
		### @return: @type: <bool>

		# set default CSS property string
		# @parameter: <style>, @type: <str>, @default: <str>
		style = Support.SetStringType(style).lower()

		# confirm CSS style is supported by HipChat Messenger client
		return True if style in Support.GetCSS() else False

	@staticmethod
	def Attribute (tag = 'a', attribute = 'href'):
		### @description: public function of class, confirms HTML attribute is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default HTML element string
		# @parameter: <tag>, @type: <str>, @default: <str>
		tag = Support.SetStringType(tag)
		# set default HTML element attribute string
		# @parameter: <attribute>, @type: <str>, @default: <str>
		attribute = Support.SetStringType(attribute)

		# confirm HTML element and tag attribute is supported by HipChat Messenger client
		return True if Support.HTML(tag) and attribute in Support.GetHTML()[tag] else False
	
	@staticmethod
	def Colour (colour = 'red'):
		### @description: public function of class, confirms colour string is supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default colour string
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = Support.SetStringType(colour)

		# confirm supplied colour string is supported by HipChat Messenger client
		return True if Support.SetStringType(colour).lower() in Support.GetColours() else False

	@staticmethod
	def Format (format_type = 'html'):
		### @description: public function of class, confirms HipChat data format supported in HipChat Messenger client
		### @return: @type: <bool>

		# set default message format type
		# @parameter: <format_type>, @type: <str>, @default: <str>
		format_type = Support.SetStringType(format_type).lower()

		# confirm message data type is supported by HipChat Messenger client
		return True if format_type in Support.GetFormats() else False

	@staticmethod
	def GetHTML ():
		### @description: public function of class, sets dictionary of supported HTML tags in HipChat Messenger client
		### @return: @type: <dict>

		# create dictionary containing supported HTML tags and attributes
		return { 'a':['style', 'href', 'rel', 'data-target', 'data-target-options'], 'b':[], 'i':[], 'strong':[], 'em':[], 'br':[], 'img':['style', 'src', 'alt', 'width', 'height', 'align'], 'pre':[], 'code':[], 'span':['style'], 'ol':[], 'ul':[], 'li':[], 'table':[], 'thead':[], 'tbody':[], 'tr':['valign'], 'th':['colspan', 'rowspan', 'valign'], 'td':['colspan', 'rowspan', 'valign'] }

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




if __name__ == '__main__':

	# fetch supported HipChat HTML
	print Support.GetHTML()
	