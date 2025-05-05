import datetime, pytz

"""
This module creates log files for the team members listed
in the 'Team Member Log' (TML) Array from within the main
program getTeamEpics.

Each logfile is prefixed with a date & time stamp which is 
over-written if the script is run mulitple times during a
day. 

This modules does not return any values; it simply creates the
initial files for logging.
"""

# Date & Time for Logging
now = datetime.datetime.now(pytz.timezone("America/Chicago"))
now_str = now.strftime('%Y-%m-%d %H:%M:%S %Z')
today = now.strftime('%m.%d.%Y')

def openTeamLogs(now_str,TML):
    char1 = "#"
    repeated = 15
    seperators = f"{'':{char1}>{repeated}}"

    try:
        for key in TML.keys():
            with open(TML[key], 'w') as Team_Log:
                message = f"{seperators}  Date: {now_str}  {seperators}\n"
                Team_Log.writelines(message) 
    except Exception as e:
        print(f"There was an exception in '{openTeamLogs.__module__}' : ", e)