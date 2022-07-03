import numpy as np
import pandas as pd
from housingAPI import property_from_api
import re
import ranking_code as rd
import visualizations as visuals

#Name of file: project_main
#Group members: Anjana Bytha | abytha@andrew.cmu.edu
#               Prajakta Wani | pwani@andrew.cmu.edu
#               Rahul Goenka | rgoenka@andrew.cmu.edu
#               Shashank Kunikullaya | suk@andrew.cmu.edu
#               Vamsidhar Parasurampuram | vamsidhp@andrew.cmu.edu
#This file serves as the main file integrating the code from all the different modules
#This file imports the 'property_from_api' method from the housingAPI module
#It also imports the ranking_code module and the visualizations module 


#method to display list of properties based on selection criteria    
def display_properties(properties):
    index = 0
    print ("{:<10} {:<30} {:<30} {:<20} {:<5} {:<10} {:<5} {:<5} {:<7} {:<7}".format('INDEX', 'STREET', 'NEIGHBORHOOD', 'CITY', 'STATE', 'ZIP', 'BEDS', 'BATHS', 'SQ FT','RENT'))
    for index, prop in properties.items():
        index += 1
        street = prop['street']
        city = prop['city']
        neighborhood = prop['neighborhood']
        state = prop['state']
        zipc = prop['zip']
        beds = prop['beds']
        bath = prop['baths']
        sqf = prop['sqft']
        rent = prop['rent']
        print ("{:<10} {:<30} {:<30} {:<20} {:<5} {:<10} {:<5} {:<5} {:<7} {:<7}".format(str(index), str(street), neighborhood, str(city), str(state), str(zipc), str(beds), str(bath), str(sqf), str(rent)))

#method to rank neighborhoods based on preset attributes
def display_rank(zipcode, dataf):
    rows = len(dataf.index)
    row_val = -1
    for i in range(rows):
        if(zipcode == str(dataf.loc[i]['Zipcode'])):
            row_val = i
            break
        
    print("*"*30 + "\n\n")
    print("Here are some statistics about the neighborhood...\n\n")
    print("*"*30 + "\n\n")
    
    if(row_val>-1):
        print(zipcode, " ranks ", dataf.loc[row_val]['Crime_score_Rank'], ' in Safety' )
        print(zipcode, " ranks ", dataf.loc[row_val]['Walk_score_Rank'], ' in Walkability' )
        print(zipcode, " ranks ", dataf.loc[row_val]['Transit_score_Rank'], ' in Transportability' )
        print(zipcode, " ranks ", dataf.loc[row_val]['Bike_score_Rank'], ' in Bikability' )
        print(zipcode, " ranks ", dataf.loc[row_val]['Traffic_score_Rank'], ' in Traffic' )
    else:
        print("Not found")
    

#main method to get user input and carry out the required processes            
if __name__ == '__main__':
    print("*"*30 + "\n\n")
    print("Welcome to OnlyHomes™! Let's find your next home...\n\n")
    print("*"*30 + "\n\n")
    
    zip_locality_map = rd.zip_locality_map
    
    #Prompt the user for a zip, neighborhood name or look at popular neighboorhoods
    
    while(True):
        final_data = rd.final_mergedData

        print("\n\nChoose:\n")
        print("1. Search by Zipcode\n")
        print("2. Search by Neighborhood\n")
        print("3. Look at Popular Neighborhoods\n")
        print("4. Exit.\n")
        
        choice = input()
        
        if choice == '1':
            found_zip = False
            while(not found_zip):
                print("\nPlease enter a 5 digit Zipcode in Pittsburgh (15XXX)\n")
                zip_code = input()
                pat = r'^15\d{3}$'
                if re.search(pat, str(zip_code)) == None:
                    print("\nInvalid Zipcode! try again")
                else:
                    found_zip = True
                    
        #user can enter the name of the neighborhood as the search criteria
        elif choice == '2':
            found_zip = False
            while(not found_zip):
                print("\n Please enter the neighborhood in Pittsburgh \n")
                neighborhood = input()
                rows = len(zip_locality_map.index)
                
                zip_code = 0
                row_val = -1
                for i in range(rows):
                    if(neighborhood in zip_locality_map.loc[i]['Neighborhood']):
                        row_val = i
                        break
                    
                if(row_val==-1):
                    print("Neighborhood not found in database")
                else:
                    zip_code = str(zip_locality_map.loc[row_val]['Zipcode'])
                    found_zip = True
        
        #users can also select from a list of popular neighborhoods                    
        elif choice == '3':
            found_zip = False
            while(not found_zip):
                print("Choose your preferred neighborhood:\n")
                print("1. Shadyside\n")
                print("2. Squirrel Hill\n")
                print("3. Oakland\n")
                print("4. Downtown\n")
                print("5. South Side\n")
                
                out = input()
                
                if(out == '1'):
                    zip_code = '15232'
                    found_zip = True
                elif(out == '2'):
                    zip_code = '15217'
                    found_zip = True
                elif(out == '3'):
                    zip_code = '15213'
                    found_zip = True
                elif(out == '4'):
                    zip_code = '15222'
                    found_zip = True
                elif(out == '5'):
                    zip_code = '15203'
                    found_zip = True
                else:
                    print("Please enter valid input")
        
        #to exit the program
        elif choice == '4':
            break
        
        else:
            print("Please enter a valid choice")
            print("*"*30)
            
        #adding second set of filters to get more specific user's needs
        print("\nPlease enter your preferences:\n")
        print("1. Enter preferred number of Beds:  (Press Enter to skip)\n")
        no_of_beds = input()
        print("\n2. Enter preferred number of Baths: (Press Enter to skip)\n")
        no_of_baths = input()
        print("\n3. Enter preferred maximum Rent: (Press Enter to skip)\n")
        max_rent = input()
        print('\n' + "*"*30 + '\n')	
        
        properties = property_from_api(zip_code,str(no_of_beds), str(no_of_baths), str(max_rent))
        
        if len(properties) == 0:
            print("Sorry! We did not find any properties in this Zipcode...")
        else:
            print("\nWe found " + str(len(properties)) + " matching your preferences!\n")
            print('\n' + "*"*30 + '\n')
            display_properties(properties)
            display_rank(zip_code, final_data)
            visuals.getCharts(final_data)
                
                
                    
                    
                