class Whisky:

	def __init__(self, brand, abv, country, typ, scoore):
		self.brand = brand
		self.abv = abv
		self.country = country
		self.typ = typ
		self.scoore = scoore


	def showWhisky(self):
		return '{} {} {} {} {}'.format(self.brand, self.abv, self.country, self.typ, self.scoore)

	def __repr__(self):
		return "Whisky('{}','{}', '{}', '{}', '{}')".format(self.brand, self.abv, self.country, self.typ, self.scoore)


#mac = Whisky('JD No7', 40, 'USA', 'Burbon', 5)

#print(mac.showWhisky())