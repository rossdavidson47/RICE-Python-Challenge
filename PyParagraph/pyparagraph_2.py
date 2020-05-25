# This code should be used for the PyParagraph homework for the Rice Bootcamp, May 2020.
# Requires sets of text called paragraph_1, paragraph_2 and paragraph_3_example 
# in the Raw_data sub folder.

#1 Import modules
import os
import re

#2 create lists, variables, dictionaries
txt = []
Word_Count = []
Sentence_Count = []
Space_Count = int(1)
Period_Count = int(0)
Comma_Period_Space_Count = int(0)
Character_Count = int(0)

#3 find file path
txtpath = os.path.join('raw_data','paragraph_2.txt')

#4 Upload and read the text file
txtfile = open(txtpath,'r')
txt=txtfile.read()

#4 Count characters and Comma/Periods/Spaces
for character in txt:
    Character_Count += 1
    if character == ".":
        Period_Count += 1
        Comma_Period_Space_Count += 1
    if character == " ":
        Comma_Period_Space_Count += 1
        Space_Count += 1
    if character == ",":
        Comma_Period_Space_Count += 1

#5 Count words
Word_Count = len(txt.split(" "))
# Word_Count is the same as Space_Count!

#6 Count sentences
Sentence_Count = len(re.split(r"(?<=[.!?]) +", txt))
Sentence_Count = Period_Count
# Sentence_Count is the same as Period_Count!

#7 Print Analysis
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {Word_Count}")
print(f"Approximate Sentence Count: {Sentence_Count}")
print(f"Average Letter Count: {round((Character_Count-Comma_Period_Space_Count)/Word_Count,2)}")
print(f"Average Sentence Length: {round(Word_Count/Sentence_Count,2)}")
