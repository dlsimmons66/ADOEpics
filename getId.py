'''
Extract the EPIC ID from the provided URL String 
User must pass the URL
'''

import re

def get_id(url):
    try:
        match = re.search(r'(\d+)$', url)
        if match:
            number = int(match.group(1))
            return str(number)
    except Exception as e:
       print(f"There was an exception in {get_id.__name__} :", e)