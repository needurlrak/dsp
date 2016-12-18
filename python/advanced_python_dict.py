#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:02:10 2016

@author: karlrudeen
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:02:10 2016

@author: karlrudeen
"""

import pandas

def create_faculty_dictionary():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    faculty_dict = dict()
    faculty_names = list(df['name'])
    faculty_first = list()
    faculty_last = list()
    for name in faculty_names:
        temp_first = name[:name.index(' ')]
        temp_last = name[name.rfind(' ') + 1:]
        faculty_first.append(temp_first)
        faculty_last.append(temp_last)
    #print(faculty_first)
    #print(faculty_last)
    
    for i in range(len(faculty_last)):
        info = df.iloc[i]
        if faculty_last[i] in faculty_dict:
            faculty_dict[faculty_last[i]].append([info[' degree'], info[' title'], info[' email']])
        else:
            faculty_dict[faculty_last[i]] = list()
            faculty_dict[faculty_last[i]].append([info[' degree'], info[' title'], info[' email']])

    return faculty_dict
    
fac_dict = create_faculty_dictionary()
print(sorted(fac_dict.items())[:3])
print(" ")


#function for parts 2 and 3   
def create_fullname_dictionary():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    fullname_dict = dict()
    faculty_names = list(df['name'])
    faculty_first = list()
    faculty_last = list()
    for name in faculty_names:
        temp_first = name[:name.index(' ')]
        temp_last = name[name.rfind(' ') + 1:]
        faculty_first.append(temp_first)
        faculty_last.append(temp_last)
        
    for i in range(len(faculty_last)):
        info = df.iloc[i]
        if (faculty_first[i], faculty_last[i]) in fullname_dict:
            fullname_dict[(faculty_first[i],faculty_last[i])] = [info[' degree'], info[' title'], info[' email']]
        else:
            fullname_dict[(faculty_first[i],faculty_last[i])] = list()
            fullname_dict[(faculty_first[i],faculty_last[i])] = [info[' degree'], info[' title'], info[' email']]
            
    #print(fullname_dict.items()[:3])
    return fullname_dict


fulldict = create_fullname_dictionary() 
print(sorted(fulldict.items())[:3])   #output for part 2
print("")
print(sorted(fulldict.items(), key = lambda entry: entry[0][1])) #output for part 3
