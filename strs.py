#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import regular expressions
import re


class String (object):

	##########################################
	### public class for string formatting ###
	##########################################

	SAMPLE = "SAMPLE"
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
	FILTER = r"\{\{{0,2}[^\{\{]+\}\}{0,2}"
	EXTENSION = r"^.+\.{1}\w+$"
	SYNTAX = r"{{|}}"

	@staticmethod
	def cconcat (strings = [], character = ""):
		### @description: public function for concatenating a list of strings by supplied character
		### @parameter: <strings>, @type: <list>, @default: <list>
		### @parameter: <character>, @type: <str>, @default: <str>
		### @return: @type: <list>

		# join strings using converted character reference
		return str(character).join(filter(None, strings))

	@staticmethod
	def concat (*strings):
		### @description: public function for concatenating multiple string arguments by empty space
		### @parameter: <strings>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# join string using whitespace
		return String.cconcat(list(strings), " ")

	@staticmethod
	def GetStyles ():
		### @description: public function for getting dict of terminal colours and formatting
		### @return: @type <dict>

		# get style references from defined static attributes
		return { 'PURPLE': String.PURPLE, 'CYAN': String.CYAN, 'DARKCYAN': String.DARKCYAN, 'BLUE': String.BLUE, 'GREEN': String.GREEN, 'YELLOW': String.YELLOW, 'RED': String.RED, 'BOLD': String.BOLD, 'UNDERLINE': String.UNDERLINE }

	@staticmethod
	def SetStyle (string = None, attribute = None):
		### @description: public function for setting style formatting around string for terminal ouput
		### @parameter: <string>, @type: <str>, @default: <None>
		### @parameter: <attribute>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# join string with attribute and attribute end
		return String.cconcat([attribute or String.BOLD, string or String.Syntax(String.SAMPLE), String.END])

	@staticmethod
	def Syntax (string = None):
		### @description: public function for setting syntax for strings
		### @parameter: <string>, @type: <str>, @default: <None>
		### @return: @type: <str>

		# join string using "{{" and "}}" to create "{{sample text}}"
		return String.cconcat(["{{", string or String.SAMPLE, "}}"])

	@staticmethod
	def Pretty (string = None, attributes = None):
		### @description: public method for setting terminal style to required text
		### @parameter: <string>, @type: <str>, @default: <None>
		### @parameter: <attributes>, @type: <list>, @default: <None>
		### @return: @type <str>

		# set base string
		string = string if type(string) is str and bool(string) else String.Syntax(String.SAMPLE)
		# set base attributes
		attributes = attributes if type(attributes) is list else ["BOLD"]
		# set base reference to styles
		styles = String.GetStyles()
		# find strings containing string style syntax 
		strings = re.findall(String.FILTER, string, re.DOTALL)
		# initialise loop to process selected texts
		for i in range(0, len(strings)):
			# find substring for matched item
			substring = re.sub(String.SYNTAX, "", strings[i])
			# set edited string
			edited = substring
			# initialise loop to process styles for string
			for k in range(0, len(attributes)):
				# confirm style attribute
				if attributes[k].upper() in styles:
					# set formatted string
					edited = String.SetStyle(edited, styles[attributes[k].upper()])
			# set original string to include substituted and formatted string reference
			string = re.sub(substring, edited, string)
		# find syntax strings and substitute with null
		return re.sub(r'{{|}}', "", string)



if __name__ == '__main__':

	# format example string
	print String.Pretty()