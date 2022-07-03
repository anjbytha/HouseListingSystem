import requests
import json

#Name of file: housingAPI
#Group members: Anjana Bytha | abytha@andrew.cmu.edu
#               Prajakta Wani | pwani@andrew.cmu.edu
#               Rahul Goenka | rgoenka@andrew.cmu.edu
#               Shashank Kunikullaya | suk@andrew.cmu.edu
#               Vamsidhar Parasurampuram | vamsidhp@andrew.cmu.edu
#This file sends out API calls to get live list of availabe apartments depending on the user's search parameters
#This file is imported by the 'project_main' module


#method to get a dict of listings
def property_from_api(zip_code, beds, baths, rent):
    url = "https://realty-in-us.p.rapidapi.com/properties/v2/list-for-rent"

    querystring = {"city":"Pittsburgh","state_code":"PA","limit":"20","offset":"0","postal_code":zip_code,"sort":"relevance", "beds_min": beds, "baths_min": baths, "price_max": rent}

    headers = {
        'x-rapidapi-host': "realty-in-us.p.rapidapi.com",
        'x-rapidapi-key': "48abb2399fmshab16a324db148abp16bffdjsn0a218e22315c"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = json.loads(response.text)
    properties = resp["properties"]
    prop_dict = {}
    index = 0
    for value in properties:
        if value is not None:
            if "community" in value:
                prop_dict[index] = {}
                prop_dict[index]["rent"] = value["community"]["price_max"]
                prop_dict[index]["street"] = value["address"]["line"]
                prop_dict[index]["city"] = "Pittsburgh"
                if("neighborhood_name" in value["address"]):
                    prop_dict[index]["neighborhood"] = value["address"]["neighborhood_name"]
                else:
                    prop_dict[index]["neighborhood"] = ""
                prop_dict[index]["state"] = "PA"
                prop_dict[index]["zip"] = zip_code
                prop_dict[index]['beds'] = value["community"]["beds_max"]
                prop_dict[index]['baths'] = value["community"]["baths_max"]
                prop_dict[index]['sqft'] = value["community"]["sqft_max"]
                index += 1
    return prop_dict
