import requests
from bs4 import BeautifulSoup
import tableData_1 as TD
import pandas as pd

#Name of file: ranking_code
#Group members: Anjana Bytha | abytha@andrew.cmu.edu
#               Prajakta Wani | pwani@andrew.cmu.edu
#               Rahul Goenka | rgoenka@andrew.cmu.edu
#               Shashank Kunikullaya | suk@andrew.cmu.edu
#               Vamsidhar Parasurampuram | vamsidhp@andrew.cmu.edu
#This file scrapes the data from the website and imports data from csv
#It also creates a data frame and assigns ranks to each attribute
#This file imports the 'tableData_1' module
#This file is imported by the 'project_main' module

class TableScrapper:
    results = []
    table = []
    
    def fetch(self, url):
        return requests.get(url)
    
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find('table')
        rows = table.findAll('tr')
        self.results.append([header.text.strip() for header in rows[0].findAll('th')])
        
        for row in rows:
            if len(row.findAll('td')):
                self.results.append([data.text for data in row.findAll('td')])
            
    def run(self):
        response = self.fetch("https://www.walkscore.com/PA/Pittsburgh")
        self.parse(response.text)

scraper = TableScrapper()
scraper.run()
TD.TableScrapper.runAll()
resultsSafety = TD.TableScrapper.results

walkScorePD = pd.DataFrame(scraper.results)
safetyPD = pd.DataFrame(resultsSafety)
 
#https://stackoverflow.com/questions/31328861/python-pandas-replacing-header-with-top-row
new_headerWalk = walkScorePD.iloc[0] #grab the first row for the header
walkScorePD = walkScorePD[2:] #take the data less the header row
walkScorePD.columns = new_headerWalk #set the header row as the df header
 
#https://stackoverflow.com/questions/31328861/python-pandas-replacing-header-with-top-row
new_header = safetyPD.iloc[0] #grab the first row for the header
safetyPD = safetyPD[2:] #take the data less the header row
safetyPD.columns = new_header #set the header row as the df header

traffic_data = pd.read_csv('Traffic_data.csv')

parking_data = pd.read_csv('Parking_data_2.csv')
zip_locality_map = pd.read_csv('Zip-Locality Mapping.csv')

mergeSafetyWalk = pd.merge(left=walkScorePD,right=safetyPD,left_on="Name",right_on="Neighborhood")
final_data1 = mergeSafetyWalk.drop_duplicates(subset=['Neighborhood'])

mergeTrafficParking = pd.merge(left=traffic_data,right=parking_data,left_on="Neighborhood",right_on="Neighborhood")
final_data2 = mergeTrafficParking.drop_duplicates(subset=['Neighborhood'])

mergeAll = pd.merge(left=mergeSafetyWalk, right=mergeTrafficParking, left_on="Neighborhood", right_on="Neighborhood")
mergeAllData = mergeAll.drop_duplicates(subset=['Neighborhood'])
 
merge_DataWithZipcode = pd.merge(left=mergeAllData,right=zip_locality_map,left_on="Neighborhood",right_on="Neighborhood")
final_mergedData = merge_DataWithZipcode.drop_duplicates(subset=['Neighborhood'])
final_mergedData = final_mergedData.drop(columns=['Name'])
 
 # Create a column Rating_Rank which contains
 # the rank of each movie based on rating
final_mergedData['Walk_score_Rank'] = final_mergedData['Walk Score'].rank(ascending=False).astype(int)
final_mergedData['Transit_score_Rank'] = final_mergedData['Transit Score'].rank(ascending=False).astype(int)
final_mergedData['Bike_score_Rank'] = final_mergedData['Bike Score'].rank(ascending=False).astype(int)
final_mergedData['Crime_score_Rank'] = final_mergedData['Crime Per 100K'].rank(ascending=False).astype(int)
final_mergedData['Traffic_score_Rank'] = final_mergedData['Average_Daily_Car_Traffic'].rank(ascending=False).astype(int)