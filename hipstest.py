#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import html strings
from html import HTML


class Messages (String, HTML):
	pass




if __name__ == '__main__':

	print dir(Messages)
