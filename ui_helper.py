"""Helper methods for the UI"""
import json
import re
import streamlit as st
import pandas as pd

class UIHelper:
    
    def is_valid_json(s):
        try:
            json.loads(s)
            return True
        except Exception as e:
            return False
    
    def camel_to_capitalized(camel_str):
        words = re.sub('([a-z0-9])([A-Z])', r'\1 \2', camel_str).split()
        capitalized_str = ' '.join(word.capitalize() for word in words)
        return capitalized_str

    def parse_json(json_obj):
        # Initialize DataFrame to store items
        items = pd.DataFrame(columns=["Name", "Value"])
        previous_key = None
        
        # Iterate over the keys and values in the json object
        for key, value in json_obj.items():
            # If the key is different from the previous one, add an empty row
            previous_key = key

            # If the value is a string, add it to the items DataFrame
            if isinstance(value, str):
                new_row = pd.DataFrame([{"Name": UIHelper.camel_to_capitalized(key), "Value": value}])
                items = pd.concat([items, new_row], ignore_index=True)        
            elif isinstance(value, list):
                new_row = pd.DataFrame([{"Name": UIHelper.camel_to_capitalized(key), "Value": ', '.join(value)}])
                items = pd.concat([items, new_row], ignore_index=True)
                
        # Return the DataFrame
        return items

    def render_json(data):
        if UIHelper.is_valid_json(data):
            json_obj = json.loads(data)
            df_items = UIHelper.parse_json(json_obj)
            st.table(df_items)
        else:
            st.write(data)
