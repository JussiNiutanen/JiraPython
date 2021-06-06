import sys
#import requests
#import json
#from datetime import datetime, timedelta
#import auto_sprints 

from datetime import date

from auto_sprints import MyData

weekNumber = date.today().isocalendar()[1];
if(0==weekNumber%2):
    print("Week number parillinen:", weekNumber);
else:
    print("Week number pariton:", weekNumber);
    quit();

try:
    sys.argv[1], sys.argv[2]
except IndexError:
    print("\n TOO FEW PARAMETERS \n");
    quit();
   
d = MyData(sys.argv[1],sys.argv[2]);
d.update_sprints();


