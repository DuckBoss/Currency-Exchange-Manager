from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter
import sys

# This program has a forex-python dependency #
class ExchangeData:

	def __init__(self):
		print("\tProgram Started...\n")
		try:
			self.rates = CurrencyRates()
			self.codes = CurrencyCodes()
			self.bit = BtcConverter()
		except:
			print("Unexpected Error: The program could not start!")
			sys.exit(1)

	def displayAllRates(self, countryOrigin):
		try:
			print("All Rates -\n {}\n".format(self.rates.get_rates(countryOrigin)))
		except:
			print("Cannot Currently Display All Rates\n")

	def displayExchangeRate(self, countryOrigin, countryTarget):
		try:
			print("Current Exchange Rate - {}\n".format(self.rates.get_rate(countryOrigin, countryTarget)))
		except:
			print("Cannot Currently Display This Exchange Rate\n")	

	def displayConversionRate(self, countryOrigin, countryTarget, originMoney):
		try:
			print("Current Conversion Rate - {}{}\n".format(self.codes.get_symbol(countryTarget).encode('UTF-8'), self.getExchangeRate(countryOrigin, countryTarget, originMoney)))
		except:
			print("Cannot Currently Display This Conversion Rate\n")

	def getExchangeRate(self, countryOrigin, countryTarget, originMoney):
		return self.rates.convert(countryOrigin, countryTarget, originMoney)

	def displayBitRate(self, originMoney, countryOrigin):
		try:
			print("Current Exchange - {}{}\n".format(self.codes.get_symbol('GBP').encode('UTF-8'), self.getBitRate(originMoney, countryOrigin)))
		except:
			print("This Bitcoin Exchange Rate Is Currently Unavailable\n")

	def getBitRate(self, originMoney, countryOrigin):
		return self.bit.convert_to_btc(originMoney, countryOrigin)

def main():
	program = ExchangeData()

	while(True):
		print("-----------------------------------")
		print("\t==== MENU ====")
		print("-----------------------------------")
		print("\t### Commands ###\n"
			"\tConvert Currency - [C/c]\n"
			"\tConvert BitCoin - [B/b]\n"
			"\tDisplay Exchange Rate - [D/d]\n"
			"\tDisplay All Rates - [DA/da]\n"
			"\tQuit - [Q/q]\n")
		inp = raw_input("Input - ").upper().strip()
		if(inp == "C"):
			inputCountry = raw_input("Enter Origin Country: ")
			outputCountry = raw_input("Enter Target Country: ")
			inputAmount = input("Input Currency Amount To Exchange: ")
			program.displayConversionRate(inputCountry, outputCountry, inputAmount)
		if(inp == "B"):
			inputCountry = raw_input("Enter Origin Country: ")
			inputAmount = input("Input Currency Amount To Exchange: ")
			program.displayBitRate(inputAmount, inputCountry)
		if(inp == "DA"):
			inputCountry = raw_input("Enter Origin Country: ")
			program.displayAllRates(inputCountry)
		if(inp == "D"):
			inputCountry = raw_input("Enter Origin Country: ")
			outputCountry = raw_input("Enter Target Country: ")
			program.displayExchangeRate(inputCountry, outputCountry)
		if(inp == "Q"):
			sys.exit(0)



	

if __name__ == "__main__":
	main()
