#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String


class Persona (String):

	###########################################
	### public class named printed messages ###
	###########################################

	def say (self, *args):
		### @description: protected function for creating formatted string as a person
		### @parameter: <args>, @type: <list>, @default: <None>
		### @return: @type: <str>

		# set supplied arguments to python list
		args = list(args)
		# initialise loop to process arguments
		for i in range(0, len(args)):
			# edit current argument to contain formatted string
			args[i] = super(Persona, self).Pretty(**self.__dict(args[i])) if type(args[i]) is dict else args[i]
		# join name with message
		return super(Persona, self).Concat(self.__name(), super(Persona, self).Cconcat(args, ' '))

	def __name (self):
		### @description: private function for creating formatted personas name
		### @return: @type: <str>

		# set base prefixed name for console output
		name = super(Persona, self).Syntax(super(Persona, self).Cconcat([self.name, self.separator]))
		# apply formatting attributes for name
		return super(Persona, self).Pretty(name, self.style)
	
	def __dict (self, arg = {}):
		### @description: private function for setting dict items to enable stylisation
		### @parameter: <arg>, @type: <dict>, @default: <dict>
		### @return: @type: <dict>

		# set dictionary key string as defined pair use String default
		arg['string'] = str(arg['string']) if not None else super(Persona, self).SAMPLE
		# set style attibutes for dictionary
		arg['attributes'] = list(arg['attributes']) if type(arg['attributes']) is list or type(arg['attributes']) is tuple else ['BOLD']
		# supply constructed dictionary
		return arg 

	def __list (self, *args):
		### @description: private function for setting argument
		### @parameter: <args>, @type: <list>, @default: <tuple>
		### @return: @type: <list>

		# set base list from supplied arguments
		return sum(filter(None, list(args)), [])


	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set message prefixed name
		# @parameter: <name>, @type: <str>, @default: <None>
		self.name = super(Persona, self).SetStrType(kwargs.get('name', None)) or 'system'
		# set separator character between prefixed name and output string 
		# @parameter: <separator>, @type: <str>, @default: <None>
		self.separator = super(Persona, self).SetStrType(kwargs.get('separator', None)) or ':'
		# set string style attributes for prefixed name 
		# @parameter: <style>, @type: <list>, @default: <list>
		self.style = self.__list(kwargs.get('style'))




if __name__ == '__main__':

	# formatted named message
	print Persona(name = 'clockwerk', separator = ':', style = ['BOLD']).say({ 'string': 'bleep!', 'attributes': ['BLUE', 'BOLD'], 'tag': True }, { 'string': 'bloop!', 'attributes': ['RED', 'BOLD'], 'tag': True }, 'I am a robot!')
