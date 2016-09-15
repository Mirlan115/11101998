from random import randint
print "ugadai chislo kotoroe ya zagadayu"
print "vvedi predel chisel"
print "Za pravilnyi otvet 5 ballov"
n = int (raw_input (">"))
x= randint (1,5)
logic = 0
popitka = 5
while (logic != 1):
	
	print "vvedite chislo"
	inp = int (raw_input(">"))
	if x==inp:
		print "ty vuigral", "s" "popitka"
		logic = 1
	else :
		
		print "game over"
		popitka + 5
		print 
