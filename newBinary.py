#Converts binary to decimal
import math

# Functions
def main():
	'''
	main() is the primary function for the program
	It questions the user and uses match-case to determine which function to implement
	'''
		
	decision = int(input('Would you like to convert:\n1. Decimal to Binary\n2. Binary to Decimal\n3. Binary Fraction to Decimal\nPlease input 1, 2, or 3: '))
#	decision = int(decision)
	# Validate input

	match decision:
		# Decimal to binary conversion
		case 1:
			# Request input and convert it to float
			convNum = float(input('What decimal number would you like to convert to binary? \nNumber to convert: '))
			newNum = toBinary(convNum)
			print(f'{convNum} in binary is {newNum}')

		# Binary to Decimal conversion
		case 2:
			BnumStr = input('Binary number to convert to Decimal\n')[::-1]
			Bnum = list(BnumStr)
			Bnum = map(int, Bnum)
			x = 0
			Dnum = 0
			for num in Bnum:
				Tnum = 0
				Tnum = num * 2**x
				x = x + 1
				Dnum = Dnum + Tnum
			print('The decimal equivalent of ', BnumStr[::-1], 'is ', Dnum)

		# Binary fraction to Decimal conversion
		case 3:
			BFStr = input('Binary fraction number to convert to Decimal fraction\n')
			BFNum = float(BFStr)
			BFList = math.modf(BFNum)
			FracBinTup = BFList[0]
			WholBinTup = BFList[1]

			# Whole Binary number conversion to decimal
			WholBinStr = str(WholBinTup)
			splitWholBin = WholBinStr.split('.')
			cleanWholBin = str(splitWholBin[0])[::-1]
			listWholBin = list(cleanWholBin)
			listWholBin = map(int, listWholBin)
			a = 0
			WholDec = 0
			for num in listWholBin:
				TempNum = 0
				TempNum = num * 2**a
				a = a + 1
				WholDec = WholDec + TempNum

			FracBinStr = str(FracBinTup)
			splitFracBin = FracBinStr.split('.')
			cleanFracBin = str(splitFracBin[1])
			listFracBin = list(cleanFracBin)
			listFracBin = map(int, listFracBin[:8])
			b = -1
			FracDec = 0.0
			for num in listFracBin:
				TemNum = 0
				TemNum = num * 2**b
				b = b - 1
				FracDec = FracDec + TemNum
			FracDec = str(FracDec)
			splitFracDec = FracDec.split('.')
			cleanFracDec = splitFracDec[1]
			print('The Decimal equivalent of ', BFStr, ' is ', str(WholDec) + '.' + cleanFracDec)
		# Catch all inappropriate input
		case _:
			print(f'{decision} is not a choice please restart the program.')


def cleanStr(dirtyNum, fracWhole):
	'''
	cleanStr is for cleaning the string to display the appropriate binary number
	input for cleanStr() is:
	dirtyNum: String from binary list
	fracWhole: 1 = Whole Number / 0 = Fraction of Number 
	'''
	cleanNum = dirtyNum.strip('[]')
	cleanNum = cleanNum.replace(',','')
	cleanNum = cleanNum.replace(' ','')
	if fracWhole == 1:
		cleanNum = cleanNum[::-1]
	return cleanNum

def toBinary(decNum):
	'''
	Function to convert Decimal to Brinary
	Takes input of decNum which must be a number
	'''

	# math.modf() converts number to list of what is before and after the decimal
	DecList = math.modf(decNum)
	DecListFrac = DecList[0]
	DecListWhole = DecList[1]
	# Empty List to build binary number
	BinWholConv = []

	# Whole number to binary conversion
	while DecListWhole > 0:
		BinNum = DecListWhole % 2
		BinNum = int(BinNum)
		if BinNum == 0:
			BinWholConv.append(0)
		elif BinNum == 1:
			BinWholConv.append(1)
		DecListWhole = DecListWhole / 2
		WholeTup = math.modf(DecListWhole)
		DecListWhole = int(WholeTup[1])

	# Convert BinWholConv from List to String
	WholeConvStr = str(BinWholConv)
	# Clean String
	cleanWholeConv = cleanStr(WholeConvStr, 1)

	# Fraction to binary conversion
	BinFracConv = []
	BinFracLength = len(BinFracConv)
	while DecListFrac > 0 and BinFracLength < 8:
		BinNum = DecListFrac * 2
		BinNum = float(BinNum)
		if BinNum < 1 and BinNum > 0:
			BinFracConv.append(0)
			DecListFrac = BinNum
			# print(DecListFrac) !! For TESTING
		elif BinNum >= 1:
			BinFracConv.append(1)
			DecListFrac = BinNum - 1
		FracConvStr = str(BinFracConv)
		BinFracLength = len(BinFracConv)
		cleanFracConv = cleanStr(FracConvStr, 0)

	# Determines what to return
	if BinWholConv:
		if BinFracConv:
			numStr = cleanWholeConv + '.' + cleanFracConv
			return numStr
		else:
			return cleanWholeConv
	elif cleanFracConv:
		numStr = '0.' + cleanFracConv
		return numStr


# Run the main function (AKA run program)
main()