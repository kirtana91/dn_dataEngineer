import json
from datetime import datetime
from getData import getLatestDate

#opening input file
covidFile = open('C:\DataEngineer\source\data.json')

#loading the file into an object
data = json.load(covidFile)
covidData = data['covidData']

#retreiving latest date and corresponding index of the latest date from the loaded data object
latestDate = getLatestDate(covidData)
print(latestDate[1])
print (covidData[latestDate[1]]['total_results_reported'])

#for i in data['covidData']:
#    print (i['date'])

covidFile.close()