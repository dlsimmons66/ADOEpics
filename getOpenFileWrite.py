#! /usr/bin/env python3
# written by David Simmons
# Version 2.0 - 5/2/2025

'''
This module creates log files defined in the parameters passed
to the module. The parameters of 'filepath' and 'message' are 
required to be passed from within the main program. 

This modules does not return any values; it simply creates the
initial files for logging.
'''

def openFileWrite(message, file_path):
    with open(file_path, 'w') as write_file:
        write_file.writelines(message)
