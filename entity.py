#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import personas
from persona import Persona
### import regular expressions
import re


class Entity (Persona):

	def ask (self, *args, **kwargs):
		### @description: protected method for requesting input from user under a persona
		### @parameter: <args>, @type: <tuple>
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type <str>

		# set formatted request string
		request = self.__format(kwargs.pop("request", "please enter a response:"))
		# set formatted confirmation string
		confirm = self.__format(kwargs.pop("confirm", "is {{%s}} the correct answer?"))
		# set option separator
		separator = kwargs.pop("separator", "/")

		# set base options
		options = [super(Entity, self).Clean(self.__str(string)) for string in args]
		# set args to list
		args = list(args)
		
		print confirm % ('lel')
	
		return options

	def __format (self, request):
		### @description: private method for beautifying request argument
		### @parameter: <request>, @type: <dict/str>, @default: <str>
		### @return: @type <str>

		# set beautiful string
		return super(Entity, self).Pretty(**self.__dict(request))

	def __syntax (self, arg = {}):
		### @description: private method for editing string to contain style tag
		### @parameter: <arg>, @type: <dict>, @default: <dict>
		### @return: @type <dict>

		# confirm arg contains string or set default
		arg = self.__dict(arg) if not 'string' in arg else arg
		# confirm tag required
		if 'tag' in arg and bool(arg['tag']):
			# set style syntax
			arg['string'] = super(Entity, self).Syntax(arg['string'])
			# delete key tag
			arg.pop("tag")
		# set updated arg
		return arg

	def __dict (self, arg = 'sample'):
		### @description: private method for casting argument to string.pretty kwargs
		### @parameter: <arg>, @type: <dict/str>, @default: <str>
		### @return: @type: <dict>

		# cast argument to dict if argument is string otherwise assume dict
		return { 'string': str(arg), 'attributes': ["BOLD"] } if type(arg) is not dict else self.__syntax(arg)

	def __str (self, arg = {'string':'sameple'}):
		### @description: private method for casting argument to string
		### @parameter: <arg>, @type: <dict/str>, @default: <str>
		### @return: @type: <str>

		# case dict to str if else assume str
		return arg['string'] if type(arg) is dict else arg

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set call to inherited persona
		super(Entity, self).__init__(**kwargs)




if __name__ == '__main__':

	# entity named request
	print Entity(**Persona().__dict__).ask("a", {"string":"b","tag":True})
	