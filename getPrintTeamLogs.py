from getOpenFileWrite import openFileWrite

"""
This module prints the stories for each team member
to the associated Team Member Log (TML) file.  

TML_PATH = "/Users/david/Desktop/Python Course/"
TML = {
    "David Simmons" : TML_PATH + "david.txt",
}

area_path     = "observability"
iteration     = "sprint4"
story_id      = "098765"
story_title   = "Science Logic SQL Rules"
state         = "active"
project_phase = "SDE"
assigned_to   = "David Simmons"
"""

def printTeamLogs(TML,area_path,iteration,story_id,story_title,state,project_phase,assigned_to):
    att = assigned_to.title()

    try:
        for key in TML.keys():
            if att in key:
                file_path = TML[key]

                message = ("Area Path:   " + (area_path) + "\n"
                    + "Iteration:   " + (iteration) + "\n"
                    + "Story ID:    " + (story_id) + "\n"
                    + "Title:       " + (story_title).title() + "\n"
                    + "State:       " + (state) + "\n"
                    + "Phase:       " + (project_phase) + "\n"
                    + "Assigned To: " + (assigned_to).title() + "\n"
                )

                openFileWrite(message,file_path)
                return

    except Exception as e:
        print(f"There was an exception in '{printTeamLogs.__module__}' : ", e)
