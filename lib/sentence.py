#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from lib.strings import String
### import pseudo random
import random


class Sentence (String):

	#############################################################################
	### extended string class to build out beautified strings pseudo randomly ###
	#############################################################################

	def randomise (self):
		### @description: protected function for creating pseudo random sentence from initialised argument strings
		### @return: @type: <str>

		# construct random string from supplied sentence fragments, separated by defined character
		return self.__process(self.fragments, self.separator)

	def __process (self, fragments, separator):
		### @description: private function for selecting items to be included in final output
		### @parameter: <fragments>, @type: <list>, @default: <list>
		### @parameter: <separator>, @type: <str>, @default: <str>
		### @return: @type: <str>	

		# set all fragments to their defined structures
		fragments = [self.__type(fragment) for fragment in fragments]
		# filter fragments to exclude dictionaries where key string is missing value
		fragments = [fragment for fragment in fragments if 'string' in fragment and bool(fragment['string'])]
		# initialise loop to construct sentence from fragments while beautifying each partial item where syntax included
		return super(Sentence, self).Cconcat([super(Sentence, self).Pretty(**fragment) for fragment in fragments], separator)

	def __type (self, arg):
		### @description: private function for processing supplied fragments based on their data types
		### @parameter: <arg>, @type: <str/dict/list/instance:Sentence>, @default: <None>
		### @return: @type: <dict>

		# confirm argument is sequence construct
		if type(arg) in [tuple, list] and bool(arg):
			# extract sequence item from length using the total length as the random number seed
			return self.__type(arg[random.randrange(0, len(arg))])
		# otherwise confirm argument is instance of sentence class
		elif isinstance(arg, Sentence):
			# construct sentence from initialised
			arg = self.__dict(arg.randomise())
		# manage keys for beautification handler
		return self.__keys(self.__dict(arg))

	def __keys (self, arg):
		### @description: private function for defining base dictionary keys
		### @parameter: <arg>, @type: <dict>, @default: <dict>
		### @return: @type: <dict>

		# confirm dictionary contains key fragments of sentence
		if 'fragments' in arg and type(arg['fragments']) in [list, tuple] and bool(arg['fragments']):
			# set string key to be result of compiled sentence
			arg['string'] = Sentence(*arg['fragments'], **arg).randomise()
		# confirm optional inclusion
		if 'optional' in arg and type(arg['optional']) is int:
			# set dictionary to empty if random number throws zero
			arg = {} if not bool(random.randrange(0, arg['optional'])) else arg
		# construct dictionary with required keys
		return { key: arg[key] for key in arg if key in ['tag', 'string', 'attributes'] }
 
	def __dict (self, arg):
		### @description: private function for defining base dictionary syntax
		### @parameter: <arg>, @type: <*>, @default: <dict>
		### @return: @type: <dict>

		# set base dictionary
		return { 'string': super(Sentence, self).SetStrType(arg), 'attributes': [], 'tag': False } if type(arg) is not dict else arg

	def __init__ (self, *args, **kwargs):
		### @descrption: class constructor
		### @parameter: <kwargs>, @type: <dict>

		# set sentence fragments
		# @parameter: <args>, @type: <list/tuple>
		self.fragments = list(args) or [['Hello', 'Hej', 'Guten Tag']]
		# set character for concatentation
		# @parameter: <separator>, @type: <str>, @default: <str>
		self.separator = super(Sentence, self).SetStrType(kwargs.get('separator', ' '))
		# set random prefixed seed
		# @parameter: <seed>, @type: <int>, @default: <int>
		self.seed = kwargs.get('seed', random.randrange(random.randrange(1, 5), random.randrange(6, 11)))




if __name__ == '__main__':

	# build pseudo random string
	print Sentence([['a', 'b'], ['c', 'd']]).randomise()
	