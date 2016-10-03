import msvcrt
def test_char():
	ch = 0
	while (1):
		ch = msvcrt.getch()
		if ch == "q":
			print ch+":"+hex(ch),
			ch = msvcrt.getch()
			if ch == "q": return
		print ch+":"+hex(ch),
		
	