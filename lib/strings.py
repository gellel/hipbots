#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import regular expressions
import re


class String (object):

	##################################################################
	### class for formatting strings with colour, weights or joins ###
	##################################################################

	SAMPLE = 'SAMPLE'
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	FILTER = r'\{\{{0,2}[^\{\{]+\}\}{0,2}'
	EXTENSION = r'^.+\.{1}\w+$'
	SYNTAX = r'{{|}}'

	@staticmethod
	def SetPrettyKeys (string = '', attributes = ['BOLD'], tag = False):
		### @description: public function of class, creates dictionary keys and values for use in String.Pretty
		### @return: @type: <dict>

		# set default string for formatting
		# @parameter: <string>, @type: <str>, @default: <str>
		string = String.SetStringType(string) if not type(string) is dict else string
		# set default style attributes for string
		# @parameter: <attributes>, @type: <list>, @default: <list>
		attributes = list(attributes) if not type(attributes) in [list, tuple] else attributes
		# set default tag requirement for string
		# @parameter: <tag>, @type: <bool>, @default: <bool>
		tag = bool(tag)

		# set base dictionary keys and values used in String.Pretty function
		return { 'string': string, 'attributes': attributes, 'tag': tag } if type(string) is str else { key: string[key] for key in string if key in ['string', 'attributes', 'tag'] }

	@staticmethod
	def SetStringType (*args, **kwargs):
		### @description: public function of class, sets supplied arguments to string type before concatenating arguments as a single string
		### @return: @type: <str>

		# set default argument list
		# @parameter: <args>, @type: <tuple>, @default: <tuple>
		args = filter(None, list(args))

		# set default fall back string
		# @parameter: <kwarg:default>, @type: <str>, @type: <str>
		default = kwargs.get('default', '')
		
		# set argument list items to be concatentated string
		args = ' '.join(filter(None, [' '.join(filter(None, list(arg))) if type(arg) in [list, tuple] else str(arg) for arg in args]))
		# set default string if concatenated string contents is evaluated as false
		return args if bool(args) else default

	@staticmethod
	def Cconcat (strings = [], character = ''):
		### @description: public function of class, join lists by supplied string character to create single string
		### @return: @type: <str>

		# set default strings for concatentation
		# @parameter: <strings>, @type: <list>, @default: <list>
		strings = list(strings)
		# set default concatenation string
		# @parameter: <character>, @type: <str>, @default: <str>
		character = String.SetStringType(character)
		
		# join strings in list by supplied character
		return character.join(filter(None, strings))

	@staticmethod
	def Concat (*args):
		### @description: public function of class, joins arguments as single string separated by spaces
		### @return: @type: <str>

		# set default arguments to be string type 
		# @parameter: <args>, @type: <list>, @default: <list>
		args = [String.SetStringType(arg) for arg in list(args)]

		# join argument strings
		return String.Cconcat(args, ' ')

	@staticmethod
	def GetStyles (*args):
		### @description: public function of class, gets dictionary containing supported unix string formatting character codes 
		### @return: @type: <dict>

		# set default arguments to string type for filtering required styles
		# @parameter: <args>, @type: <tuple>, @default: <tuple>
		args = filter(None, [String.SetStringType(arg) for arg in list(args)])

		# set default styles dictionary
		styles = { 'PURPLE': String.PURPLE, 'CYAN': String.CYAN, 'DARKCYAN': String.DARKCYAN, 'BLUE': String.BLUE, 'GREEN': String.GREEN, 'YELLOW': String.YELLOW, 'RED': String.RED, 'BOLD': String.BOLD, 'UNDERLINE': String.UNDERLINE }
		# set styles dictionary exluding items from filtered
		return { key: styles[key] for key in styles if not key in args }

	@staticmethod
	def SetStyle (string = '', attribute = ''):
		### @description: public function of class, sets unix character code formatting to string to create beautified version
		### @return: @type: <str>

		# set default string for beautification
		# @parameter: <string>, @type: <str>, @default: <str>
		string = String.SetStringType(string)
		# set default attribute string
		# @parameter: <attribute>, @type: <str>, @default: <str>
		attribute = String.SetStringType(attribute)

		# join string with attribute style and attribute end to create beautified string
		return String.Cconcat([attribute or String.BOLD, string or String.SetPrettySyntax(String.SAMPLE), String.END])

	@staticmethod
	def SetPrettySyntax (string = ''):
		### @description: public function of class, encapsulates string argument with handlebars syntax to create points for beautified string substitution
		### @return: @type: <str>

		# set default string for syntax application
		# @parameter: <string>, @type: <str>, @default: <str>
		string = String.SetStringType(string)

		# join string using "{{" and "}}" to create formatted text "{{sample text}}"
		return String.Cconcat(['{{', string or String.SAMPLE, '}}'])

	@staticmethod
	def RemovePrettySyntax (string = ''):
		### @description: public function of class, removes beautification syntax from string argument
		### @return: @type: <str>

		# set default string for syntax removal
		# @parameter: <string>, @type: <str>, @default: <str>
		string = String.SetStringType(string)

		# find syntax strings and substitute with empty string
		return re.sub(String.SYNTAX, '', string or String.SAMPLE)

	@staticmethod
	def Pretty (string = '', attributes = ['BOLD'], tag = False):
		### @description: public function of class, creates beautified string
		### @return: @type: <str>

		# set default string
		# @parameter: <string>, @type: <str>, @default: <str>
		string = String.SetStringType(string) or String.SAMPLE
		# set default syntax wrap
		# @parameter: <tag>, @type: <bool>, @default: <bool>
		string = String.SetPrettySyntax(string) if bool(tag) and not re.compile(String.SYNTAX).search(string) else string
		# set default attributes for string
		# @parameter: <attributes>, @type: <list>, @default: <list>
		attributes = list(attributes) if type(attributes) in [list, tuple] else [String.SetStringType(attributes, default = 'BOLD')]
		
		# set default reference for string styles
		styles = String.GetStyles()
		# find strings that contain string style syntax
		strings = re.findall(String.FILTER, string, re.DOTALL)
		# initialise loop to process selected texts
		for i in range(0, len(strings)):
			# find substring for matched item
			substring = re.sub(String.SYNTAX, '', strings[i])
			# set edited string
			edited = substring
			# initialise loop to process styles for string
			for k in range(0, len(attributes)):
				# confirm style attribute
				if attributes[k].upper() in styles:
					# set formatted string
					edited = String.SetStyle(edited, styles[attributes[k].upper()])
			# set original string to include substituted and formatted string reference
			string = re.sub(strings[i], edited, string)
		# find syntax strings and substitute with null
		return re.sub(String.SYNTAX, '', string)




if __name__ == '__main__':

	# format example string
	print String.Pretty("{{Hello world!}} This is a {{Pretty}} {{String!}}")
	