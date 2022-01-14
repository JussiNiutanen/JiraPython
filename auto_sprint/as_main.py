'''
@author: Jussi Niutanen
Module to update sprints
'''
import sys

from as_auto_sprint import MyData

print(sys.path)

try:
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
except IndexError:
    sys.exit()

mydata = MyData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
mydata.update_sprints()
