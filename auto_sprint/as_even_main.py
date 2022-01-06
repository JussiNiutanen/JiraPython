'''
@author: Jussi Niutanen
Module to close and start sprints bi-weekly
'''

import sys
from datetime import date
from auto_sprints import MyData

weekNumber = date.today().isocalendar()[1]
if 0==weekNumber%2:
    print("Week number parillinen:", weekNumber)
else:
    print("Week number pariton:", weekNumber)
    sys.exit()

try:
    sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4]
except IndexError:
    sys.exit()

d = MyData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
d.update_sprints()
