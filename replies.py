#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import messages class
from messages import Message




class Reply (Message):

	##########################################################################################
	### creates prefixed raw input handler to accept user input from one of two conditions ###
	##########################################################################################

	def prompt (self):
		### @description: protected method for asking user to input text that matches defined option
		### @returns: <boolean>

		# request user input from terminal
		return self.__input__(raw_input(super(Reply, self).create(super(Message, self).concat(self.message, super(Reply, self).cconcat([super(Message, self).cconcat([self.confirm, self.reject], self.option_divider), self.input_divider, " "])))) or None)

	def __input__ (self, prompt = None):
		### @description: private method for confirming receieved input against cases and types
		### @parameter: prompt, @type {string}
		### @returns: <boolean>

		# confirm type of input is string
		if type(prompt) is str:
			# confirm match of string confirmed
			if prompt.upper() == self.confirm.upper():
				# return boolean true for result handler
				return True
			# confirm match of string rejected
			elif prompt.upper() == self.reject.upper():
				# return boolean false for result handler
				return False
		# handle incorrect string
		print self.create(self.concat(self.__format__(prompt or "empty", ["BOLD"]), self.failed))		
		# recursively call handler
		return self.prompt()

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: message, @type: <string>
		### @parameter: failed, @type: <string>
		### @parameter: input_divider, @type: <string>
		### @parameter: option_divider, @type: <string>
		### @parameter: confirm, @type: <string>
		### @parameter: reject, @type: <string>

		# set prompt attribute; @default: <string>
		self.message = kwargs.get("message", "shut down mainframe?")
		# set failed attribute; @default: <string>
		self.failed = kwargs.get("failed", "did not match required")
		# set input_divider attribute; @default: <string>
		self.input_divider = kwargs.get("input_divider", ":")
		# set option_divider attribute; @default: <string>
		self.option_divider = kwargs.get("option_divider", "/")
		# set confirm attribute; @default: <string>
		self.confirm = kwargs.get("confirm", "YES")
		# set reject attribute; @default: <string>
		self.reject = kwargs.get("reject", "NO")
		# initialise inherited
		super(Reply, self).__init__(name = kwargs.get("name", "system"), seperator = kwargs.get("seperator", ":"), attributes = kwargs.get("attributes", ["BOLD", "UNDERLINE"]))




if __name__ == '__main__':
	
	# create example reply
	print Reply(message = "delete all files?", name = "evil robot").prompt()
