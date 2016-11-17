#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### py requests class package
import requests
### py random class package
import random
### py json class package
import json
### py system class package
import sys
### py os class package
import os
### py regex
import re

### script exe base file directory
__FILEPATH__ = os.path.dirname(os.path.realpath('__file__'))




class JSON:

	### @about: helper class for getting and parsing JSON data
	
	def fetch (self, method = "strs"):
		### @description: attempt to fetch formatted json from string or file
		### @param: {method} is type {string}
		### @return: is type {string}
		### determine which method to operate
		return self.__method__(method)
	
	def __method__ (self, method):
		### @description: determine method to parse json
		### @param: {method} is type {string}
		### @return: is type {string}
		### format method string to match class function string pattern
		method = String.cconcat(["__", method, "__" ])
		### confirm if self has the method defined within self
		if hasattr(self, method):
			### call found function
			return getattr(self, method)(self.context)
	
	def __strs__ (self, context):
		### @description: attempt to parse json from string
		### @param: {context} is type {string} as type {json}
		### attempt to call json load as string method
		try:
			### return formatted json as dict
			return json.loads(context)
		### handle exception error for failing to load json
		except:
			### return False type for error handling
			return False
	
	def __file__ (self, context):
		### @description: attempt to call json loads as string method
		### @param: {context} is type {string}
		### @return: is type {dictionary} or {boolean:false}
		### attempt to load supplied file instance as context argument
		try:
			### attempt to load string path / file instance
			with open(context) as file:
				### attempt to load file contents as json
				try:
					return json.load(file)
				### handle exception error for failing to parse json
				except:
					### return False type for error handling
					return False
		### handle exception error for failing to open file in context
		except:
			### return False type for error handling
			return False
	
	def __init__ (self, context = '{"example":"json"}'):
		### @description: class constructor
		### set context for fetch attempt 
		self.context = context




class List:

	### @about: helper class for fetching items within list
	
	def fetch (self, **kwargs):
		### @description: fetch index of list item without traceback
		### @param: {index} is type {integer}
		### @return: is type {*}
		### set index reference
		i = kwargs.get("index", 0)
		### attempt to fetch and return list item without error if out of range
		try:
			### return list item
			return self.context[i]
		### handle exception
		except:
			### return empty for possible evaluator
			return []

	def __type__ (self, context):
		### @description: handles context to default to list
		### @param: {context} is {*} expects {list}
		### @return: is type {list}
		### confirm returned
		return context if type(context) is list else []

	def __init__ (self, context = []):
		### @description: class constructor
		### set correct context to be list
		self.context = self.__type__(context)




