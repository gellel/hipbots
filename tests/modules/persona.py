#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

########################
### file information ###
########################
VERSION = 0.1
AUTHOR = 'lindsay.gelle@gmail.com'

##################################
### python script dependencies ###
##################################
### import strings module
import strings


class Persona (object):
	"""Simulates requests and responses from a system, person or other agent.
	
	Uses 'strings' module for easier string formatting.
	"""

	def ask (self, *args, **kwargs):
		"""Creates prompt string prefixed by persona's name.
		
		User arguments are set to string type during request process if provided.
		Provided arguments are used as a selection criteria to simulate persona asking for a specific outcome.
		"""

		# @parameter: <*args>, @type: <tuple>
		# @use: arguments used to define a preset of options for input to match
		args = list(args)

		# @parameter: <**kwargs:input_request>, @type: <str/dict>
		# @use: serves as the primary request string for user prompt
		input_request = kwargs.get('input_request', 'please enter your desired input selection')

		# @parameter: <**kwargs:input_success>, @type: <str/dict>
		# @use: (optional) acts as an expression of user input from prompt function and input handler
		input_success = kwargs.get('input_success', None)

		# @parameter: <**kwargs:input_failure>, @type: <str/dict>
		# @use: (optional) acts as an expression of incorrect input from prompt function and input handler
		input_failure = kwargs.get('input_failure', None)

		# @parameter: <**kwargs:input_null>, @type: <str/dict>
		# @use: (optional) expresses empty input submissions from prompt function
		input_null = kwargs.get('input_null', 'empty')

		# @parameter: <**kwargs:input_accept>, @type: <str/dict>
		# @use: (optional) acts as input pattern for flagging that input submission was correct
		input_accept = kwargs.get('input_accept', 'yes')

		# @parameter: <**kwargs:input_reject>, @type: <str/dict>
		# @use: (optional) acts as input pattern for flagging that input submission was incorrect
		input_reject = kwargs.get('input_reject', 'no')

		# @parameter: <**kwargs:argument_divider>, @type: <str/dict>
		# @use: (optional) separaters user arguments by character string to assist in readability
		argument_divider = kwargs.get('argument_divider', '/')

		# @return: @type: <str>
		return self.__request(arguments = args, input_request = input_request, input_success = input_success, input_failure = input_failure, 
			input_null = input_null, input_accept = input_accept, input_reject = input_reject, argument_divider = argument_divider)


	def say (self, *args, **kwargs):
		"""Creates strings prefixed by persona's name.

		Adds persona's name as a concatenation argument as well as supplied arguments.
		Dictionaries arguments are formatted as beautified strings to create more interesting responses.
		"""

		# @parameter: <*args>, @type: <tuple>
		# @use: arguments required for concatenation
		args = list(args)

		# @parameter: <**kwargs:filter>, @type: <function>
		# @use: function for filtering supplied arguments out of list to be concatenated
		manage = kwargs.get('filter', None)

		# @parameter: <**kwargs:join>, @type: <str>
		# @use: character used for concatenating supplied arguments
		join = str(kwargs.get('join', ' '))

		# set dictionary arguments to be beautified
		args = [strings.Pretty(**strings.AssignPrettyKeys(arg)) if type(arg) is dict else arg for arg in args]

		# @return: @type: <str>
		return strings.Concatenate(*[self.__name()] + args, filter = manage, join = join)


	def __request (self, **kwargs):
		"""

		"""
		return kwargs


	def __prompt (self, input_choices = [], input_request = 'enter text', argument_divider = '/'):
		"""
		"""
		pass


	def __name (self):
		"""Creates formatted name prefix.

		Constructs persona name used throughout response or request functions.
		"""

		# @return: @type: <str>
		return strings.AssignStyle(self.name, self.attributes)


	def __str__ (self):
		"""Class stringification method.

		Describes persona's defined name and assigned style attributes. 
		"""

		# set persona name description string
		name = strings.Concatenate('Persona name:', ' ', self.name)
		# set persona attributes description string
		attributes = strings.Concatenate('Assigned styles:', ' ', self.attributes or 'EMPTY' if type(self.attributes) is str else strings.Concatenate(*self.attributes or ['EMPTY']))
		
		# @return: @type: <str>
		return strings.Concatenate(name, ' ', '|', ' ', attributes)


	def __init__(self, **kwargs):
		"""Class constructor.

		Supports inheritence.
		"""

		# set required inheritences
		super(Persona, self).__init__()
		
		# @parameter: <**kwargs:name>, @type: <str>
		# @use: prefixes strings output by class
		self.name = str(kwargs.get('name', 'system'))

		# @parameter: <**kwargs:attributes>, @type: <str/list/tuple>
		# @use: attribute(s) required for beautification
		self.attributes = kwargs.get('attributes', [])




if __name__ == '__main__':
	
	#strings.Log(Persona().ask(dank = 'memes'))	
	strings.Log(Persona(name = '[terminal]:', attributes = ['RED', 'BOLD']).say('hello!', {'string':'all system go!', 'tag': 1, 'attributes': 'BOLD'}))
