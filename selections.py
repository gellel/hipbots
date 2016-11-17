#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import messages class
from messages import Message



class Select (Message):


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

	print Select().__dict__