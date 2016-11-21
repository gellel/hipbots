#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String


class MSG (String):

	##########################################
	### public clas named printed messages ###
	##########################################

	def send (self, *args):
		### @description: protected method for creating formatted string
		### @parameter: <args>, @type: <list>, @default: <None>
		### @return: @type <str>

		# set base string for output
		string = ""
		# set args to list
		args = list(args)
		# initialise loop to process arguments
		for i in range(0, len(args)):
			# edit argument to contain formatting if required
			args[i] = super(MSG, self).Pretty(**self.__dict(args[i])) if type(args[i]) is dict else args[i]
		# join strings by white space string
		return super(MSG, self).cconcat(args, " ")

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
			arg['string'] = super(MSG, self).Syntax(arg['string'])
		# edit copied dict to exclude tag key value pair
		map(arg.pop, ["tag"])
		# define base dict
		return arg 

	def __list (self, *args):
		### @description: private method for setting argument
		### @parameter: <args>, @type: <list>, @default: <None>
		### @return: @type: <list>

		# define base list
		return args if type(args) is list else ["BOLD", "UNDERLINE"] 

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
		# set seperator character between prefixed name and output string, @parameter: <seperator>, @type: <str>, @default: <None>
		self.seperator = self.__str(kwargs.get("seperator", None), ":")
		# set string style attributes for prefixed name, @parameter: <style>, @type: <list>, @default: <list>
		self.style = self.__list(kwargs.get("style", None))




if __name__ == '__main__':

	# format named message
	print MSG().send("hello", {"string":"yall","attributes":["RED"],'tag'})
