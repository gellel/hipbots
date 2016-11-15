#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### py subprocess class package
import subprocess
### py requests class package
import requests
### py random class package
import random
### py json class package
import json
### py pwd class package
import pwd
### py system class package
import sys
### py os class package
import os
### py regex
import re

### script exe base file directory
__FILEPATH__ = os.path.dirname(os.path.realpath('__file__'))


### HELP FILES FROM HIPCHAT
### https://www.hipchat.com/docs/apiv2/method/send_room_notification




class JSON:
	
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
	
	def tag (self, context = None):
		### @description: wrap string in constructor (or supplied as argument) with formatting syntax ({{context}})
		### @param: {context} is type {string}
		### @return: is type {string}
		### confirm context not supplied
		if not context and self.context:
			### set base string
			context = self.context
		### return formatted string
		return self.cconcat(["{{", context, "}}"])
	
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
	
	def __format__ (self, string, attributes):
		### @description: returns substring/string with styling attached
		### @param: {string} is type {string}
		### @param: {attributes} is type {dictionary}
		### @return is type {string}
		### iterate through attribute dict and try to match value to formatting
		for attribute in attributes:
			### attempt to find matching style from constants
			attr = getattr(self, str.upper(attributes[attribute]), None)
			### confirm if attribute styling found
			if attr:
				### format string with styling
				string = self.cconcat([attr, string, self.END])
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
			return self.concat(strs)
		else:
			### return the complete string with formatting
			return self.__substitute__(context['str'], context['attr'])
	
	def __type__ (self):
		### @description: confirm the type of the context (for multiple formatted strings of single string)
		### @return: is type {string}
		return type(self.context)
	
	def __init__ (self, context = {}):
		### @description: class constructor
		### @param: {context} is type {dictionary} or is type {list}
		### set base string context 
		self.context = context




class Responder (String):	
	
	def response (self, message = "I am totally not a robot!", attr = {}):
		### @description: creates a string (optionally filtered) prefixed by the name of the responder
		### @param: {message} is type {string}
		### @return: is type {string} 
		### return formatted concatenated string
		return self.concat(self.cconcat([self.__name__(), self.seperator]), self.__message__(message, attr))
	
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
		return self.get({'str': self.tag(self.name), 'attr': self.style})

	def __init__ (self, **kwargs):
		### @description: class constructor
		### set default name for responder in terminal
		self.name = kwargs.get('name', 'system')
		### set default styling for responder in terminal
		self.style = kwargs.get('style', {'style':'underline','weight':'bold'})
		### set default seperator between responder name and its message in terminal
		self.seperator = kwargs.get('seperator', ':')




class Request (String):
	
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
			print self.__response__(self.concat("command", self.get({'str': self.tag(str(self.response)), 'attr':{'weight':'bold'}}), "unrecognised"))
			### recall the function
			return self.open()
	
	def __option__ (self):
		### @description: format the strings defining the options available for the user
		### @return: is type {string}
		### return formatted string with the supplied confirmation and rejection choices
		return self.get({'str': self.tag(self.cconcat([self.confirm, self.reject], "/")), 'attr':{'weight':'bold'}})
	
	def __prompt__ (self):
		### @description: prompt the user to input one of the supplied action contexts
		### @return: is type {string} or {None}
		### request the user to input their text
		response = raw_input(self.__response__(self.concat(self.get({'str':self.prompt,'attr':{'weight':'bold'}}), self.cconcat([self.__option__(), " "], ":")))) or None
		### attempt to format the text to a uppercase string for easier comparison
		try:
			### return the uppercase string
			return str.upper(response)
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
		self.confirm = str.upper(kwargs.pop("confirm", "yes"))
		### set default response rejection string
		self.reject = str.upper(kwargs.pop("reject", "no"))
		### initialise responder class
		self.system = Responder(name = kwargs.get('name', None), style = kwargs.get('style', None), seperator = kwargs.get('seperator', None))




