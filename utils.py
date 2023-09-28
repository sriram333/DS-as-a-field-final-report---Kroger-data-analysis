import constants as cn
import requests
import json
import pandas as pd

import numpy as np


#Get access token 

def request_access_token():

    response = requests.post(cn.url, headers=cn.headers, data=cn.data)

    if "error" not in response.text:
        res_dict = json.loads(response.text)
        return res_dict
    else:
        print(response.text)

    

def extract_product_data(url,res_dict,term,limit,fulfillment,location_id):
    
    headers = {
    'Authorization': 'Bearer ' + res_dict['access_token'],
    'Cache-Control': 'no-cache'
    }
    
    params = {
    'filter.term': term,
    'filter.locationId': [location_id],
        'filter.fulfillment': fulfillment,
    'filter.limit':limit}
    response = requests.get(url, headers=headers,params=params)
    if "error" not in response.text:
        df_item = pd.DataFrame(json.loads(response.text)['data'])
        return df_item
    else:
        print(response.text)
    

def extract_location_data(url,res_dict,zipcode_str,max_results,search_radius_miles,chain):

    headers = {
    'Authorization': 'Bearer ' + res_dict['access_token'],
    'Cache-Control': 'no-cache'
    }
    
    params = {
    "filter.zipCode.near":zipcode_str, 
    "filter.limit":max_results,
    "filter.radiusInMiles":search_radius_miles,
    "filter.chain":chain}
    response = requests.get(url, headers=headers,params=params)
    if "error" not in response.text:
        stores = response.json()["data"]  
        df_loc = pd.json_normalize(stores)
        df_loc = df_loc.dropna()
        if 'departments' in df_loc.columns:
            df_loc['departments'] = df_loc['departments'].map(lambda dept_obj_list: [d["name"] for d in dept_obj_list])
            return df_loc 
        else:
            return df_loc
    else:
        print(response.text)