class String:

	### @about: helper class for formatting prettier strings

	### colour formatting options
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	### regexp for matching "{{string}}"
	REG = r"\{\{(?:[\w\s\d]*|[$&\+,\:\;\=\?@#\|'\<\>\.^\*\(\)%!-\/]*)*\}\}"
	### regexp for matching string.extname
	EXT = r"^.+\.{1}\w+$"
	
	@staticmethod
	def cconcat (strlist, character = ""):
		### @description: concatenate multiple arguments by string character
		### @param: {strlist} is type {list}
		### @character {character} is type {string}
		### @return: is type {string}
		return character.join(filter(None, strlist))
	
	@staticmethod
	def concat (*args):
		### @description: concatenate multiple arguments to a single string seperated by whitespace
		### @param: {args} is type {comma spaced strings}
		### @return: is type {string}
		return " ".join(filter(None, args))
	
	@staticmethod
	def tag (context = ""):
		### @description: wrap string in constructor (or supplied as argument) with formatting syntax ({{context}})
		### @param: {context} is type {string}
		### @return: is type {string}
		### return formatted string
		return String.cconcat(["{{", context, "}}"])
	
	def wrap (self, width = 60):
		### @description: prints a multiple line string with formatting
		### @param: {width} is type {integer}
		### @return: is type {string}
		print '\n'.join(line.strip() for line in re.findall(r'.{1,'+ str(width) +'}(?:\s+|$)', self.__process__()) )
	
	def line (self):
		### @description: prints a single line formatted string
		### @return: is type {string}
		print self.__process__()
	
	def get (self, context = {}):
		### @description: return entire formatted string using supplied styling
		### @param: {context} is type {dictionary}
		### @return: is type {string}
		### fetch returned processed context
		return self.__process__(context)
	
	def __format__ (self, string, attributes = {}):
		### @description: returns substring/string with styling attached
		### @param: {string} is type {string}
		### @param: {attributes} is type {dictionary}
		### @return is type {string}
		### iterate through attribute dict and try to match value to formatting
		if bool(attributes):
			for attribute in attributes:
				### attempt to find matching style from constants
				attr = getattr(self, str.upper(attributes[attribute]), None)
				### confirm if attribute styling found
				if attr:
					### format string with styling
					string = String.cconcat([attr, string, self.END])
		### return formatted string
		return string
	
	def __substitute__ (self, string, attributes = {}):
		### @description: return string with {{}} removed and styling attached
		### @param: {string} is type {string}
		### @param: {attributes} is type {dictionary}
		### @return is type {string}
		### match {{str}} substring
		matches = re.findall(self.REG, string, re.DOTALL)
		### iterate through substrings
		for i in range(0, len(matches)):
			### replace "{{"" or "}}" from substrings
			substring = re.sub(r"{{|}}", "", matches[i])
			### replace matches[i] with dict
			matches[i] = {'original': substring, 'formatted': self.__format__(substring, attributes)}
		### iterate through matches again
		for i in range(0, len(matches)):
			### replace string with formatted text based on items in matches
			string = re.sub(matches[i]['original'], matches[i]['formatted'], string)
		### return string with formatting replacing any "{{" or "}}" that exists in original string
		return re.sub(r"{{|}}", "", string)
	
	def __process__ (self, context = {}):
		### @description: return formatted string or strings depending on config context supplied (list or dict)
		### @param: {attributes} is type {dictionary}
		### @return: is type {string} 
		### check if context isn't a default
		if not bool(context):
			### check if Class was give a constructor dict
			if self.context:
				### use constructor dict
				context = self.context
			else:
				### use a sample instead
				context = [{'str':'{{Sample}}', 'attr':{'color':'cyan'}}, {'str':'{{Text}}', 'attr':{'color':'purple'}}]
		### check if context is either a list or dict
		if type(context) is list:
			### temp list for holding formatted strings
			strs = []
			### iterate through items to be formatted
			for i in range(0, len(context)):
				### append formatted strings to temp list
				strs.append(self.__substitute__(context[i]['str'], context[i]['attr']))
			### return the complete string with formatting
			return String.concat(strs)
		else:
			### return the complete string with formatting
			return self.__substitute__(context['str'], context['attr'])
	
	def __init__ (self, context = {}):
		### @description: class constructor
		### @param: {context} is type {dictionary} or is type {list}
		### set base string context 
		self.context = context




