#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import pretty strings
from strings import String
### import system
import sys
### import os
import os
### import regular expressions
import re


class File (String):

	####################################################
	### class for finding, opening and writing files ###
	####################################################

	@staticmethod
	def Close (file = None):
		### @description: public function of class, closes file instance
		### @return: @type: <bool>

		# set default file instance
		# @parameter: <file>, @type: <file>, @default: <None>
		file = file if hasattr(file, 'close') else None

		# attempt to close file instance
		return not bool(file.close()) if file is not None else False

	@staticmethod
	def Create (name = 'SAMPLE', extension = 'txt', directory = None, method = 'r+'):
		### @description: public function of class, creates new file of specified type if not found on drive otherwise opens existing
		### @return: @type: <file>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory)
		# set default file open method string
		# @parameter: <method>, @type: <str>, @default: <str>
		method = File.SetStringType(method)

		# confirm file directory exists and within directory file does not exists

		# attempt to create new file in specified directory or open file
		return open(os.path.join(File.Directory(directory), File.Cconcat([name, '.', extension])), 'w+') if File.Directory(directory) and not File.Exists(name = name, extension = extension, directory = directory) else File.Open(name = name, extension = extension, directory = directory)

	@staticmethod
	def Delete (file = None, name = 'SAMPLE', extension = 'txt', directory = None):
		### @description: public function of class, finds file and removes from system
		### @return: @type: <bool>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory)
		# set default file instance
		# @parameter: <file>, @type: <file>, @default: <None>
		file = file if hasattr(file, 'read') else File.Open(name = name, extension = extension, directory = directory, method = 'r')

		# find file instance and delete from operating system if exists
		return not bool(os.remove(File.Directory(file = file))) if file is not None else False

	@staticmethod
	def Directory (file = None):
		### @description: public function of class, finds current directory of file or python environment
		### @return: @type: <str>

		# set default file instance and find file path
		# @parameter: <file>, @type: <str/file>, @default: <None>
		file = file if type(file) is str and os.path.exists(file) else getattr(file, 'name', os.path.dirname(os.path.realpath('__file__')))
			
		# set path for file or directory
		return file

	@staticmethod
	def Exists (name = 'SAMPLE', extension = 'txt', directory = None):
		### @description: public function of class, finds file using string
		### @return: @type: <str>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory) if bool(directory) else os.path.dirname(os.path.realpath('__file__'))

		# confirm file exists in supplied or relative directory
		return True if os.path.exists(os.path.join(File.Directory(directory), File.Cconcat([name, '.', extension]))) or os.path.exists(os.path.join(File.Directory(), File.Cconcat([name, '.', extension]))) else False

	@staticmethod
	def Open (name = 'SAMPLE', extension = 'txt', directory = None, method = 'r+'):
		### @description: public function of class, opens file from relative or supplied directory
		### @return: @type: <file/None>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.Path(name = name, extension = extension, directory = directory)
		# set default file open method string
		# @parameter: <method>, @type: <str>, @default: <str>
		method = File.SetStringType(method)

		# confirm file exists on system and open file if found 
		return open(os.path.join(directory, File.Cconcat([name, '.', extension])), method) if File.Exists(name, extension, directory) else None

	@staticmethod
	def Path (name = 'SAMPLE', extension = 'txt', directory = None):
		### @description: public function of class, sets path string if found using relative or supplied
		### @return: @type: <str>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory)

		# set supplied directory prefixed file
		specified = os.path.join(directory, File.Cconcat([name, '.', extension]))
		# set relative directory prefixed file
		relative = os.path.join(File.Directory(), File.Cconcat([name, '.', extension]))

		# confirm user directory path exists
		if os.path.exists(specified):
			# set file path as user path
			return directory
		# confirm relative direct file exists
		if os.path.exists(relative):
			# set file path as relative path
			return File.Directory()
		# set path as empty
		return ''

	@staticmethod
	def Read (file = None, name = 'SAMPLE', extension = 'txt', directory = None, seeker = 0, method = 'r+'):
		### @description: public function of class, finds file and reads contents at position
		### @return: @type: <str>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory)
		# set default file seeker position 
		# @parameter: <seeker>, @type: <int>, @default: <int>
		seeker = int(seeker) if not type(seeker) in [float, int, str, unicode] else 0
		# set default file open method string
		# @parameter: <method>, @type: <str>, @default: <str>
		method = File.SetStringType(method)
		# set default file instance
		# @parameter: <file>, @type: <file>, @default: <None>
		file = file if hasattr(file, 'read') else File.Open(name = name, extension = extension, directory = directory, method = method)

		# confirm file is not none
		if file is not None:
			# set cursor position for file
			file.seek(seeker)
		# read content of file if file is not none set content as empty
		return file.read() if file is not None else ''

	@staticmethod
	def Write (file = None, name = 'SAMPLE', extension = 'txt', directory = None, method = 'r+', content = None):
		### @description: public function of class, finds file and writes content at position
		### @return: @type: <bool>

		# set default file name string
		# @parameter: <name>, @type: <str>, @default: <str>
		name = File.SetStringType(name)
		# set default file extension string
		# @parameter: <extension>, @type: <str>, @default: <str>
		extension = File.SetStringType(extension)
		# set default file directory string
		# @parameter: <directory>, @type: <str>, @default: <None>
		directory = File.SetStringType(directory)
		# set default file open method string
		# @parameter: <method>, @type: <str>, @default: <str>
		method = File.SetStringType(method)
		# set default file content string
		# @parameter: <content>, @type: <str>, @default: <str>
		content = File.SetStringType(content)
		# set default file instance
		# @parameter: <file>, @type: <file>, @default: <None>
		file = file if hasattr(file, 'write') else File.Open(name = name, extension = extension, directory = directory, method = method)

		# confirm file is not none and content is not an empty or none type structure and write to file
		return not file.write('HELLO') if file is not None and bool(content) else False



if __name__ == '__main__':

	# read self
	print File.Read(name = 'file', extension = 'py')
