#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strs import String
### import pseudo random
import random


class Sentence (String):

	###################################################################
	### creates complete string from pseudo randomly selected parts ###
	###################################################################

	def randomize (self):
		### @description: protected method for creating pseudo random sentence from initialised strings
		### @returns: <string>

		# construct random string from supplied
		return self.__process(self.fragments)

	def __process (self, fragments):
		### @description: private method for selecting items to be included in final output
		### @parameter: fragments, @type: <list>
		### @returns: <str>

		# initialise loop to process text fragments
		for i in range(0, len(fragments)):
			# set fragment to supported
			fragments[i] = self.__type(fragments[i])
		# reduce fragments
		return super(Sentence, self).cconcat(filter(None, [super(Sentence, self).Pretty(**arg) for arg in fragments]), ' ')

	def __option (self, fragment):
		### @description: private function for setting inclusion status of string fragment
		### @paramater: <fragment>, @type: <dict>
		### @return: <dict>

		# confirm dictionary conatins key optional
		if 'optional' in fragment and bool(fragment['optional']):
			# set random key
			r = random.randrange(0, self.seed) if type(fragment['optional']) is bool else random.randrange(0, int(fragment['optional']))
			# edit fragment to be empty dictionary if zero is not returned from pseudo random number generator
			fragment = fragment if not r else {}
		# set fragment
		return fragment

	def __type (self, fragment = None):
		### @description: private function for processing supplied fragments
		### @parameter: <fragment>, @type: <str/dict/list/instance:Sentence>
		### @return: @type: <dict>

		# confirm non string type
		if type(fragment) in [unicode, int, float, long, complex]:
			# set fragment to base string
			fragment = str(fragment)
		# confirm fragment is a list
		if type(fragment) is list or type(fragment) is tuple:
			# select random item from list length
			return self.__type(fragment[random.randrange(0, len(fragment))])
		# confirm fragment is a str
		elif type(fragment) is str:
			# set fragment to dict
			fragment = self.__dict(fragment)
		# confirm fragment is instance of Sentence
		elif isinstance(fragment, Sentence):
			# set constructed to dict
			fragment = self.__dict(fragment.randomize())
		# set exclusion for fragment
		return self.__option(fragment)

	def __dict (self, arg = 'sample'):
		### @description: private method for casting argument to string.pretty kwargs
		### @parameter: <arg>, @type: <dict/str>, @default: <str>
		### @return: @type: <dict>

		# cast argument to dict if argument is string otherwise assume dict
		return { 'string': str(arg), 'attributes': ['BOLD'] } if type(arg) is not dict else arg

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set random prefixed seed
		# @parameter: <seed>, @type: <int>, @default: <int>
		self.seed = kwargs.get('seed', random.randrange(2, 6))
		# set fragments for construction
		# parameter: <fragments>, @type: <list>, @default: <list>
		self.fragments = kwargs.get('fragments', [ [{ 'string': 'Hello' }, { 'string': 'Guten Tag' }, { 'string': 'Bonjour' }], ['.', '!'], 'How are you?'])
	
	

		
if __name__ == '__main__':

	# create example pseudo random sentence
	print Sentence(fragments = [['Hi there', ['Bonjour', 'Guten Tag', 'Hej']], ['!', '.'], { 'string': 'How are you', 'attributes': ['BOLD'], 'tag': True }, '?', Sentence(fragments = [['I\'m', 'I am'], 'doing', ['fine', 'good', 'great'], ['!', '.']]), Sentence(fragments = ['What\'s', ['new', 'different', 'changed', 'happening'], [{ 'string': 'today', 'tag': True }, { 'string': 'these {{days}}', 'attributes': ['BOLD'] }], '?']) ]).randomize()
