#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import personas
from persona import Persona


class Entity (Persona):

	####################################################################
	### Persona class extension to handle user arguments with prefix ###
	####################################################################

	def ask (self, *args, **kwargs):
		### @description: protected method for requesting input from user under a persona
		### @parameter: <args>, @type: <tuple>
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set formatted request string
		request = self.__format(kwargs.pop('request', 'please enter your selection'))
		# set formatted confirmation string
		confirm = self.__format(kwargs.pop('confirm', 'is {{%s}} the correct answer?'))
		# set formatted reject string
		reject = self.__format(kwargs.pop('reject', '{{%s}} is not an accepted option'))
		# set option separator
		separator = self.__format(kwargs.pop('separator', '/'))
		# set input divider 
		divider = self.__format(kwargs.pop('divider', ':'))
		# set null string
		null = self.__format(kwargs.pop('null', 'empty'))
		# set args to list
		args = list(args)
		# set accept string
		accept = kwargs.get('accept', 'YES')
		# set decline string
		decline = kwargs.get('decline', 'NO')
		# set confirmations to list
		confirms = [accept, decline]
		# set clean string options
		selection_options = [super(Entity, self).Clean(self.__str(string)) for string in args]
		# set beautiful string options
		selection_beautiful = [super(Entity, self).Pretty(**self.__dict(option)) for option in args]
		# set confirmation string options
		confirmation_options = [super(Entity, self).Clean(self.__str(string)) for string in confirms]
		# set confirmation string options
		confirmation_beautiful = [super(Entity, self).Pretty(**self.__dict(option)) for option in confirms]		
		# set user input
		return self.__strin(request = request, confirm = confirm, reject = reject, null = null, separator = separator, divider = divider, selection_options = selection_options, selection_beautiful = selection_beautiful, confirmation_options = confirmation_options, confirmation_beautiful = confirmation_beautiful, accept = accept, decline = decline)


	def __strin (self, **kwargs):
		### @description: private method for requesting input to match selection options
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set base options
		options = kwargs.get('selection_options')
		# set user input string
		user = str(self.__input(request = kwargs.get('request'), selection = kwargs.get('selection_options'), beautified = kwargs.get('selection_beautiful'), divider = kwargs.get('divider'), separator = kwargs.get('separator')) or kwargs.get('null'))
		# initialise loop to test strings
		for i in range(0, len(options)):
			# confirm selection in options
			if user.upper() == options[i].upper():
				# confirm selection
				return self.__strout(user, **kwargs)
		# notify that user input was not accepted
		print super(Entity, self).say(kwargs.get('reject') % user)
		# request user input
		return self.__strin(**kwargs)

	def __strout (self, arg, **kwargs):
		### @description: private method for confirming returned selection
		### @parameter: <arg>, @type: <str>
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set base options
		options = kwargs.get('confirmation_options')
		# set user input string
		user = str(self.__input(request = kwargs.get('confirm') % arg, selection = kwargs.get('confirmation_options'), beautified = kwargs.get('confirmation_beautiful'), divider = kwargs.get('divider'), separator = kwargs.get('separator')) or kwargs.get('null'))
		# confirm user string matches confirmation string
		if user.upper() == options[0].upper():
			# set first input
			return arg
		# confirm user string matches rejection string
		elif user.upper() == options[1].upper():
			# request new input
			return self.__strin(**kwargs)
		# notify that user input was not accepted
		print super(Entity, self).say(kwargs.get('reject') % user)
		# request user input
		return self.__strout(arg, **kwargs)
		
	def __input (self, **kwargs):
		### @description: private function for collecting user input 
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <str>

		# set user input
		return raw_input(super(Entity, self).say(super(Entity, self).concat(kwargs.get('request'), super(Entity, self).cconcat([super(Entity, self).cconcat(kwargs.get('beautified'), kwargs.get('separator')), kwargs.get('divider'), " "]))))

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
		return { 'string': str(arg), 'attributes': ['BOLD'] } if type(arg) is not dict else self.__syntax(arg)

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
	print Entity(**Persona().__dict__).ask({ 'string': 'A', 'attributes': ['BOLD'], 'tag': True }, { 'string': 'B', 'attributes': ['BOLD'], 'tag': True }, request = 'please enter one option', confirm = Entity.cconcat(['user input', Entity.Pretty('{{%s}}', ['UNDERLINE']), 'correct?'], ' '), reject = Entity.cconcat(['user input', Entity.Pretty('{{%s}}', ['UNDERLINE']), 'is incorrect.'], ' '), accept = {'string': 'YES', 'attributes': ['GREEN','BOLD'], 'tag': True }, decline =  'NO')
