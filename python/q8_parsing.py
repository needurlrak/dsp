# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:07:44 2016

@author: karlrudeen
"""
import pandas

footballfile = open('football.csv')
df = pandas.read_csv(footballfile)
goals = list(df['Goals'])
goals_allowed = list(df['Goals Allowed'])
teams = list(df['Team'])
goal_diff = list()
for i in range(len(goals)):
    goal_diff.append(abs(goals[i] - goals_allowed[i])) 
print(teams[goal_diff.index(min(goal_diff))])