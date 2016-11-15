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


class String:
	### formatting options
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



class OAuth:

	
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


class Card:
	
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



class Config:

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

	oauth = OAuth(subdomain = "{{HIDDEN}}", id = "{{HIDDEN}}", version = "v2", auth = "{{HIDDEN}}", type = "application/json")
	
	r = requests.post(oauth.AUTH_URL(), data = Config(message = "hello world.").construct(), headers = oauth.AUTH_TYPE(), params = oauth.AUTH_QUERY())

