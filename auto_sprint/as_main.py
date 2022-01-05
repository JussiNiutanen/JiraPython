import sys
#import requests
#import json
#from datetime import datetime, timedelta
#import auto_sprints 

#from datetime import date

from auto_sprints import MyData

try:
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
except IndexError:
    print("\n TOO FEW PARAMETERS \n");
    quit();
   
d = MyData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]);
d.update_sprints();


