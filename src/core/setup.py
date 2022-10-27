"""
This file will always be exectuted by main.py to perform
checks. If all checks are passed, the program will continue.
"""

########
# IMPORTS
########
import sys, os
from typing import Any

import json

########
# CLASSES
########
class installer:
    """
    Used to install have all files in the current directory. Also enables
    things like presets (json).
    """
    #: PRIVATE VARIABLES
    __g_skip = bool

    #: sets everything up for best use. can be skipped
    @classmethod
    def install(update, skip: bool) -> str:
        
        #: set skip to __g_skip
        skip = update.__g_skip

        if skip == True:
            print("[INFO]: Install skipped")

        #: "install" the shit
        elif skip == False:
            
            #: first gets all info
            pass



    #: gets information such as current path
    @classmethod
    def get_info(update, __p):
        __all = {'default_path':''}

        #: get current working directory. this should be the same root directory as all other files
        __p = os.getcwd()

        #: more stuff coming soon...

        #: apply values to dictionary
        __all['default_path'] = __p

        #: dump dict to info.json
        with open('info.json', 'w') as json_dump:
            json.dump(__all, json_dump)



    #: checks if all dependencies are in correct path
    @classmethod
    def check_install(update, __p, skip: bool):

        #: update local skip variable
        if skip == True: update.__g_skip = skip
        else: update.__g_skip = skip   

        #: read data from info.json if data is existent
        if os.path.getsize(os.getcwd+'info.json') > 0:

            #: data exists -> file is read
            with open('info.json', 'r') as json_read:
                json_obj = json.load(json_read)

            __p = json_obj['default_path']

            exists = {}
            for i in os.listdir(__p):
                for j in os.listdir(os.getcwd()):
                    if i == j:
                        exists[i] = True
                    else:
                        exists[i] = False

            with open('info.json', 'a') as json_dump:
                json.dump(exists, json_dump)


        else:
            #: calls the installer instance
            update.install()


    
    #: checks if files currently exist in path or if install should be skipped by default
    @classmethod
    def check(update, skip: bool) -> bool:
        
        #: checks if install should be skipped
        if skip == True:
            return True

        elif skip == False:
            
            #: calls the installer instance
            update.install()


installer = installer()