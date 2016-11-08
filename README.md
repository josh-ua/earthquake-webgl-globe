# earthquake-webgl-globe
###**[You can view the live globe here](http://ks3099106.kimsufi.com/josh/earthquakes/)**
(it may take a second to load depending on your connection - be patient)
WebGL Globe that displays recent earthquakes - option to display earthquakes within the past 24 hours, 7 days or 30 days. Each point on the globe represents an earthquake origin, and the height of the data point represents the earthquake's magnitude. Best viewed using Chrome.

This README.md file is a (slightly) longer and (slightly) more in-depth version of the paragraph I provided for the Capital One Challenge. 

###'getdata.py' and the actual earthquake data
The data is pulled from USGS in .csv files. I have written a python script to grab the files and convert them to the JSON format required for display on the globe ('getdata.py'). The .csv files then get deleted. This runs every 24 hours (and thus the globe data is updated every 24 hours). The globe requires the magnitude data for each column to be a value between 0 and 1 (or else the columns fly off the screen). To normalize the earthquake magnitudes, I divided each magnitude by 19 (the current 'max' of the Richter scale * 2).

#####why 'the current 'max' of the Richter scale * 2'?
There is no max to the Richter scale. For normalization purposes, I chose 9.5 as the max because that has been the highest magnitude earthquake recorded to date. I then scaled it again by 2 so the data lines were not as tall (completely for aesthetics).

###index.html & globe.js

Users have the option to select from the three different data sets - all earthquakes in the last 24 hours, 7 days and 30 days - with three different HTML buttons. To achieve this, I turned the creation of the globe into a function and the plotting of the data into a separate function. The globe is loaded in blank when the page first loads, and whenever a button is clicked by a user, the corresponding data set is passed in as an argument to the plotting function and the data is displayed on the globe. By default, the '24 hours' data set is passed through when the page fully loads (so if the user does not click a button, this dataset will display by default). Also, the text under the buttons is dynamic and changes depending on which dataset is currently being displayed.

The entire globe is NOT reloaded every time a user clicks the new data set (that would be awfully slow and laggy after a few clicks). Only the data points are changed. To achieve this, I added a "clearAllPoints" function to the globe ('globe.js') and that is called before a new data set gets plotted. The data set then gets plotted, and then a conditional ‘if statement’ checks if the globe is animated already - if it has been, then it will not reanimate it (this prevents the globe from getting laggy). Also, I toyed with the color function in 'globe.js' so the color of the points changes from green to red depending on how tall it is.

Lastly, everytime the 'getdata.py' script runs it outputs another file with the current date and time. Whenever the window is loaded, a JavaScript function is ran where it parses that file and updates the "lastUpdated" HTML span (the text in the lower right hand corner).

###how to get started with this globe
If you want to run or play with my globe on your own time, just clone the repo and serve the files. Don't forget to cd into /data/ and run the 'getdata.py' script to ensure the data is accurate. Please note that **Python 3.0 or above** is required for that script.

##In short (provided for the Capital One Challege):
  I have written a Python script ('getdata.py') that grabs recent earthquake data from USGS's website, and then converts them into the JSON format required for the globe. Each point on the globe represents an earthquake origin, and the height of the data point represents the earthquake's magnitude. The globe requires the magnitude data for each column to be a value between 0 and 1, so to normalize this each earthquake magnitude is divided by 19 (the current 'max' of the Richter scale * 2). Users have the option of easily selecting between 3 different data sets with HTML buttons - earthquakes within the past 24 hours, 7 days or 30 days. When the page loads, the '24 hours' data set is automatically displayed. The globe is initialized only once - when a user clicks on a button with a different data set, the current points on the globe get cleared and the new ones get plotted. To do this, I added a "clearAllPoints" function to the globe ('globe.js') and made the plotting of the points a function in 'index.html.'  I also wrote a couple of other JavaScript functions in 'index.html' to make the page a little more dynamic. This includes labeling what data set is currently being displayed under the buttons & inserting a "last updated" time in the bottom right corner of the page (the time is generated whenever 'getdata.py' runs). Lastly, I toyed with the color function in 'globe.js' so the colors of the points change from green to red depending on how tall it is (or rather, how high the earthquake magnitude was).
  

  
