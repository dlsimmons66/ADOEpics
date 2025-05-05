"""
Simple Test program to test the getEpicsTally module
to return the expected results from the called module
"""

from getEpicsTally import get_epics_tally

epic_arry = "0123456"
total_count = 200
completed = 90
remaining_story_count = 110
percent_complete = (completed/total_count)
CORE_ID = "john_doe"

def main():
    get_epics_tally(epic_arry,total_count,completed,remaining_story_count,percent_complete,CORE_ID)

if __name__ == '__main__':
    main()