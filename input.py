#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import persona response
from persona import Persona
### import regular expressions
import re


class Binary (Persona):

	############################################
	### public class for named input prompts ###
	############################################

	def prompt (**kwargs):
		### @description: protected method for creating stylised user input
		### @parameter: <request>, @type: <str>
		### @parameter: <options>, @type: <list>
		pass

	def __input (self, message = None):
		### @description: private method to construct raw input handler
		### @parameter: <message>, @type: <str>, @default: <None>
		pass

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set call to inherited Persona
		# @parameter: <name>, @type: <str>, @default: <None>
		# @parameter: <separator>, @type: <str>, @default: <None>
		# @parameter: <style>, @type: <list>, @default: <None>
		super(Binary, self).__init__(name = kwargs.get("name"), separator = kwargs.get("separator"), style = kwargs.get("style"))




if __name__ == '__main__':

	# formatted named raw input
	print Binary().say()
