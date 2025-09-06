#! /usr/bin/env python3
# written by David Simmons
# Version 2.0 - 5/2/2025
# Queries ADO to pull specific EPICS and related Stories

'''
Monitoring & Observability Azure Epics 
This Script is to collect Current Epics/Stories for the 
Monitoring and Observability Team from Azure DevOps and 
list them out in a simple text format for reporting and 
monitoring capabilities.
'''

# Public Modules
import re, pytz, datetime, requests
from dataclasses import dataclass, fields
from requests.auth import HTTPBasicAuth

# Custom Modules
import getOpenFileWrite, getOpenTeamLogs
from getId import get_id
from getTicketDetails import get_ticket_details
from getChildWorkItems import get_child_work_items
from getPrintTeamLogs import printTeamLogs
from getEpicsTally import get_epics_tally

# Variables
CORE_ID     = 'IFYKYK'
TOKEN       = 'xxxxxx'
ORG_URL     = 'https://dev.auzure.com/org'
PROJECT     = 'Odin'
API_VERSION = '7.0'
FIELDS      = 'System.Id,System.WorkItemType,System.Title,System.AreaPath,System.State,System.IterationPath,Custom.ProjectPhase,System.Parent'
EXPAND_OPT  = 'relations'
LINK        = 'https://dev.azure.com/org/{PROJECT}/_workitems/edit/'
GET_EPIC_URL = 'https://dev.azure.com/org/{PROJECT}/_apis/wiql'
MON_QUERY_ID = 'xxxxxx'
TML_PATH    = "/users/{CORE_ID}/project/team/"

# Date & Time for Logging
now = datetime.datetime.now(pytz.timezone("America/Chicago"))
now_str = now.strftime('%Y-%m-%d %H:%M:%S %Z')
today = now.strftime('%m.%d.%Y')

# General Logging
# Need to move to external file to prevent breaking the primary codebase
debug_logs   = "/users/" + CORE_ID + "/project/debug/project_debug.log"
project_logs = "/users/" + CORE_ID + "/project/logs/project_epics." + today + ".logs"
csvLogs      = "/users/" + CORE_ID + "/project/csv/project_epics." + today + ".csv"

# Team Members logs
# For Example only - need to make external text file and import
# data as to not break primary codebase
TML = {
    "John Smith" : TML_PATH + "john_" + today + ".txt",
    "Jane Doe"   : TML_PATH + "jane_" + today + ".txt",
    "Fu Bar"     : TML_PATH + "fu_" + today + ".txt",
}

# List of Epic ID's
# For Example only - need to make external text file and import
# data as to not break primary codebase
MO_MONITORING_EPICS    = ["123456", "234567", "345678"]
MO_OBSERVABILITY_EPICS = ["098765", "987654", "876543"]
MO_PERFORMANCE_EPICS   = ["012345", "019283", "928374"]
MO_AUTOMATION_EPICS    = ["000000", "111111", "222222"]
MO_SECURITY_EPICS      = ["999999", "888888", "777777"]

@dataclass
class UserStory:
    id: str
    title: str
    state: str
    area_path: str
    itr_path: str
    project_phase: str
    assigned_to: str
    iteration: str

# Call module to create the Team Member Story Logs
getOpenTeamLogs(now_str,TML)

