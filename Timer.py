# -*-coding: utf-8 -*-

import os, sys, time
"""
Продвинутый таймер.
Для подключения к модулю Kassa. 
"""
class Timer():
	TIME=10
	SLEEP=1
	GO_BACK=True
	BEEP=False
	BEEPS=3
	NO_SYGNAL=False
	def __init__(self):
		pass
	def timer(self,tm=TIME, slp=SLEEP, goback=GO_BACK, beep=BEEP, beeps=BEEPS):
		for i in range(int(tm)+1):
			if goback:
				print "--> %s" %(int(tm)-i),  '\r',
				sys.stdout.flush()
				time.sleep(slp)
				if beep and (int(tm)-i)<beeps :
					print "\a",
			elif not goback:
				print "--> %s" %(i),'\r',
				sys.stdout.flush()
				time.sleep(slp)

class Progress():
	def __init__(self):
		curent = 5
		total = 10
		max_width = 10
		
	def progress_bar(cur=5,total=10,max_width=10):
		#cur*max_width/total
		#[=====     ] 50%
		# _____ - cur
		#      _____ - total-cur
		smb = "="
		smb_ = " "
		print '[' + smb*(cur*max_width/total) + smb_*(max_width - cur*max_width/total) + ']',