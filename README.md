ADOEpics README

Author: David Simmons 
Date: 05/5/2025
Version: 2.0
Purpose: 
    "Simple Python script to extract scrum stories from 
    ADO for different Users. Originally written in Python 3.13.x 
    to be used on a MacBook with Sequoia (15.4.x) or comperable 
    Linux based OS."

# General Requirements:
    MacOS Sequoia or comperable Linux OS (Ubuntu/RHEL)
    Python 3.13.x/Pip 3.x

# Python imports required:
    re, pytz, timedate, requests, requests.auth, 
    dataclasses, logging, logging.handlers

# Usage: 
    1. The script expects all modules to exist in the 
    same directory location. 
    2. Set your virtual environment. The example below  shows 
    where 'id' is the 'users name' and 'venv' is the 'project'.
    3. import required python modules

    # Example:
        $ /users/{id}/{venv}/bin/python "/users/{id}/{venv}/ADO Epics/getEpics.py" 


# getEpics
    The primary execution file is getEpics.py. Currently the following information
    must be set within the script for it to work properly:

    # project variables requiring setup 
    CORE_ID         # Users ADO or corporate username designation
    TOKEN           # The Users ADO Token obtained from ADO
    ORG_URL         # 'https://dev.auzure.com/org' is the URL to the organizations ADO instance 
    PROJECT         # Is the internal ADO project designation 
    LINK            # 'https://dev.azure.com/org/{PROJECT}/_workitems/edit/' Uses the project
                    # name to route to the work items
    GET_EPIC_URL    # 'https://dev.azure.com/org/{PROJECT}/_apis/wiql'for the project API interface
    MON_QUERY_ID    # The Observability's teams query token
    TML_PATH        # "/users/" + CORE_ID + "/desktop/team/" is the path to the teams assignment logs

    # General Logging - Linux/Mac
    debug_logs   = "/users/" + CORE_ID + "/project/debug/project_debug.log"
    project_logs = "/users/" + CORE_ID + "/project/logs/project_epics." + today + ".logs"
    csvLogs      = "/users/" + CORE_ID + "/project/csv/project_epics." + today + ".csv"

    # Team Members logs - Examples
    TML = {
        "John Smith"    : TML_PATH + "john_" + today + ".txt",
        "Jane Doe"      : TML_PATH + "jane_" + today + ".txt",
    }

# module getChildWorkItems
    This module looks at the story ID to determine if it is a child 
    of the EPIC ID being iterated by 'get epics_details_completed' 
    from within getEpics.py

    This module grabs the required ADO URL for the Epic Child Items 
    and returns them for additional processing

# module getEpicsTally
    This modules calls the getOpenFileWrite to print out the tally of 
    the following information to the project logging file:

        epic_arry,
        total_cnt,
        completed,
        remaining_story_count,
        percent_completed

    CORE_ID is required to get the correct logfile path

    Expected logfile update:
        ------------------------------
        ##### 123456 #####
        Total Ticket Count: 100
        Completed Story Count: 90
        Remaining Stories: 10
        Percent Completed: 90.00% 
        ------------------------------

# module getTicketDetails
    This module retrieves the EPIC ID information from ADO. 

    In order to retrieve the data, the module requires the 
    CORE_ID, TOEKN, Project, and expansion options to properly 
    execute.

# module getOpenFileWrite
    This module creates log files defined in the parameters passed
    to the module. The parameters of 'filepath' and 'message' are 
    required to be passed from within the main program. 

    This modules does not return any values; it simply creates the
    initial files for logging.

# module getOpenTeamLogs
    This module creates the log files for the team members listed
    in the 'Team Member Log' (TML) Array from within the main
    program getTeamEpics. 

    Note: Each logfile is prefixed with a date & time stamp which is 
    over-written if the script is run mulitple times during a
    day. 

    This modules does not return any values; it simply creates
    the initial files for logging.

# module getPrintTeamLogs
    This module prints the stories for each team member
    to the associated Team Member Log (TML) file.  

    TML_PATH = "/users/{id}/{venv}/ADO Epics/logs/"

    TML = {
        "john doe" : TML_PATH + "john.txt",
        "jane smith" : TML_PATH + "jane.txt",
    }

    # Example ADO Team Information printed to logs
    area_path     = "observability"
    iteration     = "Q1S1"
    story_id      = "098765"
    story_title   = "Science Logic SQL Rules"
    state         = "active"
    project_phase = "Q&A"
    assigned_to   = "john doe"

# module getCustomLogging
Future

# aTest1
    Simple Test program to test the getEpicsTally module
    to return the expected results from the called module.
    All passed data is simulated information and does not 
    reflect any real world information or data.
# aTest2
    Simple Test program to call and test the epics lists array
    iteration and that it returns the expected results. All
    passed data is simulated information and does not reflect
    any real world information or data.


# Disclaimer:
"This script is provided 'as is' and without any warranty, 
express or implied, including but not limited to the implied 
warranties of merchantability, fitness for a particular 
purpose, and non-infringement. I will not be liable for any 
damages, including but not limited to direct, indirect, 
incidental, special, consequential, or punitive damages, 
arising out of the use or inability to use this script, 
even if I have been advised of the possibility of such 
damages." 
