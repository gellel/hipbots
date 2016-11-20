#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### py requests class package
import requests
### py json classp package
import json




class HTTP:

	###########################################################
	### creates http requests through building helper class ###
	###########################################################

	def create (self, trim = []):
		### @description: protected method to dispatch HTTP request
		### @parameter: trim, @type: <list>
		### @return: <class:requests>

		# set filtered for request method
		t = ["url", "type"]
		# merge filter trim if provided
		t = t + trim if type(trim) is list else []
		# set duplicate of self attributes as dict
		kwargs = self.__dict__.copy()
		# filter kwargs to prevent kwargs error
		map(kwargs.pop, t)
		# set base request
		r = requests
		# attempt http dispatch
		r.request(self.type, self.url, **kwargs)
		# return result of request
		return r

	def __content (self, content = None):
		### @description: private method to set HTTP Content-Type header request type
		### @parameter: content, @type: <string>
		### @return: <string>

		# confirm content is not NoneType
		if bool(content):
			# set base content types for HTTP request headers
			types = ["APPLICATION/JSON", "TEXT/HTML", "TEXT/PLAIN", "APPLICATION/X-WWW-FORM-URLENCODED"]
			# initialise loop to process available http content types
			for i in range(0, len(types)):
				# confirm supplied type matches supported
				if types[i].upper() == content.upper():
					### return set type
					return types[i]
		# return default http header type
		return "APPLICATION/JSON"

	def __headers (self, **kwargs):
		### @description: private method to set HTTP headers for HTTP request
		### @parameters: headers, @type <list> @or <dict>
		### @return: <dict>

		# set base content type for HTTP headers 
		content = {'Content-Type': self.__content(kwargs.pop('content', None))}
		# set headers to contain HTTP request type of content if not supplied
		headers = kwargs.get("headers", {})
		# append headers if headers argument does not contain defined content-type
		return dict(headers, **content) if not 'Content-Type' in headers else header

	def __type (self, content = None):
		### @description: private method for setting http request type
		### @parameter: content, @type <string>
		### @return: <string>

		# confirm content is not NoneType
		if bool(content):
			# set base request types
			types = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"]
			# initialise loop to process available http types
			for i in range(0, len(types)):
				# confirm supplied type matches supported
				if types[i].upper() == content.upper():
					# return set type
					return types[i]
		# return default http method
		return "GET"

	def __json (self, **kwargs):
		### @description: private method for converting http request body to json string
		### @parameter: kwargs, @type <dict>
		### @return: @type <dict> @or <string>

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

		# set url attribute; @default: <string>
		self.url = kwargs.pop("url", "https://{{example}}.com/{{api}}{{endpoint}}") 
		# set http type attribute; @default: <None>
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
		# set http body attribute; @default: <dict>
		self.data = self.__json(**kwargs.pop("body", { "__json__": True }))
		# set http headers attribute; @default: <dict>
		self.headers = self.__headers(**kwargs)



if __name__ == '__main__':

	# create example http request wrapper
	print HTTP(url = "https://www.google.com/", type = "GET").create()