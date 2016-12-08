#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String


class Persona (String):

	####################################################################################################
	### extended class of strings.String, creates beautified string terminal output prefixed by name ###
	####################################################################################################

	def say (self, *args):
		### @description: protected function of class, concatenates arguments to single string that is prefixed by the defined name of the class instance to simulate a response from character or system
		### @return: @type: <str>

		# set default list from supplied arguments tuple to format arguments into expected type
		# @parameter: <args>, @type: <tuple>, @default: <tuple>
		args = [super(Persona, self).SetStringDict(arg) for arg in list(args)]

		# concatenate supplied arguments using String.Cconcat to produce single uniform string
		return super(Persona, self).Concat(self.__name(), super(Persona, self).Cconcat([super(Persona, self).Pretty(**arg) for arg in filter(None, args)], ' '))

	def __name (self):
		### @description: private function of class, creates beautified string using class instances attribute name
		### @return: @type: <str>

		# create beautified string using String.Pretty to apply defined styling to name and separator attributes
		return super(Persona, self).Pretty(super(Persona, self).Syntax(super(Persona, self).Cconcat([self.name, self.separator])), self.style)

	def __init__ (self, **kwargs):
		### @description: class constructor

		# set default name string for persona prefix
		# @parameter: <kwargs:name>, @type: <str>, @default: <str>
		self.name = super(Persona, self).SetStringType(kwargs.get('name')) or 'system'
		# set default separation string 
		# @parameter: <kwargs:separator> @type: <str>, @default: <str>
		self.separator = super(Persona, self).SetStringType(kwargs.get('separator')) or ':'
		# set default style attributes for name
		# @parameter: <kwargs:style>, @type: <list>, @default: <list>
		self.style = list(kwargs.get('style', ['BOLD']))




if __name__ == '__main__':

	# create example output
	print Persona().say({'string': 'Beep!', 'attributes': ['BOLD'], 'tag': True}, {'string': 'Boop!', 'attributes': ['BOLD'], 'tag': True}, ['I am a {{ROBOT!}}'])
	