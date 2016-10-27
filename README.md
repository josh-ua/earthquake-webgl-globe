# earthquake-webgl-globe
WebGL Globe that displays recent earthquakes - option to display earthquakes within the past 24 hours, 7 days or 30 days.

The data is pulled from USGS in .csv files. I have written a python script to grab the files and convert them to the JSON format required for display on the globe ('getdata.py'). This runs every 24 hours (and thus the globe data is updated every 24 hours). The globe requires the magnitude data for each column to be a value between 0 and 1. To normalize the earthquake magnitudes, I divided each magnitude by 9.5 (the current 'max' of the Richter scale).













##In short (provided for the Capital One Challege):
  I have written a Python script ('getdata.py') that  grabs recent earthquake data from USGS's website, and then converts them into the JSON format required for the globe. The globe requires the magnitude data for each column to be a value between 0 and 1, so to normalize this each earthquake magnitude is divided by 9.5 (the current 'max' of the Richter scale). Users have the option of easily selecting between 3 different data sets with HTML buttons - earthquakes in the past 24 hours, 7 days or 30 days. The globe is initiazlied only once - when a user clicks on a button with a different dataset, the current points on the globe get cleared and the new ones get plotted. To do this, I added a "clearAllPoints" function to the globe ('globe.js') and made the plotting of the points a function in 'index.html.'  I also wrote a couple of other JavaScript functions in 'index.html' to make the page a little more dynamic. This includes labeling what dataset is currently being displayed under the buttons & inserting a "last updated" time in the bottom right corner of the page (the time is generated whenever 'getdata.py' runs). 
  
  for josh:
    getdata.py
