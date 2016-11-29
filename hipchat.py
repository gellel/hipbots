#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################

class HTML:

	ELEMENTS = ['A', 'B', 'I', 'STRONG', 'EM', 'BR', 'IMG', 'PRE', 'CODE', 'OL', 'UL', 'LI', 'TABLE', 'TR', 'TD', 'TH', 'TF', 'SPAN']
	ATTRIBUTES = {'A':['HREF','REL','DATA-TARGET','DATA-TARGET-OPTIONS'], 'IMG':['SRC','ALT','WIDTH','HEIGHT','ALIGN','STYLE'],'TD':['COLSPAN','ROWSPAN','VALIGN'],'TR':['VALIGN'],'TH':['COLSPAN','ROWSPAN','VALIGN'],'SPAN':['STYLE']}


	@staticmethod
	def confirm ():
		pass

	@staticmethod
	def element (arg):
		### @description: confirms HTML tag supported in HipChat
		pass

	@staticmethod
	def attributes (arg):
		### @description: confirms HTML attribute supported in HipChat
		pass



class REST:

	###################################################
	### public class to construct REST API endpoint ###
	###################################################

	@staticmethod
	def default (**kwargs):
		### @description: public function to select suitable substitute from allowed
		### @parameters: <kwargs>, @type: <dict>
		### @return: @type: <dict>

		# set base request
		request = kwargs.get('request', None)
		# confirm request 






if __name__ == '__main__':
	
	pass
