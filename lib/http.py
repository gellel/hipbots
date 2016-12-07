#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import http requests
import requests
### import json
import json
### import regular expressions
import re


class HTTP (String):

	######################################################################
	### extended class of strings.String, used to create HTTP requests ###
	######################################################################

	def HTTP (self):
		### @description: protected function of class, creates HTTP request using requests.request
		### @return: @type: <instance:requests>

		# set function arguments for requests.request HTTP handler
		parameters = self.__dict__
		# dispatch HTTP request using requests.request library, passing defined attributes of class as key word arguments
		return requests.request(self.method.lower(), self.URL.lower(), **{ key: parameters[key] for key in parameters if key not in ['URL', 'method'] })
			
	def __url (self, url = ''):
		### @description: private function of class, formats supplied url string to contain request protocol substring
		### @return: @type: <str>

		# set default http url string using String.SetStringType
		# @parameter: <url>, @type: <str>, @default: <str>
		url = super(HTTP, self).SetStringType(url)

		# set formatted http url to contain protocol substring if missing and use String.Cconcat to join fragments
		return url if re.compile(r'HTTPs?:\/\/.+', re.IGNORECASE).match(url) else super(HTTP, self).Cconcat(['https://', url])
		
	def __http (self, method = ''):
		### @description: private function of class, sets default HTTP request method for HTTP request
		### @return: @type: <str>

		# set default HTTP method string using String.SetStringType
		# @parameter: <method>, @type: <str>, @default: <str>
		method = super(HTTP, self).SetStringType(method)

		# confirm HTTP method exists in selections otherwise default to GET
		return method.upper() if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH'] else 'GET'

	def __json (self, data = {}):
		### @description: private function of class, sets dictionary argument to JSON string
		### @return: @type: <str/dict>

		# set default data dictionary
		# @parameter: <data>, @type: <dict>, @default: <dict>
		data = data if bool(data) else { '__json__': True }

		# stringify json if data type is dictionary and __json__ key set to dictionary
		return json.dumps({ key: data[key] for key in data if not key in ['__json__'] }) if '__json__' in data and bool(data['__json__']) else data

	def __headers (self, **kwargs):
		### @description: private function of class, sets required HTTP headers for HTTP request
		### @return: @type: <dict>

		# set default content-type HTTP header
		# @parameter: <kwargs:Content-Type>, @type: <dict>, @default: <dict>
		content = kwargs.get('Content-Type', {'Content-Type': 'application/json'})

		# set default content-type
		return dict(kwargs, **{'Content-Type': 'application/json'}) if not content in kwargs or content.upper() not in ['APPLICATION/JSON', 'APPLICATION/X-WWW-FORM-URLENCODED', 'TEXT/HTML', 'TEXT/PLAIN'] else kwargs

	def __init__ (self, **kwargs):
		### @descrption: class constructor

		# set default url attribute using String.SetStringType
		# @parameter: <kwargs:URL>, @type: <str>, @default: <None>
		self.URL = self.__url(super(HTTP, self).SetStringType(kwargs.get('URL', None))) 
		# set default HTTP method type
		# @parameter: <kwargs:method>, @type: <str>, @default: <None>
		self.method = self.__http(super(HTTP, self).SetStringType(kwargs.get('method', None)))
		# set default HTTP data attribute
		# @parameter: <kwargs:name>, @type: <dict>, @default: <dict>
		self.data = self.__json(kwargs.get('data', { '__json__': True }))
		# set default HTTP headers attribute
		# @parameter: <kwargs:headers>, @type: <dict>, @default: <dict>
		self.headers = self.__headers(**kwargs.get('headers', {}))
		# set default proxies attribute
		# @parameter: <kwargs:proxies>, @type: <str>, @default: <dict>
		self.proxies = kwargs.get('proxies', {})
		# set default query string attribute
		# @parameter: <kwargs:query>, @type: <str>, @default: <dict>
		self.params = kwargs.get('query', {})
		# set default request timeout attribute
		# @parameter: <kwargs:timeout>, @type: <str>, @default: <None>
		self.timeout = kwargs.get('timeout', None)
		# set default vertification attribute
		# @parameter: <kwargs:verify>, @type: <str>, @default: <True>
		self.verify = kwargs.get('verify', True)
		# set default stream response attribute
		# @parameter: <kwargs:stream>, @type: <str>, @default: <False>
		self.stream = kwargs.get('stream', False)
		# set default redirection attribute
		# @parameter: <kwargs:redirects>, @type: <str>, @default: <None>
		self.allow_redirects = kwargs.get('redirects', False)
		# set default certificate attribute
		# @parameter: <kwargs:certificate>, @type: <str>, @default: <None>
		self.cert = kwargs.get('certificate', None)




if __name__ == '__main__':

	# create example HTTP request wrapper
	print HTTP(URL = "https://en.wikipedia.org/w/api.php", method = "GET", headers = {'Content-Type':'application/json'}, query = { "format": "json", "action": "query", "prop": "extracts", "exintro": "", "explaintext": "", "titles": "Elizabeth_II" }, redirects = True).HTTP().content
	