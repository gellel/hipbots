#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

########################
### file information ###
########################
VERSION = 0.1
AUTHOR = 'lindsay.gelle@gmail.com'

##################################
### python script dependencies ###
##################################
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
	'END': END
}

######################################
### constants: regular expressions ###
######################################
FILTER = r'\{\{{0,2}[^\{\{]+\}\}{0,2}'
SYNTAX = r'{{|}}'
BEAUTIFIED = r'\x1b[^m]*m'


def Log (*args, **kwargs):
	"""Sets multiple arguments to be printed.
	
	User arguments can be set to structure type during concatenation process if required.
	Function can accept a filter argument to manage the contents of the print response.
	Supports the use of concatenation string character.
	"""

	# @parameter: <*args>, @type: <tuple>
	# @use: (optional) arguments required for printing
	args = list(args)

	# @parameter: <**kwargs:as_type>, @type: <function>
	# @use: (optional) sets argument to be printed as required format
	as_type = kwargs.get('as_type', None)

	# @parameter: <**kwargs:filter>, @type: <function>
	# @use: (optional) function for filtering supplied arguments out of list to be concatenated
	manage = kwargs.get('filter', None)

	# @parameter: <**kwargs:join>, @type: <str>
	# @use: (optional) character used for concatenating supplied arguments
	join = str(kwargs.get('join', ''))

	# @return: @type: <None>
	print Concatenate(*[as_type(arg) if hasattr(as_type, '__call__') else arg for arg in args], filter = manage, join = join)


def Concatenate (*args, **kwargs):
	"""Sets multiple arguments to be concatenated by supplied character string. 

	User arguments are set to string type during concatenation process. 
	Function can accept a filter argument to manage the contents of the returned concatenated string.
	"""

	# @parameter: <*args>, @type: <tuple>
	# @use: (optional) arguments required for concatenation
	args = list(args)
	
	# @parameter: <**kwargs:filter>, @type: <function>
	# @use: (optional) function for filtering supplied arguments out of list to be concatenated
	manage = kwargs.get('filter', None)

	# @parameter: <**kwargs:join>, @type: <str>
	# @use: (optional) character used for concatenating supplied arguments
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
	# @use: (optional) string requiring beautification
	string = str(string)	

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: (optional) attribute(s) required for beautification
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
	# @use: (optional) string containing beautification
	string = re.sub(SYNTAX, '', str(string))

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: (optional) filters styles dictionary to exclude certain keys
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]
	
	# set beautification to be removed from string
	encoding = { key: STYLES[key] for key in STYLES if key not in map(str.upper, attributes) }
	# set list containing formatting strings
	formatting = [encoding[key] for key in encoding if encoding[key] in string]
	# set substituted string, removing required beautification strings
	edited = re.sub(r'|'.join(map(re.escape, formatting)), '', string)

	# @return: @type: <str>
	return Concatenate(edited, END) if re.compile(BEAUTIFIED).match(edited) else edited


def AssignPrettyKeys (arg = {}, attributes = [], tag = False):
	"""Sets required key word arguments for pretty. 

	Sets strings to beautification key word arguments or filters dictionary to contain required keys only
	"""

	# @parameter: <arg>, @type: <str/dict>
	# @use: string argument to be set to dictionary or dictionary to be filtered
	arg = { 'string': str(arg) } if type(arg) is not dict else arg

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: (optional) attribute(s) required for beautification
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]

	# @parameter: <tag>, @type: <bool>
	# @use: (optional) requirement of string to include beautification syntax identifier
	tag = bool(tag)

	# set default keys for argument dictionary
	defaults = [{'key': 'string', 'value': ''}, {'key':'attributes', 'value': attributes}, {'key': 'tag','value': tag}]

	# iterate over keys requiring defaults
	for i in range(0, len(defaults)):
		# assign default key value pair
		arg.setdefault(defaults[i]['key'], defaults[i]['value'])

	# @return: @type: <dict>
	return { key: arg[key] for key in arg if key in ['string', 'attributes', 'tag'] }


def Pretty (string = 'EXAMPLE', attributes = ['BOLD'], tag = False):
	"""Sets beautification for multiple points in a string.
	
	Substrings in string that contain pretty syntax receive beautification. 
	If tag is set to true, supplied string is encased in pretty syntax. 
	Requires argument string to not contain existing pretty syntax.
	"""
	
	# @parameter: <string>, @type: <str>
	# @use: (optional) string(s) requiring beautification
	string = str(string) if type(string) not in [list, tuple] else Concatenate(*string)

	# @parameter: <attributes>, @type: <str/list/tuple>
	# @use: (optional) attribute(s) required for beautification
	attributes = attributes if type(attributes) in [list, tuple] else [str(attributes)]
		
	# @parameter: <tag>, @type: <bool>
	# @use: (optional) requirement of string to include beautification syntax identifier
	tag = bool(tag)

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
	