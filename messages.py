#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings class
from strings import String




class Message (String):

	#################################################
	### creates printed messages prefixed by name ###
	#################################################

	def create (self, string = "hello world!"):
		### @description: protected method to create string prefixed with message name and seperator
		### @parameter: string, @type <string>
		### @returns: <string>

		# use inherited protected method to concatenate supplied string with name prefix
		return self.cconcat([super(Message, self).create(), string], " ")

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: name, @type: <string>
		### @parameter: attributes, @type <list>

		# set name attribute; @default: <string>
		self.name = kwargs.get("name", "system")
		# set attributes attribute; @default: <list>
		self.attributes = kwargs.get("attributes", ["BOLD", "UNDERLINE"])
		# set seperator attribute; @default: <string>
		self.seperator = kwargs.get("seperator", ":")
		# initialise inherited
		super(Message, self).__init__(string = self.cconcat([self.tag(self.name), self.seperator]), strings = False, attributes = self.attributes)




if __name__ == "__main__":

	print dir(Message)

	# create example message
	print Message(name = "robot", seperator = ":").create("bleep! bloop!")
