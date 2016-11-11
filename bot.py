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
	### concatenate multiple arguments by string character
	@staticmethod
	def cconcat (strlist, character = ""):
		return character.join(filter(None, strlist))
	### concatenate multiple arguments to a single string
	@staticmethod
	def concat (*args):
		return " ".join(filter(None, args))
	### wrap string in constructor with formatting syntax
	def tag (self, context = None):
		if context is None:
			if self.context:
				context = self.context
		return self.cconcat(["{{", context, "}}"])
	### prints a multiple line string with formatting
	def wrap (self, width = 60):
		print '\n'.join(line.strip() for line in re.findall(r'.{1,'+ str(width) +'}(?:\s+|$)', self.__process__()) )
	### prints a single line formatted string
	def line (self):
		print self.__process__()
	### return entire formatted string using supplied styling
	def get (self, context = {}):
		### fetch returned processed context
		return self.__process__(context)
	### return substring/string with styling attached
	def __format__ (self, string, attributes):
		### iterate through attribute dict and try to match value to formatting
		for attribute in attributes:
			attr = getattr(self, str.upper(attributes[attribute]), None)
			if attr:
				string = attr + string + self.END
		### return formatted string
		return string
	### return string with {{}} removed and styling attached
	def __substitute__ (self, string, attributes = {}):
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
	### return formatted string or strings depending on config context supplied (list or dict)
	def __process__ (self, context = {}):
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
	### return the type of the context
	def __type__ (self):
		return type(self.context)
	### return the context supplied
	def __self__ (self):
		return self.context
	### constructor 
	def __init__ (self, context = {}):
		self.context = context



class OAuth:


	def params (self):
		### set query string for authorisation
		return { "auth_token": self.auth }

	def type (self):
		### set content type from supplied
		return { "Content-Type": self.type }

	def url (self):
		### concatenate strs to produce complete request URL
		return String.cconcat([String.cconcat([String.cconcat(["https://", self.organisation]), "hipchat", "com"], "."), "/", self.version, "/", "room", "/", self.id, "/notification"])
	### constructor
	def __init__ (self, **kwargs):
		self.organisation = kwargs.get("organisation", "{{SUB_NAME}}")
		self.id = kwargs.get("id", "{{ROOM_ID}}")
		self.version = kwargs.get("version", "{{API_VERSION}}")
		self.auth = kwargs.get("auth", "{{AUTH_TOKEN}}")
		self.type = kwargs.get("type", "application/json")


class Card:
	### set config value
	def __value__ (self, **kwargs):
		### @param {url} is type {string}
		### @param {style} is type {string}
		### @param {label} is type {string}
		return { "url": kwargs.get("url", "https://www.google/{{value}}"), "style": kwargs.get("style", "lozenge-complete"), "label": kwargs.get("label", "Google label") }
	### set config icon
	def __icon__ (self, **kwargs):
		### @params {url} is type {string}
		### @params {url@2x} is type {string}
		return { "url": kwargs.get("url", self.DEFAULT_IMG), "url@2x": kwargs.get("url@2x", self.DEFAULT_IMG)}
	### set description
	def __desc__ (self, **kwargs):
		### @params {format} is type {string}
		### @params {value} is type {string}
		return { "format": kwargs.get("format", "html"), "value": kwargs.get("value", "this is a <strong>HTML</strong> description") }
	### set config thumbail 
	def __thumbnail__ (self, **kwargs):
		### @params {url} is type {string}
		### @params {width} is type {integer} or {string}
		### @params {height} is type {integer} or {string}
		return { "url": kwargs.get("url", self.DEFAULT_IMG), "width": kwargs.get("width", 500), "height": kwargs.get("height", 500) }
	### set config activity
	def __activity__ (self, **kwargs):
		### @params {html} is type {string}
		### @params {icon} is type {dict}
		return { "html": kwargs.get("html", "<strong>activity<strong> HTML"), "icon": self.__icon__(**kwargs.get("icon", {})) }
	### set config attributes
	def __attributes__ (self, **kwargs):
		### @param {value} is type {dict}
		### @param {icon} is type {dict}
		### @param {label} is type {string}
		return { "value": self.__value__(**kwargs.get("value", {})), "icon": self.__icon__(**kwargs.get("icon", {})), "label": kwargs.get("label", "attributes label") }
	### constructor
	def __init__ (self, **kwargs):
		### @params {id} is {integer}
		### @params {description} is type {dict}
		### @params {format} is type {string}
		### @params {url} is type {string}
		### @params {title} is type {string}
		### @params {thumbail} is type {dict}
		### @params {activity} is type {dict}
		### @params {attributes} is type {dict}
		### set base id 
		self.id = kwargs.get("id", 1)
		### set base icon
		self.icon = self.__icon__(**kwargs.get("icon", {}))
		### set description key dict 
		self.description = self.__desc__(**kwargs.get("description", {}))
		### set base format size for card
		self.format = kwargs.get("format", "medium")
		### set primary click-out url
		self.url = kwargs.get("url", "https://www.google.com/")
		### set card title
		self.title = kwargs.get("title", "Search on Google")
		### set card thumnail image
		self.thumbnail = self.__thumbnail__(**kwargs.get("thumbnail", {}))
		### set card activity operation
		self.activity = self.__activity__(**kwargs.get("activity", {}))
		### set card attributes
		self.attributes = self.__attributes__(**kwargs.get("attributes", {}))
		### set card default image
		self.DEFAULT_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2000px-Google_%22G%22_Logo.svg.png"




class Config:
	### create card object 
	def __card__ (self, **kwargs):
		### confirm that kwarg was set as undefined handler
		if 'f' in kwargs and not bool(kwargs['f']):
			return {}
		### build card
		return Card(**kwargs).create()
	### constructor
	def __init__ (self, **kwargs):
		### @params {message_format} is type {string}
		### @params {color} is type {string}
		### @params {attach_to} is type {integer?}
		### @params {notify} is type {string}
		### @params {message} is type {string}
		### @params {card} is type {dict}
		### determines how the message is treated by our server and rendered inside HipChat applications
		self.message_format = kwargs.get("message_format", "html")
		### background color for message
		self.color = kwargs.get("color", "random")
		### the message id to to attach this notification to, for example if this notification is in response to a particular message. for supported clients, this will display the notification in the context of the referenced message specified by attach_to parameter. if this is not possible to attach the notification, it will be rendered as an unattached notification. the message must be in the same room as that the notification is sent to
		self.attach_to = kwargs.get("attach_to", None)
		### whether this message should trigger a user notification (change the tab color, play a sound, notify mobile phones, etc). each recipient's notification preferences are taken into account
		self.notify = kwargs.get("notify", "false")
		### the message body for notification
		self.message = kwargs.get("message", "This is a test message.")
		### set an optional card object 
		self.card = self.__card__(**kwargs.get("card", {'f':False}))


class Request:

	def __init__ (self, **kwargs):
		pass



if __name__ == '__main__':
	
	print 

"""

https://answers.atlassian.com/questions/33156779/how-to-post-a-card-using-hipchat-api

class OAUTH:
	
	def __url__ (self, subdomain = '{{EXAMPLE}}'):
		return String.cconcat(["https://", subdomain, "hipchat", "com"], ".")

	def __init__ (self, **kwargs):
		self.url = self.__url__(kwargs.get("subdomain", "{{EXAMPLE}}"))
		self.version = self.__ 
"""
