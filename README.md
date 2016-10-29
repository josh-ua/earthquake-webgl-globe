# earthquake-webgl-globe
WebGL Globe that displays recent earthquakes - option to display earthquakes within the past 24 hours, 7 days or 30 days.

This README.md file is a (slightly) longer and (slightly) more in-depth version of what I provided for the Capital One Challenge. 

###data
The data is pulled from USGS in .csv files. I have written a python script to grab the files and convert them to the JSON format required for display on the globe ('getdata.py'). The .csv files then get deleted. This runs every 24 hours (and thus the globe data is updated every 24 hours). The globe requires the magnitude data for each column to be a value between 0 and 1. To normalize the earthquake magnitudes, I divided each magnitude by 9.5 (the current 'max' of the Richter scale).



###changes to index.html & globe.js

Users have the option to select from the three different datasets - all earthquakes in the last 24 hours, 7 days and 30 days - with three different HTML buttons. To acheive this, I turned the creation of the globe into a function and the plotting of the data into a seperate function. The globe is loaded in blank when the page first loads, and whenever a button is clicked by a user, the corresponding dataset is passed in as an argument to the plotting function and the data is displayed on the globe. By default, the '24 hours' dataset is passed through when the page fully loads (so if the user does not click a button, this dataset will dispaly by default). Also, the text under the buttons is dynamic and changes depending on which dataset is currently being displayed.

The entire globe is NOT reloaded everytime a user clicks the new dataset (that would be awfully slow and laggy after a few clicks). Only the data points are changed. To achieve this, I added a "clearAllPoints" function to the globe ('globe.js') and that is called before a new dataset gets plotted. The datset then gets plotted, and the a conditional if statement checks if the globe is animated already -if it has been, then it will not reanimate it (this prevents the globe from getting laggy).

Lastly, everytime the 'getdata.py' script runs it outputs another file with the current date and time. Whenever the window is loaded, a JavaScript function is ran where it parses that file and updates the "lastUpdated" HTML div (the text in the lower right hand corner).

##In short (provided for the Capital One Challege):
  I have written a Python script ('getdata.py') that  grabs recent earthquake data from USGS's website, and then converts them into the JSON format required for the globe. The globe requires the magnitude data for each column to be a value between 0 and 1, so to normalize this each earthquake magnitude is divided by 9.5 (the current 'max' of the Richter scale). Users have the option of easily selecting between 3 different data sets with HTML buttons - earthquakes in the past 24 hours, 7 days or 30 days. The globe is initiazlied only once - when a user clicks on a button with a different dataset, the current points on the globe get cleared and the new ones get plotted. To do this, I added a "clearAllPoints" function to the globe ('globe.js') and made the plotting of the points a function in 'index.html.'  I also wrote a couple of other JavaScript functions in 'index.html' to make the page a little more dynamic. This includes labeling what dataset is currently being displayed under the buttons & inserting a "last updated" time in the bottom right corner of the page (the time is generated whenever 'getdata.py' runs). 
  
