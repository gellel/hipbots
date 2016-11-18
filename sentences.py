#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings class
from strings import String
### py pseudo random 
import random




class Sentence (String):

	###################################################################
	### creates complete string from pseudo randomly selected parts ###
	###################################################################

	def create (self):
		### @description: protected method for creating pseudo random sentence from initialised strings
		### @returns: <string>

		# use inherited private method to concatenate strings create from init method on super.String
		return super(Sentence, self).create()

	def __test (self, fragments = []):
		### @description: private method for selecting items to be included in final output
		### @parameter: fragments, @type: <list>
		### @returns: <list>

		# initialise loop to process fragments
		for i in range(0, len(fragments)):
			# set fragment index to filtered item
			fragments[i] = self.__fragment(fragments[i])
		# return filter list exlcuding non boolean values
		return filter(None, fragments)

	def __fragment (self, fragment = None):
		### @description: private method for breaking down nested fragments to create more varied returned string
		### @parameter: fragment, @type: <string> or <dict> or <list>
		
		# confirm fragment is type list
		if type(fragment) is list:
			# set selection for fragement argument from pseudo random 
			fragment = fragment[random.randrange(0, len(fragment))]
		# confirm fragment is instance of Sentence class
		elif isinstance(fragment, Sentence):
			# set fragment to be constructed result
			fragment = fragment.create()
		# return filted fragment after it has been potentially processed by optional private method
		return self.__optional(fragment) if type(fragment) is dict else fragment
	
	def __optional (self, fragment = False):
		### @description: private method for determining whether fragment that is dictionary with key optional should be include based on psuedo random number generation
		### @parameter: fragment, @type: <dict> or <string>
		### @returns: <dict> or <boolean>

		# confirm that dict contains optional key and type is not none or false
		if 'optional' in fragment and bool(fragment['optional']):
			# generate pseudo random number from either boolean true or supplied integer
			r = random.randrange(0, random.randrange(1, self.seed)) if type(fragment['optional']) is bool else random.randrange(0, fragment['optional'])
			# set supplied fragment argument to false if random number is not zero
			fragment = fragment if not r else False
		# return updated fragement argument
		return fragment
		
	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: fragment, @type: <list>
		### @parameter: seed, @type: <intger>

		# set random seed attribute; @default <integer>
		self.seed = kwargs.get("seed", random.randrange(2, 6))
		# initialise inherited
		super(Sentence, self).__init__(strings = self.__test(kwargs.get("fragments", [{"string":"{{Hi!}}","optional":True,"attributes":["BOLD"]}, {"string":"I am written in {{Python}}."}, ["How are you?", "Hope you are well!"], {"string":"Thanks for reading.","optional":4}])))



if __name__ == '__main__':

	# create example sentence
	print Sentence().create()
