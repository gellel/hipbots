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
	"""Creates strings prefixed by a defined persona name.
	
	Intended to represent a reply from a system, character or other agent.
	Uses 'strings' modules for easier string formatting.
	"""

	def __str__ (self):
		"""Class stringification method
		
		Describes name prefix and assigned attributes
		"""

		# set persona name description string
		name = strings.Concatenate('Persona name:', ' ', self.name)
		# set persona attributes description string
		attributes = strings.Concatenate('Assigned styles:', ' ', self.attributes if type(self.attributes) is str else strings.Concatenate(*self.attributes))
		
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
		self.attributes = kwargs.get('attributes', 'BOLD')




if __name__ == '__main__':
	
	print Persona().__str__()
	