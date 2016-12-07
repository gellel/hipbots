#!/usr/bin/python
# -*- coding: utf-8 -*-
#sys.argv[1:]

###################################
### python scripts dependencies ###
###################################
### import json
import json
### import system
import sys
### import os
import os
### import regular expressions
import re
### set root folder path
sys.path.append('../../')
### import pretty strings
from lib.strings import String
### import random sentences
from lib.sentence import Sentence
### import HipChat REST
from lib.api import REST
### import http requests
from lib.http import HTTP
### import files
from lib.file import File


if __name__ == '__main__':

	

	print String.Pretty(tag = True)

