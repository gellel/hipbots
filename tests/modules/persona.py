#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

########################
### file information ###
########################
VERSION = 0.1
AUTHOR = 'lindsay.gelle@gmail.com'

###################################
### python scripts dependencies ###
###################################
### import strings module
import strings


class Persona (object):
	"""Simulates requests and responses from a system, person or other agent.
	
	Uses 'strings' module for easier string formatting.
	"""

	def say (self, *args, **kwargs):
		"""Creates strings prefixed by persona's name.

		Uses classes '__name' function (private) to construct prefix for response output. 
		Assigns this prefix as a concatenation argument as well as supplied arguments.
		Intended to represent a reply on the behalf of this 'persona'.
		Function arguments can be formatted as beautified strings to create more interesting responses.
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
		args = [strings.Pretty(**{ key: arg[key] for key in arg if key in ['string', 'attribute', 'tag'] }) if type(arg) is dict else arg for arg in args]

		# @return: @type: <str>
		return strings.Concatenate(*[self.__name()] + args, filter = manage, join = join)


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
		
	print Persona(name = '[terminal]:', attributes = ['RED', 'BOLD']).say('hello!', {'string':'all system go!', 'tag': 1, 'attributes': 'BOLD'})
	