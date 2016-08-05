import csv
import sqlite3
conn = sqlite3.connect("StarlingInfo.db")
c = conn.cursor()
starling_in = open("Starlings.csv", 'rU')
starling_reader = csv.reader(starling_in)
column_headers = starling_reader.next()




def queryIdentity():
	print("YIPPEEE WE WILL QUERY IDENTITY NOW....")
	print "How many adults were found in Los Angeles?"
	for item in c.execute('SELECT "Identity.Age ",Location.County FROM Location JOIN BigTable ON BigTable.LID = Location.LID JOIN Identity ON BigTable.ID = Identity.ID WHERE Location.County = "Los Angeles County"'):
		for i in item:
			print i
	
def queryCollection():
	print("YIPPEEE WE WILL QUERY COLLECTION NOW....")
	print "How many Starlings did each collector collect?"
	for item in c.execute("SELECT Collector, Count(CID) FROM BigTable GROUP BY Collector"):
		for i in item:
			print i
	#how do you query COLLECTION?


def choice(ltr): 
	if (ltr.lower() == "i"):
		#do something
		print("you chose identity") #comment this out after debugging
		#call the function you need
		queryIdentity()
	elif (ltr.lower() == "c"):
		#do something
		print("you chose collection")
		queryCollection()
	elif (ltr.lower() == "g"):
		#do something
		print("you chose geography")
		queryGeography()
	elif (ltr.lower() == "b"):
		#do something
		print("you chose brought")	
		queryBrought()
	elif (ltr.lower() == "q"):
		print("Come Back Again")
	else:
		print("I DON't KNOW WHAT YOU CHOSE.")
		

def starling_info():
	user_choice = "0"
	while user_choice != "q": 	
		print 'WELCOME TO WHERE YOU CAN GAIN KNOWLEDGE,HERE YOU WILL BE ABLE TO LEARN ABOUT STARLINGS!'

		print("How many adults were found in Los Angeles? How many starlings did each collector collect? If you want to quit, enter "'quit'"." )
	 	user_choice = raw_input("For identity (type i), for collection (type c),to quit (type q).")
	 	choice(user_choice)

 	
starling_info() 	




