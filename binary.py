BnumStr = input("binary number to convert to decimal\n")[::-1]
Bnum = list(BnumStr)
Bnum = map(int, Bnum)
x = 0
Dnum = 0
for num in Bnum:
	Tnum = 0
	Tnum = num * 2**x
	x = x + 1
	Dnum = Dnum + Tnum
print("The decimal equivalent of ", BnumStr[::-1], "is ", Dnum)
