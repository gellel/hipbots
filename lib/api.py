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



class Notification (HTML):

	###################################################################
	### public function for creating HipChat REST API notifications ###
	###################################################################

	def __HTML (self, tag = 'span'):
		### @description: private function for confirming HTML tag supported
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# get base HTML tags and confirm tag exists
		return True if String.SetStrType(tag).lower() in Notification.GetHTML() else False

	def __CSS (self, style = 'color'):
		### @description: private function for confirming CSS attribute supported
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# get base CSS styles and confirm style exists
		return True if String.SetStrType(style).lower() in Notification.GetCSS() else False

	def __attribute (self, tag = 'a', attribute = 'href'):
		### @description: private function for confirming HTML attribute supported for tag
		### @parameter: <tag>, @type: <str>, @default: <str>
		### @parameter: <attribute>, @type: <str>, @default: <str>
		### @return: @type: <bool>
		
		# get base HTML tag and confirm as well as test if attribute exists
		return True if Notification()._Notification__HTML(tag) and String.SetStrType(attribute) in Notification.GetHTML()[tag] else False
	
	def __colour (self, colour = 'red'):
		### @description: private function for confirming HipChat colour supported
		### @parameter: <colour>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# get base HipChat colours and confirm colour exists
		return True if String.SetStrType(colour).lower() in Notification.GetColours() else False

	def __format (self, format_type = 'html'):
		### @description: private function for confirming HipChat format supported
		### @parameter: <format_type>, @type: <str>, @default: <str>
		### @return: @type: <bool>

		# get base HipChat format types and confirm format exists
		return True if String.SetStrType(format_type).lower() in Notification.GetFormats() else False

	@staticmethod
	def GetHTML ():
		### @description: public function for getting dict of supported HTML tags in HipChat messages
		### @return: @type: <dict>

		# get supported HTML tags 
		return { 'a':['style', 'href', 'rel', 'data-target', 'data-target-options'], 'b':[], 'i':[], 'strong':[], 'em':[], 'br':[], 'img':['style', 'src', 'alt', 'width', 'height', 'align'], 'pre':[], 'code':[], 'span':['style'], 'ol':[], 'ul':[], 'li':[], 'table':[], 'thead':[], 'tbody':[], 'tr':['valign'], 'th':['colspan', 'rowspan', 'valign'], 'td':['colspan', 'rowspan', 'valign'] }

	@staticmethod
	def GetCSS ():
		### @description: public function for getting list of supported CSS attributes in HipChat messages
		### @return: @type: <list>

		# get supported CSS attributes
		return ['font-weight', 'color', 'text-decoration', 'height', 'width']

	@staticmethod
	def GetColours ():
		### @description: public function for getting list of supported colour attributes in HipChat messages
		### @return: @type: <list>

		# get supported HipChat message colours
		return ['yellow', 'green', 'red', 'purple', 'gray', 'random']

	@staticmethod
	def GetFormats ():
		### @description: public function for getting list of supported message formats in HipChat messages
		### @return: @type: <list>

		# get supported HipChat message formats
		return ['html', 'text']

	@staticmethod
	def Object (**kwargs):
		### @description: public function for getting base dict for REST API
		### @return: @type: <dict>

		# set base colour for object
		# @parameter: <colour>, @type: <str>, @default: <str>
		colour = kwargs.get('colour') if Notification()._Notification__colour(kwargs.get('colour')) else 'random'
		# set base message for object
		# @parameter: <message>, @type: <str>, @default: <str>
		message = String.SetStrType(kwargs.get('message'))
		# set base notification alert for object
		# @parameter: <notify>, @type: <bool>, @default: <False>
		notify = str(bool(kwargs.get('notify', False))).lower()
		# set base message format for object
		# @parameter: <format>, @type: <str>, @default: <str>
		format_type = kwargs.get('format') if Notification()._Notification__format(kwargs.get('format')) else 'html'
		# get supported HipChat message formats
		return { 'color': colour, 'message': message, 'notify': notify, 'message_format': format_type }




if __name__ == '__main__':

	# create example REST object for messages API
	print Notification.Object()
