from Interface import *
import sys

def addContact(file, str1):
    with open (file, 'a') as data:
        data.write(str1 + '\n')

def showAllContacts(file):
    with open (file, 'r') as data:
        print()
        for line in data:
           print(line)
        print()

def searchByLastName(file, str1):
    with open(file, 'r') as data:
        flag = True
        for line in data:
            if str1 in line:
                print(line)
                flag = False
        if flag == True:
            print('No such contact exists. PLease, try again.')

# home tasks

def deleteLine(file, string):
    with open(file, 'r') as data:
        lines = data.readlines()
    with open(file, 'w') as data:
        for line in lines:
            if string not in line:
                data.write(line)

def changeLine(file, searchWord, newContact):
    with open(file, 'r') as data:
        lines = data.readlines()
    with open(file, 'w') as data:
        for line in lines:
            if searchWord in line:
                data.write(newContact)
            else:
                data.write(line)

def cycleMatch(file):
    match getStr(youCanDo):
        case '1':
            addContact(file, getStr(addContactPrompt))
            print(whatsnextPrompt)
            cycleMatch(file)
        case '2':
            showAllContacts(file)
            print(whatsnextPrompt)
            cycleMatch(file)
        case '3':
            searchByLastName(file, getStr(searchPrompt))
            print(whatsnextPrompt)
            cycleMatch(file)
        case '4':
            deleteLine(file, getStr(deletePrompt))
            print(whatsnextPrompt)
            cycleMatch(file)
        case '5':
            changeLine(file, getStr(changePrompt1), getStr(changePrompt2))
            print(whatsnextPrompt)
            cycleMatch(file)
        case '6':
            sys.exit(bye)
        case _:
            print(wrong)
            print(whatsnextPrompt)
            cycleMatch(file)

