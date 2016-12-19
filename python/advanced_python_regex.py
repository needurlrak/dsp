#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:48:05 2016

@author: karlrudeen
"""
import pandas

def unique_degrees():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    faculty_degrees = list(df[' degree'])
    fixed_faculty_degrees = list()
    deg_dict = dict()
    for deg in faculty_degrees:
        if (deg != '0'):
            temp_deg = deg.upper()
            temp_deg = temp_deg.replace('.', '')
            temp_degs = temp_deg.split()
            #the below loop is necessary for faculty members with multiple degrees.
            for degree in temp_degs:
                if (degree in deg_dict):
                    deg_dict[degree] += 1
                else:
                    deg_dict[degree] = 1
            fixed_faculty_degrees = fixed_faculty_degrees + temp_degs #this line is probably pretty inefficient.
    print(len(set(fixed_faculty_degrees)))
    return(deg_dict)
      
def unique_titles():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    faculty_titles = list(df[' title'])
    title_dict = dict()
    for title in faculty_titles:
        if(title in title_dict):
            title_dict[title] += 1
        else:
            title_dict[title] = 1
    return title_dict
    
def print_emails():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    email_list = list(df[' email'])
    print(email_list)
    
def unique_domains():
    facultyfile = open('faculty.csv')
    df = pandas.read_csv(facultyfile)
    email_list = list(df[' email'])
    domain_list = list()
    for address in email_list:
        domain = address[address.index('@'):]
        domain_list.append(domain)
    return(set(domain_list))
    
    
    
    
    
    
