#-*- coding: utf-8 -*-
import os,  time,  sys,  thread

#constants:
DEBUG = True
#show more messages
VERBOSE=False
#default current directory
WORK_DIR = "./"
#backup dir 
BACKUP_DIR = "./backup"
#current work dir ddmmYY
CURRENT_DIR = time.strftime("%d%m%y")
WORKDIR = "C:\workshop"
SERVPATH = u"\\Serv\\документы"

#title for Windows cmd
TITLE = time.strftime("%d.%m.%Y")
#show notifications
SHOW_NOTIFY=True

abc = "abcdefghijklmnopqrstuvwxyz"
num = "01234567890"
smb = """`-=[];'\,./~!@#$%^&*()_+{}:"|<>?"""

#try do it simple!!! and refactoring code

#TODO: update this and 

#try TODO: logging
#and passwording :)

# LOG_FILE = CURRENT_DIR+".txt"
# def log(filename = LOG_FILE):
	# lfile = open(LOG_FILE, "wb")
	# lfile.write("write in "+str(time.time()))
	# lfile.close()

#try key signal
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
		
#ch = _Getch()

#ok 
#and why?


	
def test_platform():
    #sys.platform == linux2 - for linux
    #sys.platform == win32 - for windows
    if sys.platform == 'linux2':
        if DEBUG and VERBOSE: print "Linux machine"
        return "lin"
    elif sys.platform == 'win32':
        if DEBUG and VERBOSE: print "Windows machine"
        return "win"
    else:
        if DEBUG and VERBOSE: print "Other machine"
        return "x3"


def set_color(col="0a"):
	os.system("color "+col)
	##how colorize any symbol
		
def test_dir():
	if os.path.abspath("./") != WORKDIR:
		try:
			os.chdir(WORKDIR)
		except:
			os.mkdir(r"c:\workshop")
			os.chdir(WORKDIR)
		else:
			print "Problem whith directory!"			
	if CURRENT_DIR in os.listdir('./'):
		print "Directory is present."
		return 1
	else:
		print "Try create work directory."
		os.mkdir(CURRENT_DIR)
		if CURRENT_DIR in os.listdir('./'):
			os.chdir(CURRENT_DIR)
			return 1
		return 0


def set_title():
    if test_platform() == "win":
        try:
            os.system("title "+TITLE)
        except:
            if DEBUG and VERBOSE: print "OH, SHIT!"
        # finally:
            # if DEBUG and VERBOSE:
                # print "Ok, don't touch anything!"
                # print "OK?"
    else:
        pass

def cls():
    if test_platform() =="win":
        os.system("cls")
    elif test_platform() == "lin":
        os.system("clear")
    else:
        if DEBUG and VERBOSE: print "OH, SHIT!"
        return -1

def diskount(price,  percent=0,  rounded=False):
    if percent > 100:
        if DEBUG and VERBOSE: print "Are you sure?"
        percent = 100
    elif percent < 0:
        if DEBUG and VERBOSE: print "Are you sure?"
        percent = 0
    if rounded:
        return round(price*(100-percent)/100.)
    elif not rounded:
        return price*(100-percent)/100.
    

def prc(percent=5):
    price =0
    summ=0
    disk =0
    rdisk = 0
    print "Percent = %"+str(percent),  "Enter to exit."
    while(1):
        price = raw_input(': ')
        if price in abc+smb+"":
            print "Summ:", summ,  "\tDisk:",  disk,  "\tRDisk:",  rdisk
            print "SMax:",  (max(disk,  rdisk)), "Diff:",  (rdisk-disk),  "rub."
            return
        else:
            try:
                summ += float(price)
                disk += float(diskount(float(price),  percent))
                rdisk += float(diskount(float(price),  percent, True))
            except:
                print "Input Error! Only number or ENTER to exit!"
            else:
                print "\t",  diskount(float(price),  percent), "\t",  diskount(float(price),  percent,  True)

def note(self, message=""):
    if message == "":
        message = "Мне нечего сказать."
    n = pynotify.Notification("Server:",  message)
    n.show()

def test_coding():
    message = "Проверка кодировки.\nВыставьте желаемую кодировку вручную."
    #print message.decode("ibm866"),  "cp866 - for DOS"
    #print message.decode("cp1251"),  "cp1251 - for Windows"
    print message.decode("utf-8"),  "utf-8 - You are lucky!"
    #print message

class Timer:
    def __init__(self):
        self.def_time =10
        self.def_sleep = 1
        self.go_back = True
        self.get_bell = False
        self.bells = 3
        self.in_thread = False
        self.see_out = True
        self.see_message = DEBUG
        
    def start(self):
        for times in range (self.def_time+1):
            if not self.go_back:
                pass
            elif self.go_back:
                pass
            time.sleep(self.def_sleep)
        if self.see_message:
            if VERBOSE:
                print "OK"
    

if __name__ == "__main__":
	if SHOW_NOTIFY and test_platform()=="lin":
		try:
			import pynotify
		except:
			print "Can't import notifications!"
	if test_platform()=="win":
		set_title()
		set_color()
		test_dir()
		#попробуем открыть все это
		try:
			os.system("explorer "+WORKDIR+"\\"+CURRENT_DIR)
			#а это пока не стоит открывать
			#os.system("explorer "+SERVPATH.decode("utf-8"))
			
		except:
			print r"Can't open work directory or \\Serv\документы!"
			time.sleep(5)
	cls()