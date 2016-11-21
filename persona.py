#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class Persona (String):

	###########################################
	### public class named printed messages ###
	###########################################

	def say (self, *args):
		### @description: protected method for creating formatted string as a person
		### @parameter: <args>, @type: <list>, @default: <None>
		### @return: @type <str>

		# set args to list
		args = list(args)
		# initialise loop to process arguments
		for i in range(0, len(args)):
			# edit argument to contain formatting if required
			args[i] = super(Persona, self).Pretty(**self.__dict(args[i])) if type(args[i]) is dict else args[i]
		# set complete name with sep syntax
		name = super(Persona, self).Syntax(super(Persona, self).cconcat([self.name, self.separator]))
		# set style to name
		name = super(Persona, self).Pretty(name, self.style)
		# join name with message
		return super(Persona, self).concat(name, super(Persona, self).cconcat(args, " "))

	def __dict (self, arg):
		### @description: private method for setting dict items to enable stylisation
		### @parameter: <arg>, @type: <dict>, @default: <None>
		### @return: @type: <dict>

		# set base string key value pair
		arg['string'] = str(arg['string']) if not None else "sample"
		# set base attibutes key value pair
		arg['attributes'] = list(arg['attributes']) if type(arg['attributes']) is list or type(arg['attributes']) is tuple else ["BOLD"]
		# set base tag key value pair
		arg['tag'] = bool(arg['tag']) if 'tag' in arg else False
		# confirm tag key exits
		if 'tag' in arg and bool(arg['tag']):
			# set string to contain syntax wrapper
			arg['string'] = super(Persona, self).Syntax(arg['string'])
		# edit copied dict to exclude tag key value pair
		map(arg.pop, ["tag"])
		# define base dict
		return arg 

	def __list (self, *args):
		### @description: private method for setting argument
		### @parameter: <args>, @type: <list>, @default: <tuple>
		### @return: @type: <list>
		
		# set base list
		return sum(list(args), [])

	def __str (self, arg = None, fallback = ""):
		### @descrption: private method for setting argument as string
		### @parameter: <arg>, @type: <str>, @default: <None>
		### @parameter: <fallback>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# set base string 
		return str(arg) if arg is not None else str(fallback)

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set message prefixed name, @parameter: <name>, @type: <str>, @default: <None>
		self.name = self.__str(kwargs.get("name", None), "system")
		# set separator character between prefixed name and output string, @parameter: <separator>, @type: <str>, @default: <None>
		self.separator = self.__str(kwargs.get("separator", None), ":")
		# set string style attributes for prefixed name, @parameter: <style>, @type: <list>, @default: <list>
		self.style = self.__list(kwargs.get("style", None))
		print self.style



if __name__ == '__main__':

	# formatted named message
	print Persona(name = "clockwerk", separator = ":", style = ["BOLD", "GREEN"]).say({"string":"bleep!","attributes":["BLUE", "BOLD"],"tag":True}, {"string":"bloop!","attributes":["RED", "BOLD"],"tag":True}, "I am a robot!")
