import csv
import sqlite3

def starling_info():
	print 'WELCOME TO WHERE YOU CAN GAIN KNOWLEDGE,HERE YOU WILL BE ABLE TO LEARN ABOUT STARLINGS!'

	print("If you would like to know about the starlings ID, catalog, identification, and age, enter "'identity'".If you would like to know who collected the bird, when he/she collected it, and when it arrived at the AMNH, enter "'collection'". If you would like to know where the starlings are from, enter "'place'". If you would like to know how the starlings were brought in, enter "'brought'".If you want to quit, enter "'quit'"." )
 	choice = raw_input("For identity (type i), for collection (type c),for place (type p),for brought (type b), to quit (type q).")


starling_info()
  


conn = sqlite3.connect("Starlings.db")
c = conn.cursor()

starling_in = open("Starlings.csv", 'rU')

starling_reader = csv.reader(starling_in)
column_headers = starling_reader.next()


git add
git commit
git push