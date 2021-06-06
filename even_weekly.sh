#!/bin/bash
week=$(date +%U)
if [ $(($week % 2)) == 0 ]; then
    # even week / parillinen viikko Alex table
    python3 ~/jira/PythonScripts/auto_sprints.py https://niutanen.atlassian.net/ 20 $1
fi

#odd week / pariton viikko