# Primary function to pull a list of the completed stories
# from the epics list.
def get_epic_details_completed(epic_list_arry, epic_arry):
    """
    epic_list_arry = array of all of the epics by Epic ID
    epic_arry = identified the epic classification being iterated 
    (i.e. MO, INFRA, PERF, SEC)

    Iterates through the list of EPICS and and grabs the details for
    the stories under the EPIC under the EPIC ID number
    """

    # Resets for each iteration through the epic_list_arry
    completed = 0
    total_cnt = 0

    if AdoDebug:
        message = f"Executing 'get_epic_details_completed' function: {epic_list_arry}"
        getOpenFileWrite(message, debug_logs)

    try:
        for id in epic_list_arry:
            child_ids = get_child_work_items(get_ticket_details(id),
                                             project_logs,
                                             csvLogs
                                             )

            if child_ids is not None:
                for cid in child_ids:
                    cid_details = get_ticket_details(get_id(cid),
                                                     CORE_ID,
                                                     TOKEN,
                                                     ORG_URL,
                                                     PROJECT,
                                                     EXPAND_OPT,
                                                     API_VERSION
                                                     )

                    if AdoDebug:
                        message = f"Executing cid_detail: {cid_details}"
                        getOpenFileWrite(message, debug_logs)
                
                if cid_details is not None:
                    if 'eventId' in cid_details:
                        err_msg = cid_details.get('message')
                        getOpenFileWrite(err_msg, project_logs)
                        pass
                    else:
                        for item in cid_details['value']:
                            area_path = item["fields"]["System.AreaPath"]

                            # Grabbing M&O Stories only
                            if "Observability" in area_path:

                                AdoType = item['fields']['System.WorkItemType']

                                if AdoType == 'UserStory':
                                    story_id      = item['id']
                                    state         = item['fields']['System.State']
                                    story_title   = item['fields']['System.Title']
                                    project_phase = item['fields']['Custom.ProjectPhase']
                                    iteration     = item['fields']['System.IterationPath']

                                    # Since I confuse myself with my var names:
                                    # at = Assigned to
                                    # atdn = Assigned To Display Name in Azure

                                    at_item = ['fields']
                                    atdn = at_item.get('System.AssignedTo')

                                    # Error handling if data not available 
                                    if atdn is not None:
                                        assigned_to = item['fields']['System.AssignedTo']['displayName']
                                    else:
                                        assigned_to = "Unassigned"
                                    
                                    # CLI Output if ADO Debug flag is set
                                    # Need to clean up...
                                    if AdoDebug:
                                        if state not in ['Closed',"Removed"]:
                                            print(f"Area Path:   " + {str(area_path)})
                                            print(f"Iteration:   " + {str(iteration)})
                                            print(f"Story ID:    " + {str(story_id)})
                                            print(f"Title:       " + {str(story_title).title()})
                                            print(f"State:       " + {str(state)})
                                            print(f"Phase:       " + {str(project_phase)})
                                            print(f"Assigned To: " + {str(assigned_to).title()} + "\n")
                                        
                                        # Writes them out to the assigned engineers log file
                                        printTeamLogs(TML,area_path,iteration,story_id,story_title,state,project_phase,assigned_to)

                                    # Standard Logging
                                    message = f"{project_phase},{story_id},{assigned_to},{story_title}"
                                    getOpenFileWrite(message, project_logs)
                                    
                                    # Story count
                                    total_cnt += 1

                                    if state in ["Closed","Removed"]:
                                        completed += 1
                                    else:
                                        # Output to CSV file
                                        message = (
                                            ","
                                            + str(story_id) + ","
                                            + state + ","
                                            + project_phase + ","
                                            + assigned_to.title() + ","
                                            + story_title.title() + ","
                                            + iteration
                                        )
                                        getOpenFileWrite(message, csvLogs)

        remaining_story_count = total_cnt - completed
        stack.append(remaining_story_count)
        percent_completed = (completed/total_cnt)

        # Calls the module to update the logfile with the Epic-Story-Tally
        get_epics_tally(epic_arry,
                        total_cnt,
                        completed,
                        remaining_story_count,
                        percent_completed,
                        CORE_ID,
                        project_logs
                        )
        
        # Print/Output formatting setup 
        char1 = "-"
        repeated = 25
        seperators = f"{'':{char1}>{repeated}}"

        return f"{seperators}\nTotal ticket count: {total_cnt}\nCompleted Story Count: {completed}\nRemaining Story Count: {remaining_story_count}\nPercentage Completed: {(percent_completed)*100:.2f}%\n{seperators}"
    
    except Exception as e:
        print(f"There was an exception in {get_epic_details_completed.__name__}: ", e)


def main():
    global epic_arry, AdoDebug, TML, now, now_str
    global stack
    AdoDebug = False

    epic_lists = {
        "M&O_MONITORING_EPICS":     MO_MONITORING_EPICS,
        "M&O_OBSERVABILITY_EPICS":  MO_OBSERVABILITY_EPICS,
        "M&O_PERFORMANCE_EPICS":    MO_PERFORMANCE_EPICS,
        "M&O_AUTOMATION_EPICS":     MO_AUTOMATION_EPICS,
        "M&O_SECURITY_EPICS":       MO_SECURITY_EPICS,
    }

    try:
        for epic_arry, epic_list_arry in epic_lists.items():
            init_msg = f'{epic_arry}' + ": " + f'{epic_list_arry}'
            getOpenFileWrite(init_msg, project_logs)

            print(f'##### {epic_arry} #####', get_epic_details_completed(epic_list_arry,epic_arry))

        # Initializes the story count under each Epic
        scnt = 0
        for _ in range(len(stack)):
            cnt = stack.pop()
            scnt = scnt + cnt

        char0 = "#"
        main_repeated = 30
        main_sep = f"{'':{char0}>{main_repeated}}"

        print(f"{main_sep}\nTotal remaining stories is: {scnt}\n {main_sep}")

    except Exception as e:
        print(f"There was an exception in '{main.__module__}' : ", e)

if __name__ == '__main__':
    main()