class Set (String):
	
	def open (self):
		### @description: create dictionary with returned response and boolean
		### @return: is type {dictionary}
		### check if supplied request a string
		if type(self.request) is str:
			### format string to request for single entity type
			self.request_string = self.request
		### check if supplied request is a list
		elif type(self.request) is list:			
			### format message as a multiple option choice
			### concatenate request string
			self.request_string = self.cconcat(self.request, "/")
		else:
			### return response handler
			return {'bool': False, 'response': None}
		### prompt user to input the requested type
		return self.__prompt__()
	
	def __compare__ (self):
		### @description: evaluate user string against potential options
		### @return: is type {dictionary}
		### if request type is a string
		if type(self.request) is str:
			### proceed to confirmation
			return self.__confirm__()
		### if request type is a list of mutliple sections
		elif type(self.request) is list:
			### iterate over list of options within supplied list
			for i in range(0, len(self.request)):
				### remove formatting from listed string
				match_string = re.sub(r"{{|}}", "", self.request[i])
				### compare if the supplied string is equal to the options within the list
				if str.upper(match_string) == str.upper(self.user):
					### if match is found proceed to confirmation
					return self.__confirm__(match_string)
			### if no match occurred notify user that their input wasn't found
			self.__sys__(self.concat("user input", self.get({'str': self.tag(str.upper(self.user)), 'attr':{'weight':'bold'}}), "did not match", self.request_string))
			### prompt user to reattempt selection
			if Request(prompt = "try again?").open():
				### recall user input handler
				return self.__prompt__()
			### if user selected to not continue
			else:
				### return response handler
				return {'bool': False, 'response': None}
	
	def __confirm__ (self, response = None):
		### @description: confirm if the provided input was the correct selection
		### @param: {response} is type {string}
		### @return: is type {dictionary}
		### if string was not provided to function
		if not response:
			### set response string as the user string provided in single option conformation
			response = self.user
		### prompt user to confirm their inputted text
		self.__sys__(self.concat("is", self.get({'str': self.tag(response), 'attr': {'weight': 'bold'}}), "the correct input for", self.cconcat([self.get({'str':self.response, 'attr':{'weight':'bold'}}), " "], "?") ))
		### if user selected to keep input
		if Request().open():
			### return response handler
			return {'bool': True, 'response': response}
		### if user opted to not keep input
		else:
			### prompt user to change input
			if Request(prompt = "try again?").open():
				### recall user input handler
				return self.__prompt__()
			### if user did not choose to change input
			else:
				### return response handler
				return {'bool': False, 'response': None}
	
	def __prompt__ (self):
		### @description: prompts user to input their desired value for setter class
		### @return: is type {dictionary}	
		### print message asking user to input their desired value for the supplied options
		self.user = self.__input__(self.__sys__(self.concat(self.cconcat([self.concat(self.request_string), " "], ":")), False))
		### if returned input was empty or undefined
		if not self.user:
			### notify user that the required input cannot be empty or None type
			self.__sys__(self.get({'str': "user input cannot be {{NONE}}", 'attr':{'weight':'bold'}}))
			### prompt user to reattempt to declare their input
			if Request(prompt = "try again?").open():
				### recall function
				return self.__prompt__()
			### if user chose not to re-enter their selection
			else:
				### return response handler
				return {'bool': False, 'response': None}
		### if user supplied a string
		else:
			### compare provided string to possible ptions
			return self.__compare__()
	
	def __input__ (self, string):
		### @description: collects input from user
		### @return: is type {string} or {None}
		### prompt user to input string
		return raw_input(str(string)) or None
	
	def __sys__ (self, message, printed = True):
		### @description: returns string or prints the message as system to terminal 
		### @param: {message} is type {string} and is optional; defaults to {None}
		### @param: {printed} is type {boolean}
		### @return: is type {string} or {None}
		### format string with formatting if required
		message = self.system.response(self.get({'str':message, 'attr': {'weight':'bold'}}))
		### print string 
		if printed:
			print message
		### return string
		return message

	def __init__ (self, **kwargs):
		### @description: class constructor
		### set request string context for user input e.g: "please enter the value you wish to confirm"
		self.request = kwargs.get('request', None)
		### set the confirmation for response to user after context e.g: "is the value x correct?"
		self.response = kwargs.get('response', None)
		### initialise responder
		self.system = Responder(name = kwargs.get('name', None), style = kwargs.get('style', None), seperator = kwargs.get('seperator', None))




class HipChatOAuth:

	def AUTH_QUERY (self):
		### @description: sets query string for HTTP request
		### @return: is type {dictionary}
		### set query string for authorisation
		return { "auth_token": self.auth }

	def AUTH_TYPE (self):
		### @description: sets HTTP request header from self type
		### @return: is type {dictionary}
		### set content type from supplied
		return { "Content-Type": self.type }

	def AUTH_URL (self):
		### @description: construct base url for oauth request
		### @return: is type {string}
		### concatenate strs to produce complete request URL
		return String.cconcat([String.cconcat([String.cconcat(["https://", self.subdomain]), "hipchat", "com"], "."), "/", self.version, "/", "room", "/", self.id, "/notification"])

	def __init__ (self, **kwargs):
		### @description: class constructor
		### set sub domain for request string
		self.subdomain = kwargs.get("subdomain", "{{SUB_DOMAIN}}")
		### set room id for message delivery
		self.id = kwargs.get("id", "{{ROOM_ID}}")
		### set HipChat API version
		self.version = kwargs.get("version", "{{API_VERSION}}")
		### set oauth token supplied from HipChat
		self.auth = kwargs.get("auth", "{{AUTH_TOKEN}}")
		### set request type to HipChat server (default is json)
		self.type = kwargs.get("type", "application/json")




