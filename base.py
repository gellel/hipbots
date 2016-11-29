#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################


class Base:

	def __str (self, arg):
		### @description: private function to handle None arguments to string
		### @parameter: <arg>, @type: <*>, @default: <None>
		### @return: @type: <str>

		# set base string
		return str(arg) if type(arg) in [int, float, unicode, str] else ''



if __name__ == '__main__':

	# display base operations
	print dir(Base)