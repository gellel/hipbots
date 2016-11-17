#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import regular expressions
import re




class String (object):

	###############################################
	### creates styled strings for system print ###
	###############################################

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
	REG = r"\{\{(?:[\w\s\d]*|[$&\+,\:\;\=\?@#\|'\<\>\.^\*\(\)%!-\/]*)*\}\}"
	EXT = r"^.+\.{1}\w+$"
	FLT = r"{{|}}"

	@staticmethod
	def cconcat (strings = [], character = ""):
		### @description: protected method to concatenate characters by supplied character argument
		### @parameter: strings, @type: <list>
		### @parameter: character, @type: <string>
		### @returns: <string>

		# concatenate list with string
		return str(character).join(filter(None, strings))

	@staticmethod
	def concat (*args):
		### @description: protected method to concatenate arguments by seperated white space
		### @parameter: args, @type: <string>
		### @returns: <string>

		# concatenate arguments joined by white space
		return " ".join(filter(None, args))

	@staticmethod
	def tag (string = "tagged example"):
		### @description: protected method to encapsulate supplied string by highlighting markup
		### @parameter: string, @type: <string>
		### @returns: <string>

		# concatenate string with markup using public method of class
		return String.cconcat(["{{", string, "}}"])

	def create (self):
		### @description: protected method to method for creating beautified strings for class instance
		### @returns: <string>

		# create formatted strings using private method of class instance
		return self.__strs__()

	def __format__ (self, string = "sample", attributes = ["BOLD", "GREEN"]):
		### @description: private method to encapsulate supplied string by attribute strings
		### @parameter: string, @type: <string>
		### @parameter: attributes, @type: <list>
		### @returns: <string>

		# initialise loop to process supplied attributes
		for i in range(0, len(attributes)):
			# attempt to get attribute of class or set default to empty string
			attribute = getattr(self, str(attributes[i]).upper(), "")
			# concatenate string using class public method 
			string = String.cconcat([attribute, string, self.END])
		# return formatted string
		return string
	
	def __test__ (self, **kwargs):
		### @description: private method to processes strings and apply styling to required substrings
		### @parameter: string, @type <string>
		### @parameter: attributes, @type <string>
		### @returns: <string>
		
		# set base string
		string = kwargs.get("string", "{{sample}}")
		# set attempted string match from regular expression
		matches = re.findall(self.REG, kwargs.get("string", string), re.DOTALL)
		# initialise loop to process substring matches
		for i in range(0, len(matches)):
			# set string to exclude prettify selector
			substring = re.sub(self.FLT, "", matches[i])
			# set string to include
			prettified = self.__format__(substring, kwargs.get("attributes", []))
			# refined string to be substituted string
			string = re.sub(substring, prettified, string)
		# return formatted string excluding selectors
		return re.sub(self.FLT, "", string)

	def __sets__ (self, string = "{{sample}}"):
		### @description: private method to set key word arguments for test
		### @parameter: string, @type: <string>
		### @returns: <string>

		# supplies to private method "strs" dictionary if paramater "string" is type dictionary otherwise creates a new dictionary with the keys string and attributes
		return string if type(string) is dict else { 'string': string, 'attributes': self.attributes }

	def __strs__ (self):
		### @description: private method to determine arguments for beautification
		### @returns: <string>

		# supplies to protected method "create" formatted string built from dictionary; selects to use either self.strings if self.string is not a defined value; attributes are chosen from either self.strings internal dictionary or base list for class instance 
		return String.cconcat([self.__test__(string = self.string, attributes = self.attributes)], " ") if bool(self.string) and not bool(self.strings) else String.cconcat([self.__test__(**self.__sets__(string)) for string in self.strings], " ")
	
	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: string, @type: <string>
		### @parameter: strings, @type: <list>
		### @parameter: attributes, @type <list>

		# set string attribute; @default: <None>
		self.string = kwargs.pop("string", None)
		# set strings attribute; @default: <list>
		self.strings = kwargs.pop("strings", [String.tag("prettified"), {"string":String.tag("sample"),"attributes":["BOLD", "DARKCYAN"]}])
		# set attributes attribute; @default: <list>
		self.attributes = kwargs.pop("attributes", ["BOLD", "BLUE"])




if __name__ == '__main__':
	
	# create example beautified string
	print String(strings = ["{{here}} is {{sample}}", {"string":String.tag("text"),"attributes":["BOLD", "CYAN"]}, "with {{highlights}}"], attributes = ["BOLD", "BLUE"]).create()
