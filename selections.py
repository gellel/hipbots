#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import messages class
from messages import Message



class Select (Message):

	def prompt (self):
		### @description: protected method for asking user to input text that matches defined option
		### @returns: <boolean>

		# request user input from terminal
		return self.__input__(raw_input(super(Select, self).create(super(Message, self).concat(self.message, super(Select, self).cconcat([super(Message, self).cconcat(self.selections, self.option_divider), self.input_divider, " "])))) or None)

	def __input__ (self, prompt = None):
		### @description: private method for confirming receieved input against cases and types
		### @parameter: prompt, @type {string}
		### @returns: <string>

		# confirm type of input is string
		if type(prompt) is str:
			# initialise loop to process defined selections
			for i in range(0, len(self.selections)):
				# confirm match of string against selection
				if self.selections[i].upper() == prompt.upper():
					# return string for result handler
					return self.selections[i]

		# handle incorrect string
		print self.create(self.concat(self.__format__(prompt or "empty", ["BOLD"]), self.failed))		
		# recursively call handler
		return self.prompt()


	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: selections, @type: <list>
		### @parameter: message, @type: <string>
		### @parameter: failed, @type: <string>
		### @parameter: input_divider, @type: <string>
		### @parameter: option_divider, @type: <string>

		# set selections attribute; @default <list>
		self.selections = kwargs.get("selections", ["a", "b", "c"])
		# set prompt attribute; @default: <string>
		self.message = kwargs.get("message", "select one of these options")
		# set failed attribute; @default: <string>
		self.failed = kwargs.get("failed", "did not match required")
		# set input_divider attribute; @default: <string>
		self.input_divider = kwargs.get("input_divider", ":")
		# set option_divider attribute; @default: <string>
		self.option_divider = kwargs.get("option_divider", "/")
		# initialise inherited
		super(Select, self).__init__(name = kwargs.get("name", "system"), seperator = kwargs.get("seperator", ":"), attributes = kwargs.get("attributes", ["BOLD", "UNDERLINE"]))




if __name__ == '__main__':

	# create example selection
	print Select(selections = ["pizza", "chocolate", "coffee"], name = "candy robot").prompt()
	