class Lexicon (String):

	### @about: class for creating pseudo randomised sentences from string fragments
	
	def construct (self):
		### @description: creates lexical text
		### @return: is type {string}
		### format context object
		return self.__format__()

	def __lexical__ (self, key, value):
		### @description: creates string from pseudo random selection
		### @param: {key} is type {dictionary}
		### @param: {value} is type {string}
		### @return: is type {string}
		return key[value][random.randrange(len(key[value]))]
	
	def __construct__ (self, context):
		### @description: create formatted string based on LX configuration
		### @param: {context} is type {dictionary}
		### @return: is type {string}
		### obtain random string
		context['formatted'] = self.__lexical__(context['key'], context['value'])
		### format string with colours, weight, underline if attr dictionary 
		if bool(context['attr']):
			### call String class
			context['formatted'] = self.get({'str': String.tag(context['formatted']), 'attr': context['attr']})
		### append string with puncutation
		if bool(context['punctuate']):
			### select from list of punctuation if supplied
			if type(context['punctuate']) is list:
				### obtain random punctuation from list
				context['punctuate'] = self.__lexical__({'t': context['punctuate']}, 't')
			### append punctuation to the formatted string
			context['formatted'] = String.cconcat([context['formatted'], context['punctuate']])
		### return formatted string including optional punctuation
		return context['formatted']

	def __optional__ (self, context):
		### @description: create formatted string if random number generated was not considered a boolean value
		### @param: {context} is type {dictionary}
		### @return: is type {string}
		### confirm if LX dict optional was set as false format string
		if not context['optional']:
			### return formatted string
			return self.__construct__(context)
		else:
			### confirm LX was provided a int or float attempt to run formatting
			if (type(context['optional']) is int) or (type(context['optional']) is float):
				### confirm number returned was equal to zero format string
				if not bool(random.randrange(int(context['optional']))):
					return self.__construct__(context)
		### return empty string if context dict did not pass optional
		return ""
	
	def __process__ (self, context):
		### @description: create lexicon string whether or not it was formatted
		### @param: {context} is type {list} or {dictionary}
		### set temp list for holding processed strings
		processed = []
		### process a single item object
		if not type(context) is list:
			### check if single item was optionally formatted
			processed.append(self.__optional__(context))
		### process multiple objects
		else:
			### iterate over the context object
			for i in range(0, len(context)):
				### check if single item was optionally formatted
				processed.append(self.__optional__(context[i]))
		### return seperated string
		return " ".join(filter(None, processed))
	
	def __type__ (self, context):
		### @description: create formatted instance as dictionary
		### @param: {context} is type {list} or {dict} or {class:Lexicon}
		### @return: is type {dictionary}
		### process objects that are not list type
		if not type(context) is list:
			### process individual item
			if type(context) is dict:	
				### parse dictionary as named arguments to LX class
				context = LX(**context).construct()
			### process items that are instances of classes LX or Lexicon
			elif isinstance(context, LX) or isinstance(context, Lexicon):
				### call class operator to return string or formatted dictionary
				context = context.construct()
		### process items as list
		else:
			### parse list as the key to LX class and return formatted dictionary
			context = LX(key = context).construct()
		### return formatted object
		return context
	
	def __format__ (self):
		### @description: format self to be valid Lexicon data
		### @return is type {dictionary}
		### process single item object
		if not type(self.context) is list:
			### format type object data
			self.context = self.__type__(self.context)
		### process multiple objects
		else:
			### iterate over object
			for i in range(0, len(self.context)):
				### format type object data
				self.context[i] = self.__type__(self.context[i])
		### process formatted data
		return self.__process__(self.context)
	
	def __init__ (self, context = {}):
		### @description: class constructor
		### @param: {context} is type {list} or {dictionary}
		self.context = context




class LX:

	### @about: builds dictionary to assist lexicon in producing a randomised formatted string
	
	def construct (self):
		### @description: create formatted dictionary from self
		### @return: is type {dictionary}
		return self.__dict__
	
	def __format__ (self, key):
		### @description: create format key to be list
		### @param: {key} is type {list} or {class:Lexicon}
		### @return: is type {dictionary}
		### process single supplied object
		if not type(key) is list:
			### convert object type to be string 
			return self.__type__(key)
		else:
			### iterate list supplied as key
			for i in range(0, len(key)):
				### convert object type to be string 
				key[i] = self.__type__(key[i])
			### return valid dictionary object
			return {'t': key }
	
	def __type__ (self, context):
		### @description: create formatted instance as string
		### @param: {context} is type {list} or {class:Lexicon}
		### @return: is type {dictionary}
		### process single object
		if not type(context) is list:
			### check if object is instance of Lexicon
			if isinstance(context, Lexicon):
				### process and return Lexical string
				context = context.construct()
			### return formatted string
			return context
		### process multiple instances
		else:
			### iterate over objects
			for i in range(0, len(context)):
				### check if object is instance of Lexicon
				if isinstance(context[i], Lexicon):
					### process and return Lexical string
					context[i] = context[i].construct()
			### return formatted string
			return context
	
	def __init__ (self, **kwargs):
		### @description: class constructor
		### @param: {key} is type {list} or {class:Lexicon}
		### @param: {value} is type {string}
		### @param: {attr} is type {dictionary}
		### @param: {punctuate} is type {list} or {string}
		### @param: {optional} is type {integer} or {float} or {boolean}
		### set base key for dictionary
		self.key = self.__format__(kwargs.get('key', {}))
		### set base value for dictionary
		self.value = kwargs.get('value', 't')
		### set base attributes for string
		self.attr = kwargs.get('attr', {})
		### set base punctuation for string
		self.punctuate = kwargs.get('punctuate', None)
		### set base optional for string
		self.optional = kwargs.get('optional', False)




