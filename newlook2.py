#-*-coding:utf-8 -*-
import os, time, sys

DIR_FORMAT="%d%m%y"
TITLE_FORMAT="%d.%m.%Y"

TODAY=time.strftime(DIR_FORMAT)

#TODO
# нужно указать пользователя
# иначе не будет работать
USERNAME=""

WORK_PATH=""
BACKUP_PATH=""
UPDATE_PATH=""

class Interactiv(object):
	"""docstring for Interactiv"""
	def __init__(self, arg):
		super(Interactiv, self).__init__()
		self.arg = arg
		self.commands=

	def command(self, ps=">", mode="None"):
		#TODO: preparsing raw_input
		return raw_input(" "+ps)
	def com_parser(self, com):
		if com == "": print "No command"

		else print "Bad command"