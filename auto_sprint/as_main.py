'''
@author: Jussi Niutanen
Module to update sprints
'''
import sys

from auto_sprints import MyData

try:
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
except IndexError:
    sys.exit()

d = MyData(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
d.update_sprints()
