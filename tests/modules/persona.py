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
		# @use: (optional) function for filtering supplied arguments out of list to be concatenated
		argument_filter = kwargs.get('filter', None)

		# @parameter: <**kwargs:join>, @type: <str>
		# @use: (optional) character used for concatenating supplied arguments
		string_join = str(kwargs.get('join', ''))

		# set dictionary arguments to be beautified
		args = [strings.Pretty(**strings.AssignPrettyKeys(arg)) if type(arg) is dict else arg for arg in args]

		# @return: @type: <str>
		return strings.Concatenate(self.__name(), ' ', strings.Concatenate(*args), filter = manage, join = join)


	def __request (self, **kwargs):
		"""

		"""
		return self.__prompt(kwargs.get('arguments'), kwargs.get('input_request'), kwargs.get('argument_divider'))


	def __prompt (self, input_choices = [], input_request = 'please input text', argument_divider = '/'):
		"""Creates raw input request prefixed by persona's name.
		
		Concatenates input choices by argument divider string. Empty input choices lists are not included in prompt.
		Prompts are prefixed by persona's name with input request trailing the constructed name.
		"""

		# @parameter: <input_choices>, @type: <list>
		# @use: sets prompt to expect input string to match item in list
		input_choices = filter(None, input_choices)

		# @parameter: <input_request>, @type: <str/dict>
		# @use: acts as string to inform user what input is expected or required
		input_request = strings.Pretty(**strings.AssignPrettyKeys(input_request))

		# @parameter: <argument_divider>, @type: <str/dict>
		# @use: separates user input choices
		argument_divider = strings.Pretty(**strings.AssignPrettyKeys(argument_divider))

		# set input prompt request string including persona name
		string_request = strings.Concatenate(self.__name(), ' ', input_request)
		# set request options string separated by argument dividing character string 
		string_options = argument_divider.join([strings.Pretty(**strings.AssignPrettyKeys(choice)) for choice in input_choices])

		# @return: @type: <str>
		return raw_input(strings.Concatenate(string_request, ' ', string_options, ' ') if bool(string_options) else strings.Concatenate(string_request, ' '))


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
	
	strings.Log(Persona().ask('a', 'b'))	
	#strings.Log(Persona(name = '[terminal]:', attributes = ['RED', 'BOLD']).say('hello!', {'string':'all system go!', 'tag': 1, 'attributes': 'BOLD'}))
	