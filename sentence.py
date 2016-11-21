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

	def __items (self, fragments = []):
		### @description: private method for selecting items to be included in final output
		### @parameter: fragments, @type: <list>
		### @returns: <list>

		# initialise loop to process all supplied fragments
		for i in range(0, len(fragments)):
			# process sentence fragment
			fragments[i] = self.__process(fragments[i])
		# return list with none type removed
		return filter(None, fragments)

	def __process (self, fragment = "sample"):
		### @description: private function for processing supplied fragments
		### @parameter: fragment, @type <list> @or <dict> @or <class:sentence> @or <string>
		### @returns: <dict> @or <string>

		# confirm type is list and contains length
		if type(fragment) is list and bool(fragment):
			# pseudo randomly select item
			return self.__process(fragment[random.randrange(0, len(fragment))]) 
		# confirm type is dict and contains keys
		elif type(fragment) is dict and bool(fragment):
			# process fragement dictionary requirements
			fragment = self.__dict(fragment) if bool(fragment) else {}
		# confirm type is instance of sentence class
		elif isinstance(fragment, Sentence):
			# construct sentence
			fragment = fragment.create()
		# return updated fragment
		return fragment

	def __dict (self, fragment = {}):
		### @description: private method for editing dictionary key values for completed string item
		### @parameter: fragment, @type <dict>
		### @returns: <dict>

		# confirm dict contains string
		if not 'string' in fragment:
			# return empty dict
			return {}
		# confirm dictionary contains key tag
		if 'tag' in fragment and bool(fragment['tag']):
			# edit string to contain beautification wrapper
			fragment['string'] = self.tag(fragment['string'])
		# confirm dictionary conatins key optional
		if 'optional' in fragment and bool(fragment['optional']):
			# set random key
			r = random.randrange(0, self.seed) if type(fragment['optional']) is bool else random.randrange(0, fragment['optional'])
			# edit fragment to be empty dictionary if zero is not returned from pseudo random number generator
			fragment = fragment if not r else {}
		# return edited fragment
		return fragment
		
	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: fragment, @type: <list>
		### @parameter: seed, @type: <intger>

		# set random seed attribute; @default <integer>
		self.seed = kwargs.get("seed", random.randrange(2, 6))
		# initialise inherited
		super(Sentence, self).__init__(strings = self.__items(kwargs.get("fragments", [{"string":"{{Hello}}","optional":True,"attributes":["BOLD"]}, "{{world}}!"])))




if __name__ == '__main__':

	# create example pseudo random sentence
	print Sentence(fragments = [["Hi there", ["Bonjour", "Guten Tag", "Hej"]], ["!", "."], {"string":"How are you", "attributes":["BOLD"], "tag":True}, "?", Sentence(fragments = [["I'm", "I am"], "doing", ["fine", "good", "great"], ["!", "."]]), Sentence(fragments = ["What's", ["new", "different", "changed", "happening"], [{"string":"today","tag":True}, {"string":"these {{days}}","attributes":["BOLD"]}], "?"]) ]).create()
