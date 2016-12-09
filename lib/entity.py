#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import personas
from persona import Persona


class Entity (Persona):

	###########################################################################################################
	### extended class of persona.Persona, creates input prompts using the Persona class to prefix requests ###
	###########################################################################################################

	def ask (self, *args, **kwargs):
		### @description: protected function of class, prompts user for input but uses the persona prefix to simulate a system or character requesting an action
		### @return: @type: <str>

		# set default argument list
		# @parameter: <args>, @type: <tuple>, @default: <list>
		args = filter(None, list(args or [{'string':'a', 'tag': True}, {'string':'b', 'tag': True}, '{{c}}']))
		# set default request prompt string
		# @parameter: <kwarg:user_request>, @type: <str/dict>, @default: <str>
		user_request = kwargs.get('user_request', 'please enter your desired input selection.')
		# set default confirm input prompt string
		# @parameter: <kwarg:user_confirm>, @type: <str/dict>, @default: <str>
		user_confirm = kwargs.get('user_confirm', 'is selection {{%s}} the correct choice?')
		# set default reject input string
		# @parameter: <kwarg:user_reject>, @type: <str/dict>, @default: <str>
		user_reject = kwargs.get('user_reject', 'input {{%s}} is not an accepted selection.')
		# set default null input string
		# @parameter: <kwarg:user_null>, @type: <str/dict>, @default: <str>
		user_null = kwargs.get('user_null', 'empty')
		# set default user accept string
		# @parameter: <kwarg:user_accept>, @type: <str/dict>, @default: <dict>
		user_accept = kwargs.get('user_accept', {'string':'yes', 'tag': True})
		# set default user reject string
		# @parameter: <kwarg:user_decline>, @type: <str>, @default: <str>
		user_decline = kwargs.get('user_decline', 'no')
		# set default character to separate selection options
		# @parameter: <kwarg:selection_divider>, @type: <str>, @default: <str>
		selection_divider = kwargs.get('selection_divider', '/')
		# set default character to separate user input from request string
		# @parameter: <kwarg:input_divider>, @type: <str>, @default: <str>
		input_divider = kwargs.get('input_divider', ':')
		
		# manage user responses
		return self.__manage(user_choices = args, user_request = user_request, user_confirm = user_confirm, user_reject = user_reject, user_null = user_null, user_accept = user_accept, user_decline = user_decline, selection_divider = selection_divider, input_divider = input_divider)

	def __manage (self, **kwargs):
		### @description: private function for class, manages the pairing of user input in against the allowed responses
		### @return: @type: <str>
		
		# request input submission from user
		submission = self.__prompt(kwargs.get('user_choices'), kwargs.get('user_request'), kwargs.get('selection_divider'), kwargs.get('input_divider'), kwargs.get('user_null'))
		# confirm user submission matches supplied options
		if self.__test(submission, kwargs.get('user_choices')):
			# accept user submission or request input again
			return submission if self.__select(submission, **kwargs) else self.__manage(**kwargs)
		# request user submit accepted input using String.SetStringDict to set requirements for String.Pretty
		print super(Entity, self).say(super(Entity, self).Pretty(**super(Entity, self).SetStringDict(kwargs.get('user_reject') % submission)))
		# request user input
		return self.__manage(**kwargs)	

	def __select (self, submission, **kwargs):
		### @description: private function for class, confirms whether selected input from manage was the intended choice
		### @return: @type: <bool>

		# set default accept input string
		# @parameter: <kwarg:user_accept>, @type: <str>, @default: <str>
		user_accept = super(Entity, self).Clean(kwargs.get('user_accept')['string'] if type(kwargs.get('user_accept')) is dict else kwargs.get('user_accept'))
		# set default decline input string
		# @parameter: <kwarg:user_accept>, @type: <str>, @default: <str>
		user_decline = super(Entity, self).Clean(kwargs.get('user_decline')['string'] if type(kwargs.get('user_decline')) is dict else kwargs.get('user_decline'))

		# request confirmation input submission from user using String.SetStringDict to set requirements for String.Pretty
		confirmation = self.__prompt([kwargs.get('user_accept'), kwargs.get('user_decline')], super(Entity, self).Pretty(**super(Entity, self).SetStringDict(kwargs.get('user_confirm') % submission)), kwargs.get('selection_divider'), kwargs.get('input_divider'), kwargs.get('user_null'))
		# confirm user submission matches supplied options
		if self.__test(confirmation, [user_accept, user_decline]):
			# confirm outcome
			return True if confirmation == user_accept else False
		# request user submit accepted input using inherited Persona.Say to produce formatted printed message
		print super(Entity, self).say(super(Entity, self).Pretty(**super(Entity, self).SetStringDict(kwargs.get('user_reject') % confirmation)))
		# request user input
		return self.__select(submission, **kwargs)

	def __test (self, submission = 'sample', options = ['1', '2', '3']):
		### @description: private function for class, evaluates user input submission against defined option to confirm a match
		### @return: @type: <bool>

		# set default submission string
		# @parameter: <submission>, @type: <str>, @default: <str>
		submission = super(Entity, self).SetStringType(submission).lower()
		# set default option strings using String.Clean 
		# @parameter: <options>, @type: <list>, @default: <list>
		options = [super(Entity, self).Clean(option['string'] if type(option) is dict else option).lower() for option in list(options)]

		# set test result
		return True if submission in options else False
	
	def __prompt (self, choices, request, selection_divider, input_divider, empty):
		### @description: private function for class, creates beautified prompt string including persona prefix
		### @return: @type: <str>

		# set default request string using String.SetStringDict to set requirements for String.Pretty
		# @parameter: <request>, @type: <str>, @default: <str>
		request = super(Entity, self).Pretty(**super(Entity, self).SetStringDict(request))
		# set default beautified options using String.SetStringDict to set requirements for String.Pretty
		# @parameter: <choices>, @type: <list>, @default: <list>
		choices = [super(Entity, self).Pretty(**super(Entity, self).SetStringDict(i)) for i in choices]
		# set default selection divider string
		# @parameter: <selection_divider>, @type: <str>, @default: <str>
		selection_divider = super(Entity, self).SetStringType(selection_divider)
		# set default input divider string
		# @parameter: <input_divider>, @type: <str>, @default: <str>
		input_divider = super(Entity, self).SetStringType(input_divider)
		# set default empty input string using String.SetStringDict to set requirements for String.Pretty
		# @parameter: <request>, @type: <str>, @default: <str>
		empty = super(Entity, self).Pretty(**super(Entity, self).SetStringDict(empty))

		# request user input response using Persona.Say
		return raw_input(super(Entity, self).say(request, super(Entity, self).Cconcat([super(Entity, self).Cconcat(choices, selection_divider), input_divider, " "]))) or empty

	def __init__ (self, **kwargs):
		### @description: class constructor

		# set default attribute requirements for Persona from key word arguments
		# @parameter: <kwargs:name>, @type: <str>, @default: <str>

		# set default break from name to output
		# @parameter: <kwargs:separator> @type: <str>, @default: <str>

		# set default style attributes for name
		# @parameter: <kwargs:style>, @type: <list>, @default: <list>
		super(Entity, self).__init__(**kwargs)




if __name__ == '__main__':

	# example entity ask
	print Entity().ask()
	