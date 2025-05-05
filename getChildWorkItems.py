from getOpenFileWrite import openFileWrite

"""
This module looks at the story ID to determine if  
it is a child of the EPIC ID being iterated by 
'get epics_details_completed'

citem = child item
EpicTitle
EpicID
event_id = Looking for an Error EventID 
"""

def get_child_work_items(data,projectLog,csvLog):
    child_urls = []

    try:
        if 'event_id' in data:
            error_msg = data.get('message')
            message=f"Error: " + str(error_msg)
            openFileWrite(message,projectLog)
            pass
        else:
            if 'relations' in data['value'][0]:
                for citems in data['value']:
                    EpicTitle = str(citems['fields']['SystemTitle']).replace(",", "").replace(", ", "")
                    Epic_ID = str(citems['id'])
                    
                    header = f"\n#*5\n#*5" + Epic_ID + ": " + EpicTitle + "\n#*5"
                    openFileWrite(header,projectLog)
                    openFileWrite(header,csvLog)

            for relation in data['value'][0]['relations']:
                if relation['rel'] == 'System.LinkTypes.Hierarchy-Forward' and relation['attributes']['name'] == 'Child':
                    child_urls.append(relation['url'])
    
        return child_urls
    
    except Exception as e:
       print(f"There was an exception in {get_child_work_items.__name__} :", e)