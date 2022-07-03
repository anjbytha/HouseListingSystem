import pandas as pd
import matplotlib.pyplot as plt

#Name of file: visualizations
#Group members: Anjana Bytha | abytha@andrew.cmu.edu
#               Prajakta Wani | pwani@andrew.cmu.edu
#               Rahul Goenka | rgoenka@andrew.cmu.edu
#               Shashank Kunikullaya | suk@andrew.cmu.edu
#               Vamsidhar Parasurampuram | vamsidhp@andrew.cmu.edu
#This file has the code that creates the visualizations for individual parameters
#This file is imported by the 'project_main' module
  
def getCharts(final_mergedData):
    
    print("\n\nBar highlighted in red shows zip code with the highest value\n\n")
    #Visualizations
    final_mergedData.rename(columns={"Walk Score":"WalkScore", "Zipcode":"Zipcode", "Crime Per 100K":"CrimesPer100K", "Bike Score":"BikeScore"}, inplace=True)
    
    #Removing outliers
    final_mergedData = final_mergedData.sort_values(by=['Zipcode'])
    final_mergedData = final_mergedData.iloc[1:64, :]
    
    #Converting the string values to int
    final_mergedData["WalkScore"] = pd.to_numeric(final_mergedData["WalkScore"])    
    final_mergedDataSorted = final_mergedData.sort_values(by=['WalkScore'])
    
    #Bar chart for WalkScore
    final_mergedDataSorted = final_mergedData.sort_values(by=['WalkScore'])
    
    # plotting a line plot after changing it's width and height
    f = plt.figure()
    f.set_figwidth(14)
    f.set_figheight(8)
    
    colors = ['crimson' if (bar == max(final_mergedDataSorted['WalkScore'])) else 'lightblue' for bar in final_mergedDataSorted['WalkScore']]
    plt.bar(x=final_mergedDataSorted['Zipcode'], height=final_mergedDataSorted['WalkScore'], width = 0.7, color=colors)
    plt.xticks(final_mergedDataSorted['Zipcode'], rotation = 45)
    plt.xlabel('Zipcode', fontsize=16)
    plt.ylabel('WalkScore', fontsize=16)
    plt.show()
    
    #Bar chart for Bike Score
    #Converting the string values to int
    final_mergedData["BikeScore"] = pd.to_numeric(final_mergedData["BikeScore"])    
    final_mergedDataSortedBikeScore = final_mergedData.sort_values(by=['BikeScore'])
    
    # plotting a line plot after changing it's width and height
    f = plt.figure()
    f.set_figwidth(14)
    f.set_figheight(8)
    
    colors = ['crimson' if (bar == max(final_mergedDataSortedBikeScore['BikeScore'])) else 'lightblue' for bar in final_mergedDataSortedBikeScore['BikeScore']]
    plt.bar(x=final_mergedDataSortedBikeScore['Zipcode'], height=final_mergedDataSortedBikeScore['BikeScore'], width = 0.7, color=colors)
    plt.xticks(final_mergedDataSortedBikeScore['Zipcode'], rotation = 45)
    plt.xlabel('Zipcode', fontsize=16)
    plt.ylabel('Bike Score', fontsize=16)
    plt.show()

    #Bar chart for Safety
    #Replacing ',' in numbers with space https://stackoverflow.com/questions/63425208/valueerror-unable-to-parse-string-15-181-80-at-position-0 
    final_mergedData["CrimesPer100K"] = final_mergedData["CrimesPer100K"].str.replace(',', '').astype(int)
    
    #Converting the string values to int
    final_mergedData["CrimesPer100K"] = pd.to_numeric(final_mergedData["CrimesPer100K"])    
    final_mergedDataSortedCrime = final_mergedData.sort_values(by=['CrimesPer100K'])
    
    # plotting a line plot after changing it's width and height
    f = plt.figure()
    f.set_figwidth(14)
    f.set_figheight(8)
    
    colors = ['crimson' if (bar == max(final_mergedDataSortedCrime['CrimesPer100K'])) else 'lightblue' for bar in final_mergedDataSortedCrime['CrimesPer100K']]
    plt.bar(x=final_mergedDataSortedCrime['Zipcode'], height=final_mergedDataSortedCrime['CrimesPer100K'], width = 0.7, color=colors)
    plt.xticks(final_mergedDataSortedCrime['Zipcode'], rotation = 45)
    plt.xlabel('Zipcode', fontsize=16)
    plt.ylabel('Crimes Per 100K', fontsize=16)
    plt.show()
    
    #Bar chart for Traffic Data
    #Converting the string values to int
    final_mergedData["Average_Daily_Car_Traffic"] = pd.to_numeric(final_mergedData["Average_Daily_Car_Traffic"])    
    final_mergedDataSortedTraffic = final_mergedData.sort_values(by=['Average_Daily_Car_Traffic'])
    
    # plotting a line plot after changing it's width and height
    f = plt.figure()
    f.set_figwidth(14)
    f.set_figheight(8)
    
    colors = ['crimson' if (bar == max(final_mergedDataSortedTraffic['Average_Daily_Car_Traffic'])) else 'lightblue' for bar in final_mergedDataSortedTraffic['Average_Daily_Car_Traffic']]
    plt.bar(x=final_mergedDataSortedTraffic['Zipcode'], height=final_mergedDataSortedTraffic['Average_Daily_Car_Traffic'], width = 0.7, color=colors)
    plt.xticks(final_mergedDataSortedTraffic['Zipcode'], rotation = 45)
    plt.xlabel('Zipcode', fontsize=16)
    plt.ylabel('Average Daily Car Traffic', fontsize=16)
    plt.show()
