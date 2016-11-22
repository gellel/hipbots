#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### py requests class package
import requests
### py json class package
import json
### py regex class package
import re




class HTTP:

	###########################################################
	### creates HTTP requests through building helper class ###
	###########################################################

	def create (self, trim = []):
		### @description: protected method to dispatch HTTP request
		### @parameter: trim, @type: <list>
		### @returns: <class:requests>

		# set filtered for request method
		t = ["url", "type"]
		# merge filter trim if provided
		t = t + trim if type(trim) is list else []
		# set duplicate of self attributes as dict
		kwargs = self.__dict__.copy()
		# filter kwargs to prevent kwargs error
		map(kwargs.pop, t)
		# attempt HTTP dispatch
		r = requests.request(self.type.lower(), self.url.lower(), **kwargs)
		# return result of request
		return r

	def __content (self, content = None):
		### @description: private method to set HTTP Content-Type header request type
		### @parameter: content, @type: <string>
		### @returns: <string>

		# confirm content is not NoneType
		if bool(content):
			# set base content types for HTTP request headers
			types = ["APPLICATION/JSON", "TEXT/HTML", "TEXT/PLAIN", "APPLICATION/X-WWW-FORM-URLENCODED"]
			# initialise loop to process available HTTP content types
			for i in range(0, len(types)):
				# confirm supplied type matches supported
				if types[i].upper() == content.upper():
					### return set type
					return types[i]
		# return default HTTP header type
		return "APPLICATION/JSON"

	def __headers (self, **kwargs):
		### @description: private method to set HTTP headers for HTTP request
		### @parameters: headers, @type: <list> @or <dict>
		### @returns: <dict>

		# set base content type for HTTP headers 
		content = {'Content-Type': self.__content(kwargs.pop('content', None))}
		# set headers to contain HTTP request type of content if not supplied
		headers = kwargs.get("headers", {})
		# append headers if headers argument does not contain defined content-type
		return dict(headers, **content) if not 'Content-Type' in headers else headers

	def __url (self, url = None):
		### @description: private method to format urls
		### @parameter: url, @type: <string>
		### @returns: <string>

		# confirm variable type is string and if it matches HTTP(s)://*
		return url if type(url) is str and re.compile(r'HTTPs?:\/\/.+', re.IGNORECASE).match(url) else "HTTPs://{{example}}.com/{{api}}{{endpoint}}"
		
	def __type (self, content = None):
		### @description: private method for setting HTTP request type
		### @parameter: content, @type: <string>
		### @returns: <string>

		# confirm content is not NoneType
		if bool(content):
			# set base request types
			types = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
			# initialise loop to process available HTTP types
			for i in range(0, len(types)):
				# confirm supplied type matches supported
				if types[i].upper() == content.upper():
					# return set type
					return types[i]
		# return default HTTP method
		return "GET"

	def __json (self, **kwargs):
		### @description: private method for converting HTTP request body to json string
		### @parameter: kwargs, @type <dict>
		### @returns: @type <dict> @or <string>

		# confirm stringified json data type is required or return dict
		return json.dumps(kwargs) if "__json__" in kwargs and bool(kwargs["__json__"]) else kwargs

	def __init__ (self, **kwargs):
		### @description: class constructor
		### @parameter: url, @type <string>
		### @parameter: type, @type <string>
		### @parameter: proxies, @type <dict>
		### @parameter: query, @type <dict>
		### @parameter: timeout, @type <integer> @or <float>
		### @parameter: verify, @type <bool>
		### @parameter: stream, @type <bool>
		### @parameter: redirects, @type <bool>
		### @parameter: certificate, @type <string>
		### @parameter: body, @type <dict> or <string>
		### @parameter: headers, @type <dict>
		### @parameter: content, @type <string>

		# set url attribute; @default: <None>
		self.url = self.__url(kwargs.pop("url", None)) 
		# set HTTP type attribute; @default: <None>
		self.type = self.__type(kwargs.pop("type", None))
		# set proxies attribute; @default: <dict>
		self.proxies = kwargs.pop("proxies", {})
		# set query string attribute; @default: <dict>
		self.params = kwargs.pop("query", {})
		# set request timeout attribute; @default: <None>
		self.timeout = kwargs.pop("timeout", None)
		# set vertification attribute; @default: <None>
		self.verify = kwargs.pop("verify", True)
		# set stream response attribute; @default: <False>
		self.stream = kwargs.pop("stream", False)
		# set redirection attribute; @default: <False>
		self.allow_redirects = kwargs.pop("redirects", False)
		# set certificate attribute; @default: <None>
		self.cert = kwargs.pop("cert", None)
		# set HTTP body attribute; @default: <dict>
		self.data = self.__json(**kwargs.pop("body", { "__json__": True }))
		# set HTTP headers attribute; @default: <dict>
		self.headers = self.__headers(**kwargs)




if __name__ == '__main__':

	# create example HTTP request wrapper
	print HTTP(url = "https://en.wikipedia.org/w/api.php", type = "GET", query = { "format": "json", "action": "query", "prop": "extracts", "exintro": "", "explaintext": "", "titles": "Elizabeth_II" }, redirects = True).create()
	