class Responder (String):	

	### @about: creates message printed with "system:" prefixed to beginning to simulate two way communication
	
	def response (self, message = "I am totally not a robot!", attr = {}):
		### @description: creates a string (optionally filtered) prefixed by the name of the responder
		### @param: {message} is type {string}
		### @return: is type {string} 
		### return formatted concatenated string
		return String.concat(String.cconcat([self.__name__(), self.seperator]), self.__message__(message, attr))
	
	def __message__ (self, message = "destroy all humans!", attr = {}):
		### @description private method for fetching the formatted string for the message part of robot response
		### @param: {attr} is type {dictionary}
		### @return: is type {string}
		### call inherited class of string to format string
		return self.get({'str': message, 'attr': attr})
	
	def __name__ (self):
		### @description: private method for fetching and formatting the string that defines the robot's name
		### @return: is type {string}
		### encapsulate name of responder in formatting syntax, instantiate to String class
		return self.get({'str': String.tag(self.name), 'attr': self.style})

	def __init__ (self, **kwargs):
		### @description: class constructor
		### set default name for responder in terminal
		self.name = kwargs.get('name', 'system')
		### set default styling for responder in terminal
		self.style = kwargs.get('style', {'style':'underline','weight':'bold'})
		### set default seperator between responder name and its message in terminal
		self.seperator = kwargs.get('seperator', ':')




class Request (String):

	### @about: creates input response system for handling binary user responses
	
	def open (self):
		### @description: method for asking the user to input one of two provided options
		### @return: is type {boolean}
		### prompt user for input returning text submitted or NoneType if empty
		self.response = self.__prompt__()
		### confirm if response was equal to the confirmation string
		if self.response == self.confirm:
			### return true if user input matches the supplied confirm string
			return True
		### confirm if response was equal to the rejection string
		elif self.response == self.reject:
			### return false if the user input matches the supplied reject string
			return False
		### prompt user that the supplied input wasn't considered valid
		else:
			### concatenate string with formatting
			print self.__response__(String.concat("command", self.get({'str': String.tag(str(self.response)), 'attr':{'weight':'bold'}}), "unrecognised"))
			### recall the function
			return self.open()
	
	def __option__ (self):
		### @description: format the strings defining the options available for the user
		### @return: is type {string}
		### return formatted string with the supplied confirmation and rejection choices
		return self.get({'str': String.tag(String.cconcat([self.confirm, self.reject], "/")), 'attr':{'weight':'bold'}})
	
	def __prompt__ (self):
		### @description: prompt the user to input one of the supplied action contexts
		### @return: is type {string} or {None}
		### request the user to input their text
		response = raw_input(self.__response__(String.concat(self.get({'str':self.prompt,'attr':{'weight':'bold'}}), String.cconcat([self.__option__(), " "], ":")))) or None
		### attempt to format the text to a uppercase string for easier comparison
		try:
			### return the uppercase string
			return str.upper(response)
		### handle exception
		except:
			### return NoneType if unsuccessful
			return response
	
	def __response__ (self, string):
		### @description: format a Responder response
		### @param: {string} is type {string}
		### @return: is type {string}
		return self.system.response(string)

	def __init__ (self, **kwargs):
		### @description: class constructor
		### set default response handlers for input command
		self.prompt = kwargs.get("prompt", "please type either")
		### set default response confirmation string
		self.confirm = str.upper(kwargs.get("confirm", "yes"))
		### set default response rejection string
		self.reject = str.upper(kwargs.get("reject", "no"))
		### initialise responder class
		self.system = Responder(**kwargs)




