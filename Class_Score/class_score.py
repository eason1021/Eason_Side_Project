"""
File: class_score.py
----------------------------------------------
Author : Yi-Ming Tseng
-----------------------------------------------
Introduction : 
Professor can use the program to conditional randomly pick the students to answer the class questions.
And then give the corresponding scores to the students. The results synchronize to the google sheets automatically.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import os

'''
Set up the maximum score.
The lower someone's score, the higher their chances of being selected.
When the maximum score is reached, the student will no longer be picked.
'''
MAX_CLASS_SCORE = 15
Class = True

def get_weight(sheet):
    #calculate the percentage of the current score of the maximum score
    name = np.array(sheet.col_values(1))
    score = (np.array(sheet.col_values(2))).astype(np.float)
    weight = MAX_CLASS_SCORE - score
    weight = (weight/(np.sum(weight))).astype(np.float)
    
    return name, score, weight

def get_sheet(path, key):
    #Receive the sheet information
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path, gss_scopes)
    gss_client = gspread.authorize(credentials)

    return gss_client.open_by_key(key).sheet1 

path = '/the/json_file_path'
spreadsheet_key = 'google_doc_api_key' 
sheet = get_sheet(path, spreadsheet_key)

while Class:

    #Refresh information
    name, score, weight = get_weight(sheet)
    
    #Pick student
    student = np.random.choice(name, 1, replace = False, p=weight)
    print(student)

    #Adjust the score
    new_score = int(input('How many extra points? (Enter a number): '))
    index = np.where(name == student)
    new_score = new_score + score[index]
    sheet.update_cell(index[0]+1, 2, new_score[0])
        
    #Check the status
    next_one = input('Continue? (Y/N): ').upper()
    if next_one != 'Y':
        Class = False
        os.system('clear')
    else :
        os.system('clear')