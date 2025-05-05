#! /usr/bin/env python3
# written by David Simmons
# Version 2.0 - 5/2/2025

from getOpenFileWrite import openFileWrite
import datetime, pytz

# Date & Time setup for Logging
now = datetime.datetime.now(pytz.timezone("America/Chicago"))
now_str = now.strftime('%Y-%m-%d %H:%M:%S %Z')
today = now.strftime('%m.%d.%Y')

"""
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
"""

def get_epics_tally(epic_arry, total_cnt, completed, remaining_story_count, percent_completed,CORE_ID,project_logs):

    try:
        msg_header = ("\n" + "-"*30 + "\n")
        msg = ("#"*5 + " " + str(epic_arry) + " " + "#"*5 +
                   "\nTotal Ticket Count: " + str(total_cnt) + 
                   "\nCompleted Story Count: " + str(completed) + 
                   "\nRemaining Stories: " + str(remaining_story_count) +
                   "\nPercent Completed: {:.2%}".format(percent_completed)
                    )
        msg_footer = ("\n" + "-"*30 + "\n")
        message = msg_header + msg + msg_footer
        openFileWrite(message,project_logs)
        return
    
    except Exception as e:
        print(f"There was an exception in '{get_epics_tally.__module__}' : ", e)