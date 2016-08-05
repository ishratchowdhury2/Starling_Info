UPDATE BigTable 
SET CID = (
	SELECT CID from Collection WHERE 
	BigTable.COLLECTOR = Collection.Collector AND 
	BigTable.COLLECTING_DATE_FROM =  Collection.CollectingFrom AND 
	BigTable.Arrived_AMNH = Collection.Arrived_AMNH); 

	



