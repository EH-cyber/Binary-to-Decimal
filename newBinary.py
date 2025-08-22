#Converts binary to decimal
import math
def main():
		
	decision = input('Would you like to convert:\n1. Decimal to Binary\n2. Binary to Decimal\n3. Binary Fraction to Decimal\nPlease input 1, 2, or 3: ')
	decision = int(decision)
	# Validate input

	match decision:
		# Decimal to binary conversion
		case 1:
			DecNum = input('What is the Decimal number you would like to convert?\n')
			DecNum = float(DecNum)
			DecList = math.modf(DecNum)
			DecListFrac = DecList[0]
			DecListWhole = DecList[1]
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
			WholeConvStr = str(BinWholConv)
			cleanWholeConv = WholeConvStr.strip('[]')
			cleanWholeConv = cleanWholeConv.replace(',', '')
			cleanWholeConv = cleanWholeConv.replace(' ', '')
			cleanWholeConv = cleanWholeConv[::-1]
			# print('Whole Num ', DecList, ' is ', cleanWholeConv[::-1]) !! For TESTING
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
				cleanFracConv = FracConvStr.strip('[]')
				cleanFracConv = cleanFracConv.replace(',', '')
				cleanFracConv = cleanFracConv.replace(' ', '')
			if BinWholConv:
				if BinFracConv:
					print('The Binary of ', DecNum, ' is ', cleanWholeConv + '.' + cleanFracConv)
				else:
					print(cleanWholeConv)
			elif cleanFracConv:
				print('The Binary of ', DecNum, ' is 0.' + cleanFracConv)


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


# Run the main function (AKA run program)
main()