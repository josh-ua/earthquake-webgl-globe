import urllib.request ##to grab files
import csv ##to process files
import json ##to process files
import os ##to delete files
from datetime import datetime ##get date
import time ##to sleep


##names of a files (these are constant), final output initalized
csvNames = ["all_month.csv", "all_week.csv", "all_day.csv"]
output =[]

##grabs csv files from url
def grabFiles():
    url ="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"

    for name in csvNames:
        print("Getting " + name)
        urllib.request.urlretrieve(url+name, name)
        print("Received "+name+ " successfully")
        print()

##gets relevant data from csv files and then puts them into json format for the webgl globe
##makes a new json file for each one
def processFiles():
    for fileName in csvNames:
        print("Opening and processing "+ fileName)
        csvFile = csv.DictReader(open(fileName, "rt"))

        data = []
        for row in csvFile:
            # sometimes some of the data needed is missing (most of the times it's magnitude), so we check everything is there
            #if not, skip it because it's of no use
            if (row['latitude'] != "" and row['longitude'] != "" and row['mag'] != ""):
                data.append(float(row['latitude']))
                data.append(float(row['longitude']))
                data.append(float(row['mag']) / 9.5)
        output.append([fileName.replace(".csv", ""), data])
        print("Processed "+fileName+ " successfully.")
        print("Converting output data to json file...")
        with open((fileName.replace(".csv", "")+".json"), 'w') as outfile:
            json.dump(output, outfile)


    ##deletes csv files after we're done with them
    ##doing them all together afte data conversion help prevent the OS from thinking the file is in use
    print("Done converting - now deleting...")
    for fileName in csvNames:
        try:
            os.remove(fileName)
            print("Deleted: "+fileName)
        except: ##either it's not there, or the OS is using it for some reason (that seems to only happen on windows)
            print("Delete FAILED: "+fileName)

    print("Done.")


##makes a json file with the current time - allows for "last updated" information to be displayed alongside globe
def lastUpdated():
    with open('last_updated.json', 'w') as outfile:
        json.dump((str(datetime.now())), outfile)

#main method
def main():
    grabFiles();
    processFiles();
    lastUpdated();
    print(str(datetime.now()))
    print('Sleeping for 24 hours...')
    print()
    time.sleep(86400)


while True:
    main();