class Set (String):

	### @about: creates prompt system for managing users input to match expected or define value
	
	def open (self):
		### @description: request user to input into terminal
		### @return: is type {string} or {None}
		### confirm request is a single string
		if type(self.request) is str:
			### prompt user for input and return formatted result
			return self.__prompt__(self.request)
		### confirm request is multiple optional
		elif type(self.request) is list:
			### prompt user for input and return formatted result
			return self.__prompt__(String.cconcat(self.request, "/"))

	def __prompt__ (self, prompt):
		### @description: request user to input value into terminal
		### @param: {prompt} is type {string}
		### @return: is type {string} or {None}
		### get response from terminal
		response = self.__input__(self.__sys__(String.concat(String.cconcat([String.concat("please enter", prompt), " "], ":")), False))
		### confirm if returned input was empty or undefined
		if not response:
			### notify user that the required input cannot be empty or None type
			self.__sys__(self.get({'str': "user input cannot be {{NONE}}", 'attr':{'weight':'bold'}}))
			### prompt user to reattempt to declare their input
			if Request(prompt = "try again?").open():
				### recall function
				return self.__prompt__(prompt)
			### if user chose not to re-enter their selection return response handler
			else:
				return None
		### otherwise if user supplied a string compare provided string to possible ptions
		else:
			return self.__test__(response, prompt)

	def __test__ (self, response, prompt):
		### @description: evaluate user string against potential options
		### @param: {response} is type {string}
		### @param: {prompt} is type {string}
		### if request type is a string
		if type(self.request) is str:
			### proceed to confirmation
			return self.__confirm__(response, prompt)
		### if request type is a list of mutliple sections
		elif type(self.request) is list:
			### iterate over list of options within supplied list
			for i in range(0, len(self.request)):
				### remove formatting from listed string
				match_string = re.sub(r"{{|}}", "", self.request[i])
				### compare if the supplied string is equal to the options within the list
				if str.upper(match_string) == str.upper(response):
					### if match is found proceed to confirmation
					return self.__confirm__(match_string, prompt)
			### if no match occurred notify user that their input wasn't found
			self.__sys__(self.concat("user input", self.get({'str': self.tag(str.upper(response)), 'attr':{'weight':'bold'}}), "did not match", prompt))
			### prompt user to reattempt selection
			if Request(prompt = "try again?").open():
				### recall user input handler
				return self.__prompt__(prompt)
			### if user selected to not continue return response handler
			else:
				return None

	### confirm if the provided input was the correct selection
	def __confirm__ (self, response, prompt):
		### prompt user to confirm their inputted text
		self.__sys__(self.concat("is", self.get({'str': self.tag(response), 'attr': {'weight': 'bold'}}), "the correct input for", self.cconcat([self.get({'str':self.response, 'attr':{'weight':'bold'}}), " "], "?") ))
		### if user selected to keep input
		if Request().open():
			### return response handler
			return response
		### if user opted to not keep input
		else:
			### prompt user to change input
			if Request(prompt = "try again?").open():
				### recall user input handler
				return self.__prompt__(prompt)
			### if user did not choose to change input
			else:
				### return response handler
				return None

	def __input__ (self, prompt):
		### @description: print input for user in terminal
		### @param: {prompt} is type {string}
		### @return: is type {string} or {None}
		### prompt user to input string
		return raw_input(str(prompt)) or None

	def __sys__ (self, message, printed = True):
		### @description: return message and optionally print as system to terminal
		### @param: {message} is type {string}
		### @param: {printed} is type {boolean}
		### format string with formatting if required
		message = self.system.response(self.get({'str':message, 'attr': {'weight':'bold'}}))
		### print string 
		if printed:
			print message
		### return string
		return message

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @param: {request} is type {string} or {list}{string}
		### @param: {response} is type {string}
		### set request string context for user input e.g: "please enter the value you wish to confirm"
		self.request = kwargs.get('request', "{{sample}} for response")
		### set the confirmation for response to user after context e.g: "is the value x correct?"
		self.response = kwargs.get('response', "{{sample}}")
		### initialise responder
		self.system = Responder(**kwargs)




