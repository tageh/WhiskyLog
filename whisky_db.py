import sqlite3
from whiskyClass import Whisky

conn = sqlite3.connect('whisky.db')#whisky.db:memory:
global dele
c = conn.cursor()
'''
c.execute("""CREATE TABLE whisky(
			brand text,
			abv int,
			country text,
			typ text,
			scorre int
			)""")
'''
def addWhisky(w):
	with conn:
		c.execute("INSERT INTO whisky VALUES(:brand, :abv, :country, :typ, :scoore)", {'brand': w.brand, 'abv': w.abv, 'country': w.country, 'typ':w.typ, 'scoore':w.scoore})


def showWhisky():
	c.execute("SELECT * FROM whisky")
	for row in c:
		print(row)

def delWhisky(w):
	with conn:
		c.execute("DELETE FROM whisky WHERE brand = :brand", {'brand':w.brand})

while True:
	q1 = input()
	
	if q1 == 'add':
		b = input("Brand and name: ")
		a = input("What abv is the whisky? ")
		cf = input("Where is the whsiky from? ")
		t = input("What type of whisky is it? (borbon, singe malt, blend, etc ")
		s = input("What overall scoore would you like to give the whisky? ")

		addWhisky(Whisky(b,a,cf,t,s))
		print('New whisky added: ' + b)

	elif q1 == 'show':
		#dele = input('hvilken whisky vil du slette?')
		#delWhisky(dele)
		showWhisky()
	elif q1 =='delete':
		showWhisky()
		dele = input('hvilken whisky vil du slette? ')
		delWhisky(dele)
		print("Whisky deleted " + dele)
	elif q1 == "":
			print("Program exit")
			break
	else:
		print("Commadns avalible: \n add \n show \n delete\n 'enter to exit'")


c.execute("DELETE FROM whisky WHERE brand='hei'")
conn.commit()


conn.close()