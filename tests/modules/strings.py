#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

########################
### file information ###
########################
VERSION = 0.1
AUTHOR = 'lindsay.gelle@gmail.com'

###################################
### python scripts dependencies ###
###################################
### import regexp module
import re

#################################
### ANSI base text formatting ###
#################################
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

##################################
### ANSI formatting dictionary ###
##################################
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
	'END': END
}

###########################################
### module regular expression constants ###
###########################################
FILTER = r'\{\{{0,2}[^\{\{]+\}\}{0,2}'
SYNTAX = r'{{|}}'
BEAUTIFIED = r'\x1b[^m]*m'


def Concatenate (*args, **kwargs):
	"""Sets multiple arguments to be concatenated by supplied character string. 

	User arguments are set to string type during concatenation process. 
	Function can accept a filter argument to manage the contents of the returned concatenated string.
	"""

	# @parameter: <*args>, @type: <tuple>
	# @use: arguments required for concatenation
	args = list(args)
	
	# @parameter: <**kwargs:filter>, @type: <function>
	# @use: function for filtering supplied arguments out of list to be concatenated
	manage = kwargs.get('filter', None)

	# @parameter: <**kwargs:join>, @type: <str>
	# @use: character used for concatenating supplied arguments
	join = str(kwargs.get('join', ''))

	# @return: @type: <str>
	return str(join).join([str(arg) for arg in filter(manage if hasattr(manage, '__call__') else None, args)])


def AssignStyle (string = 'EXAMPLE', attributes = []):
	"""Sets string to contain beautification formatting. 

	Style attributes can be supplied as a string, list or tuple. 
	Sequence arguments are expected to contain strings referring to their style reference. 
	Beautification attributes can be nested to produce more complex styles.
	"""

	# @parameter: <string>, @type: <str>
	# @use: string required for ansi formatting
	string = str(string)	

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: attribute(s) required for beautification
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]

	# set attributes as concatenated string (if defined in styles dictionary)
	encoding = ''.join([STYLES[attr] for attr in map(str.upper, attributes) if attr in STYLES])

	# @return: @type: <str>
	return Concatenate(encoding, string, END)


def EraseStyle (string = '\033[91mEXAMPLE\033[0m', attributes = []): 
	"""Removes beautification formatting from string. 
	
	Style attributes can be supplied as a string, list or tuple. 
	Sequence arguments are expected to contain strings referring to their style reference. 
	Supplied attributes are not removed from string.
	"""

	# @parameter: <string>, @type: <str>
	# @use: string containing formatting
	string = re.sub(SYNTAX, '', str(string))

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: filters styles dictionary to exclude certain keys
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]
	
	# set beautification to be removed from string
	encoding = { key: STYLES[key] for key in STYLES if not key in map(str.upper, attributes) }
	# set list containing formatting strings
	formatting = [encoding[key] for key in encoding if encoding[key] in string]
	# set substituted string, removing required beautification strings
	edited = re.sub(r'|'.join(map(re.escape, formatting)), '', string)

	# @return: @type: <str>
	return Concatenate(edited, END) if re.compile(BEAUTIFIED).match(edited) else edited


def Pretty (string = 'EXAMPLE', attributes = ['BOLD'], tag = False):
	"""Sets beautification for multiple points in a string.
	
	Substrings in string that contain pretty syntax receive beautification. 
	If tag is set to true, supplied string is encased in pretty syntax. 
	Requires string does not contain pretty syntax.
	"""
	
	# @parameter: <string>, @type: <str>
	# @use: string(s) required for ansi encoding
	string = str(string) if not type(string) in [list, tuple] else Concatenate(*string)

	# @parameter: <tag>, @type: <bool>
	# @use: requirement of string to include beautification syntax identifier
	tag = bool(tag)

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: attribute(s) required for beautification
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]
		
	# set string to contain pretty syntax if required and string does not contain pretty syntax
	string = Concatenate('{{', string, '}}') if tag and not re.compile(SYNTAX).search(string) else string
	# find strings containing pretty syntax
	matches = re.findall(FILTER, string, re.DOTALL)

	# iterate over substrings requiring beautification
	for i in range(0, len(matches)):
		# substitute substring with beautified replacement
		string = re.sub(matches[i], AssignStyle(re.sub(SYNTAX, '', matches[i]), attributes), string)
	
	# @return: @type: <str>
	return re.sub(SYNTAX, '', string)




if __name__ == '__main__':

	# create beautified string and substract style
	print EraseStyle(Pretty("{{Hello}}", ['RED', 'BOLD', 'BLINK']), ['RED', 'BOLD'])
	