class HTTP:

	### @about: helper class to construct http request

	### default HTTP request method
	DEFAULT_TYPE = "POST"
	### default HTTP request header content-type
	DEFAULT_CONTENT_TYPE = "APPLICATION/JSON"

	def send (self):
		### @description: dispatches HTTP request
		### @return: is type {}
		### set base copy of self definitions
		kwargs = self.__dict__.copy()
		### discard unwanted key word arguments for requests.request method
		map(kwargs.pop, ["request_url", "request_type"])
		### set base request
		r = requests
		### attempt http dispatch
		r.request(self.request_type, self.request_url, **kwargs)
		### return request
		return r

	def __headers__ (self, **kwargs):
		### @description: set HTTP headers for request
		### @param: {headers} is type {list} or {dictionary}
		### @return: is type {dictionary}
		### set base content type for headers 
		content = {'Content-Type': self.__content__(kwargs.pop('content_type', self.DEFAULT_CONTENT_TYPE))}
		### set headers to contain type of content if not supplied
		headers = kwargs.get("headers", {})
		### append headers if headers argument does not contain defined content-type
		return dict(headers, **content) if not 'Content-Type' in headers else header

	def __content__ (self, content = None):
		### @description: set HTTP Content-Type header request type
		### @param: {content} is type {string}
		### @return: is type {string}
		### confirm content is not NoneType
		if bool(content):
			### set base content types for HTTP request headers
			types = ["application/json", "text/html", "text/plain", "application/x-www-form-urlencoded"]
			### enumerate over length of types of content request headers
			for i in range(0, len(types)):
				### confirm supplied type matches supported
				if types[i].upper() == content.upper():
					### return set type
					return types[i]
		### return set default
		return self.DEFAULT_CONTENT_TYPE.lower()

	def __type__ (self, content = None):
		### @description: set http request type
		### @param: {content} is type {string}
		### @return: is type {string}
		### confirm content is not NoneType
		if bool(content):
			### set base request types
			types = ["get", "post", "put", "delete", "head", "options", "patch"]
			### enumerate over length of types of content request headers
			for i in range(0, len(types)):
				### confirm supplied type matches supported
				if types[i].upper() == content.upper():
					### return set type
					return types[i]
		### return defined default
		return self.DEFAULT_TYPE.lower()

	def __json__ (self, **kwargs):
		### @description: set formatted request body
		### @param: {kwargs} is type {dictionary}
		### @return: is type {dictionary} or {string}
		return json.dumps(kwargs) if "__json__" in kwargs and bool(kwargs["__json__"]) else kwargs

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @param: {request_url} is type {string}
		### @param: {request_type} is type {string}
		### @param: {proxies} is type {dictionary}
		### @param: {query} is type {dictionary}
		### @param: {timeout} is type {integer} or {float}
		### @param: {verify} is type {boolean}
		### @param: {stream} is type {boolean}
		### @param: {allow_redirects} is type {boolean}
		### @param: {cert} is type {string}
		### @param: {data} is type {dictionary} or {string}
		### @param: {json} is type {dictionary} or {string}
		### @param: {headers} is type {dictionary}
		### @param: {contentType} is type {string}
		### set base url for http connection
		self.request_url = kwargs.pop("url", "https://{{example}}.com/{{api}}{{endpoint}}") 
		### set base method for http connection
		self.request_type = self.__type__(kwargs.pop("type", None))
		### set base proxies for http connection
		self.proxies = kwargs.pop("proxies", {})
		### set base query string for http url
		self.params = kwargs.pop("query", {})
		### set base timeout for http request
		self.timeout = kwargs.pop("timeout", None)
		### set base veritifcation for http request
		self.verify = kwargs.pop("verify", True)
		### set base response processing method for http request response
		self.stream = kwargs.pop("stream", False)
		### set base redirection usage for http request server handler
		self.allow_redirects = kwargs.pop("allow_redirects", False)
		### set base certificate for http request
		self.cert = kwargs.pop("cert", None)
		### set base request body for http request
		self.data = self.__json__(**kwargs.pop("data", { "__json__": True }))
		### set base request body for http request
		self.json = self.__json__(**kwargs.pop("json", {}))
		### set base headers for http request
		self.headers = self.__headers__(**kwargs)




class HipChat:

	### @about: helper class to format url to connect to HipChat API endpoint

	### default HipChat subdomain
	DEFAULT_SUBDOMAIN = "{{subdomain}}"
	### default HipChat API version
	DEFAULT_VERSION = 2
	### default HipChat room ID
	DEFAULT_ROOM = "{{00000}}"
	### default HipCHat API endpoint
	DEFAULT_API = "{{sample/api}}"

	def URL (self):
		### @description: constructs formatted string for HipChat API requests
		return String.cconcat([String.cconcat([String.cconcat(["https://", self.subdomain]), "hipchat", "com"], "."), "/", String.cconcat(["v", str(self.version)]), "/", "room", "/", self.room, "/", self.api])

	def __init__ (self, **kwargs):
		### set base subdomain for HipChat API
		self.subdomain = kwargs.get("subdomain", self.DEFAULT_SUBDOMAIN)
		### set base version for HipChat API
		self.version = kwargs.get("version", self.DEFAULT_VERSION)
		### set base room for HipChat API
		self.room = kwargs.get("room", self.DEFAULT_ROOM)
		### set base endpoint for HipChat API
		self.api = kwargs.get("api", self.DEFAULT_API)


if __name__ == "__main__":

	print String({"str":"lel", "attr":{}}).get()

	#HTTP(url = HipChat(subdomain = None, version = 2, room = None, api = "notification").URL(), query = { "auth_token": None }, data = { "color": "green", "message": "Sample Text", "notify": "false", "message_format": "text", "__json__": True }).send()

