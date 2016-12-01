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



class HTTP:

	###########################################################
	### creates HTTP requests through building helper class ###
	###########################################################

	def create (self):
		### @description: protected function for dispatching HTTP request
		### @return: @type: <instance:requests>

		# set base kwargs for requests function
		kwargs = self.__dict__.copy()
		# remove unexpected keys
		map(kwargs.pop, ['URL', 'method'])
		# set base request
		r = requests.request(self.method.lower(), self.URL.lower(), **kwargs)
		# send result
		return r
		
	def __URL (self, URL = ''):
		### @description: private function for setting HTTP URL
		### @parameter: <URL>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# set base HTTP URL
		return URL if re.compile(r'HTTPs?:\/\/.+', re.IGNORECASE).match(URL) else 'https://en.wikipedia.org/w/api.php'
		
	def __HTTP (self, method = ''):
		### @description: private function for setting HTTP request method
		### @parameter: <method>, @type: <str>, @default: <str>
		### @return: @type: <str>

		# set base HTTP method
		return method.upper() if method.upper() in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH'] else 'GET'

	def __JSON (self, arg = {}):
		### @description: private function to stringify dictionary to JSON string
		### @parameter: <arg>, @type <dict>, @default: <dict>
		### @return: @type: <str/dict>

		# stringify dictionary if key json exists
		return json.dumps(arg) if '__json__' in arg and bool(arg['__json__']) else arg

	def __HEAD (self, **kwargs):
		### @description: private function to set HTTP minimum headers for request
		### @parameter: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base content-type
		return dict(kwargs, **{'Content-Type':'application/json'}) if not kwargs.get('Content-Type') in kwargs or kwargs.get('Content-Type', '').upper() not in ['APPLICATION/JSON', 'APPLICATION/X-WWW-FORM-URLENCODED', 'TEXT/HTML', 'TEXT/PLAIN'] else kwargs

	def __init__ (self, **kwargs):
		### @descrption: class constructor
		### @parameters: <kwargs>, @type: <dict>

		# set base url attribute
		# @parameter: <URL>, @type: <str>, @default: <None>
		self.URL = self.__URL(String.SetStrType(kwargs.pop('URL'))) 
		# set base HTTP method type
		# @parameter: <method>, @type: <str>, @default: <None>
		self.method = self.__HTTP(String.SetStrType(kwargs.pop('method')))
		# set base HTTP body attribute
		# @parameter: <name>, @type: <dict>, @default: <dict>
		self.data = self.__JSON(kwargs.pop('body', { '__json__': True }))
		# set base HTTP headers attribute
		# @parameter: <headers>, @type: <dict>, @default: <dict>
		self.headers = self.__HEAD(**kwargs.get('headers', {}))
		# set base proxies attribute
		# @parameter: <name>, @type: <str>, @default: <dict>
		self.proxies = kwargs.pop('proxies', {})
		# set base query string attribute
		# @parameter: <name>, @type: <str>, @default: <dict>
		self.params = kwargs.pop('query', {})
		# set base request timeout attribute
		# @parameter: <name>, @type: <str>, @default: <None>
		self.timeout = kwargs.pop('timeout', None)
		# set base vertification attribute
		# @parameter: <name>, @type: <str>, @default: <True>
		self.verify = kwargs.pop('verify', True)
		# set base stream response attribute
		# @parameter: <name>, @type: <str>, @default: <False>
		self.stream = kwargs.pop('stream', False)
		# set base redirection attribute
		# @parameter: <name>, @type: <str>, @default: <None>
		self.allow_redirects = kwargs.pop('redirects', False)
		# set base certificate attribute
		# @parameter: <name>, @type: <str>, @default: <None>
		self.cert = kwargs.pop('cert', None)




if __name__ == '__main__':

	# create example HTTP request wrapper
	print HTTP(URL = "https://en.wikipedia.org/w/api.php", method = "GET", headers = {'Content-Type':'fake'}, query = { "format": "json", "action": "query", "prop": "extracts", "exintro": "", "explaintext": "", "titles": "Elizabeth_II" }, redirects = True).create().content
	