class HipChatCard:
	
	def value (self, **kwargs):
		### @description: sets keys and values for attributes object
		### @param {url} is type {string}
		### @param {style} is type {string}
		### @param {label} is type {string}
		### @return: is type {dictionary}
		return { "url": kwargs.get("url", "https://{{ATTRIBUTES_VALUE_URL}}"), "style": kwargs.get("style", "lozenge-complete"), "label": kwargs.get("label", "{{attributes}}{{label}}") }

	def icon (self, **kwargs):
		### @description: sets keys and values for icon object; can be shared for object:attributes, object:activity
		### @params {url} is type {string}
		### @params {url@2x} is type {string}
		### @return: is type {dictionary}
		return { "url": kwargs.get("url", "{{DEFAULT_ICON}}.png"), "url@2x": kwargs.get("url@2x", "{{RETINA_ICON}}.png")}

	def description (self, **kwargs):
		### @description: sets keys and values for description object
		### @params {format} is type {string}
		### @params {value} is type {string}
		### @return: is type {dictionary}
		return { "format": kwargs.get("format", "html"), "value": kwargs.get("value", "<strong>{{EXAMPLE DESCRIPTION}}</strong>") }

	def thumbnail (self, **kwargs):
		### @description: sets thumbail image for card
		### @params {url} is type {string}
		### @params {width} is type {integer} or {string}
		### @params {height} is type {integer} or {string}
		### @return: is type {dictionary}
		return { "url": kwargs.get("url", "{{DEFAULT_THUMBNAIL}}.png"), "width": kwargs.get("width", 200), "height": kwargs.get("height", 200) }

	def activity (self, **kwargs):
		### @description: sets key values for attributes object; shares icon config function
		### @params {html} is type {string}
		### @params {icon} is type {dict}
		### @return: is type {dictionary}
		return { "html": kwargs.get("html", "<em>{{EXAMPLE ACTIVTITY}}<em>"), "icon": self.icon(**kwargs.get("icon", {})) }

	def attributes (self, **kwargs):
		### @description: sets key values for attributes object
		### @param {value} is type {dict}
		### @param {icon} is type {dict}
		### @param {label} is type {string}
		### @return: is type {dictionary}
		return { "value": self.value(**kwargs.get("value", {})), "icon": self.icon(**kwargs.get("icon", {})), "label": kwargs.get("label", "{{EXAMPLE_ATTRIBUTES_LABEL}}") }

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @params {id} is {integer}
		### @params {description} is type {dict}
		### @params {format} is type {string}
		### @params {url} is type {string}
		### @params {title} is type {string}
		### @params {thumbail} is type {dict}
		### @params {activity} is type {dict}
		### @params {attributes} is type {dict}
		### set base id 
		self.id = kwargs.get("id", None)
		### set base icon
		self.icon = self.icon(**kwargs.get("icon", {}))
		### set description key dict 
		self.description = self.description(**kwargs.get("description", {}))
		### set base format size for card
		self.format = kwargs.get("format", "medium")
		### set primary click-out url
		self.url = kwargs.get("url", "https://{{EXAMPLE_SITE_URL}}.com/")
		### set card title
		self.title = kwargs.get("title", "{{EXAMPLE_TITLE}}")
		### set card thumnail image
		self.thumbnail = self.thumbnail(**kwargs.get("thumbnail", {}))
		### set card activity operation
		self.activity = self.activity(**kwargs.get("activity", {}))
		### set card attributes
		self.attributes = self.attributes(**kwargs.get("attributes", {}))




class HipChatPost:

	def construct (self, response_data = "json"):
		### @description: creates formatted body for HTTP request to hipchat
		### @param: {response_data} is type {string}
		### @return: is type {string}
		### confirm type of data to be sent
		if response_data == "json" or response_data == "application/json":
			## set empty dictionary to contain fixed
			j = {}
			### iterate over self dict
			for i in self.__dict__:
				### confirm valid value
				if bool(self.__dict__[i]):
					### update new dict
					j.update({i: self.__dict__[i]})
			### return complete
			return json.dumps(j)
		### return default HTML
		return self.HTML 

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @params {message_format} is type {string}
		### @params {color} is type {string}
		### @params {attach_to} is type {integer?}
		### @params {notify} is type {string}
		### @params {message} is type {string}
		### @params {card} is type {dict}
		### determines how the message is treated by our server and rendered inside HipChat applications
		self.message_format = kwargs.get("message_format", "text")		
		### background color for message
		self.color = kwargs.get("color", "random")
		### the message id to to attach this notification to, for example if this notification is in response to a particular message. for supported clients, this will display the notification in the context of the referenced message specified by attach_to parameter. if this is not possible to attach the notification, it will be rendered as an unattached notification. the message must be in the same room as that the notification is sent to
		self.attach_to = kwargs.get("attach_to", None)
		### whether this message should trigger a user notification (change the tab color, play a sound, notify mobile phones, etc). each recipient's notification preferences are taken into account
		self.notify = kwargs.get("notify", "false")
		### the message body for notification
		self.message = kwargs.get("message", "Sample Text")
		### set an optional card object 
		self.card = kwargs.get("card", {})
		### set HTML if supplied 
		self.HTML = kwargs.get("HTML", "<strong>HTML</strong>")



if __name__ == '__main__':

	oauth = HipChatOAuth(subdomain = "{{HIDDEN}}", id = "{{HIDDEN}}", version = "v2", auth = "{{HIDDEN}}", type = "application/json")
	
	r = requests.post(oauth.AUTH_URL(), data = HipChatPost(message = "hello world.").construct(), headers = oauth.AUTH_TYPE(), params = oauth.AUTH_QUERY())

	print Responder().response()
