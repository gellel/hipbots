#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import pseudo random
import random


class Sentence (String):

	##################################################################################
	### extended class of strings.String, creates beautified pseudo random strings ###
	##################################################################################

	def randomise (self):
		### @description: protected function of class, used to generate pseudo random string from defined fragments
		### @return: @type: <str>

		# process argument fragment collection 
		return self.__process(self.fragments)

	def __process (self, fragments = []):
		### @description: private function of class, processes argument collection from constructor
		### @return: @type: <str>

		# set default fragments list
		# @parameter: <fragments>, @type: <list>, @default: <list>
		fragments = fragments if type(fragments) is list else []

		# initialise loop to process individual fragment arguments and process item by its type requirement
		return super(Sentence, self).Cconcat(filter(None, [self.__type(fragment) for fragment in fragments]), ' ')

	def __type (self, fragment):
		### @description: private function of class, tests data type of fragment to construct response
		### @return: @type: <str>

		# confirm fragment is a sequence
		if type(fragment) in [list, tuple]:
			# confirm sequence contains content
			if bool(fragment):
				# pseudo randomly select item from sequence using length as random seed
				return self.__type(fragment[random.randrange(0, len(fragment))])
		# confirm fragment is a dictionary
		if type(fragment) is dict:
			# confirm dictionary contains keys
			if bool(fragment):
				# confirm optional key present in dictionary and pseudo random number rolled zero
				if 'optional' in fragment and not bool(fragment['optional']) and bool(random.randrange(0, random.randrange(0, 10))):
					# set empty string for exclusion
					return ''
				# process selection beautifing string
				return super(Sentence, self).Pretty(**super(Sentence, self).SetPrettyKeys(fragment)) if 'string' in fragment and not type(fragment['string']) in [list, tuple] else Sentence(*fragment['string']).randomise()
		# confirm fragment is an instance of Sentence
		if isinstance(fragment, Sentence):
			# construct sentence
			return fragment.randomise()
		# confirm fragment is not considered false and construct beautified string else return empty
		return super(Sentence, self).Pretty(**super(Sentence, self).SetPrettyKeys(fragment)) if bool(fragment) else ''

	def __init__ (self, *args):
		### @descrption: class constructor

		# set default sentence string fragments
		# @parameter: <args>, @type: <tuple>, @default: <tuple>
		self.fragments = filter(None, list(args or [['Hello', 'Bonjour', 'Salut', 'Guten Tag']]))




if __name__ == '__main__':

	# create pseudo random sentence
	print Sentence([{'string':[[1, 2, 3]]}], [{'string':'Hello','tag':True,'attributes':['GREEN', 'BOLD']}, {'string':'Bye!','tag':True,'attributes':['RED', 'BOLD']}]).randomise()
	