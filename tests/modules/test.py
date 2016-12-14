#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

##################################
### python script dependencies ###
##################################
### import future print function
from __future__ import print_function
### import regexp module
import re

############################################
### constants: string formatting options ###
############################################
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[37m'
BLINK = '\033[5m'
INVERSE = '\033[7m'
HIDDEN = '\033[8m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

STYLES = { 
	'PURPLE': PURPLE, 
	'CYAN': CYAN, 
	'DARKCYAN': DARKCYAN, 
	'BLUE': BLUE, 
	'GREEN': GREEN, 
	'YELLOW': YELLOW, 
	'RED': RED, 
	'WHITE': WHITE, 
	'BLINK': BLINK,
	'INVERSE': INVERSE,
	'HIDDEN': HIDDEN,
	'BOLD': BOLD,
	'UNDERLINE': UNDERLINE,
	'END': END }

######################################
### constants: regular expressions ###
######################################
FILTER = r'\{\{{0,2}[^\{\{]+\}\}{0,2}'
SYNTAX = r'{{|}}'
BEAUTIFIED = r'\x1b[^m]*m'



def Concatenate (*args, **kwargs):
	"""Sets multiple arguments to be concatenated by supplied character string. 

	User arguments are set to string type during concatenation process. 
	Function can accept a filter argument to manage the contents of the returned concatenated string.
	"""

	# named function arguments #

	# @parameter: <kwargs:string_join>, @type: <str>
	# Used to concatenate each of the supplied function arguments.
	string_join = kwargs.get('string_join', '')

	# @parameter: <kwargs:type_filter>, @type: <function>
	# Used to filter out or in (based on definition) supplied arguments.
	type_filter = kwargs.get('type_filter', None)

	# @return: @type: <str>
	return str(string_join).join(map(str, filter(type_filter if hasattr(type_filter, '__call__') else None, list(args))))


def ApplyStyle (string = 'HELLO', attributes = []):
	"""Sets string argument to contain colour, weight or style formatting. 
	
	Formatting styles can be supplied as a string, list or tuple.
	Sequence arguments are expected to contain strings referring to their formatting reference. 
	"""

	# named function arguments #

	# @parameter: <string>, @type: <str>
	# Used as anchor for formatting attribute assignment.
	string = str(string)

	# @parameter: <attributes>, @type: <str/list/tuple>
	# Used for selecting escaped formatting strings from styles dictionary.
	attributes = map(str.upper, attributes) if type(attributes) in [list, tuple] else [str(attributes).upper()]

	# @return: @type: <str>
	return Concatenate(''.join([STYLES[attr] for attr in attributes if attr in STYLES]), string, END) 


def EraseStyle (string = '\033[91mHELLO\033[0m', attributes = []):
	"""Sets string argument to exclude colour, weight or style formatting. 
	
	Formatting styles can be supplied as a string, list or tuple.
	Sequence arguments are expected to contain strings referring to their formatting reference.
	Supplied attributes are removed from string.
	"""

	# named function arguments #

	# @parameter: <string>, @type: <str>
	# Used as an anchor for removing assigned formatting attributes.
	string = re.sub(SYNTAX, '', str(string))

	# @parameter: <attributes>, @type: <str/list/tuple>
	# Used for selecting escaped formatting strings from styles dictionary.
	attributes = map(str.upper, attributes) if type(attributes) in [list, tuple] else [str(attributes).upper()]

	# set string substitutions for found styles
	string = re.sub(r'|'.join(map(re.escape, [STYLES[key] for key in filter(None, attributes)])), '', string)

	# @return: @type: <str>
	return Concatenate(string, END) if re.compile(BEAUTIFIED).match(string) and END not in string else re.sub(re.escape(END), '', string)





if __name__ == '__main__':

	print(repr(EraseStyle(ApplyStyle('hello', ['RED', 'BLINK']), ['BLINK','RED'])))
	