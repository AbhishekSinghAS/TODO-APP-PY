"""
[19:38, 3/26/2020] Adarsh Psit: readFile(): reads a file from args #1
formatString(): do tasks like StringSlicing and returns a Dictionary #2
modifyInput(): accepts a dictionary and returns a list of dictionaries

showAllTodo(): prints all todo tasks in a proper way
showSearchedTodoByTime(): prints all todo's according to entered time
showSearchTodoByEvent(): prints all todo's according to entered events
showByStatus(): prints todo's according to entered status
addTodo(): adds new event to the file object
deleteTodoByEvent(): removes eneterd event from the file object
[19:38, 3/26/2020] Adarsh Psit: file name input: args


readFile -> File content list
            args(fileName)
            fileopen return list data
modifyInput-> input list -> output dictionary
              input: data recived from reading file
              dictionary output :
              [{
                  Event: "",
                  Time:"",
                  Status:"done"/"undone"
              }]
showAllTodo -> display all todo formatted
showSearchedTodoByTime -> input time, output todo
showSearchTodoByEvent -> input event, output time +
addTodo-> adds a new event + time
deleteTodo-> input name of event : delete that event
showByStatus : input :done / Undone -> respective todo show
"""
# CODE STARTS HERE #
from sys import argv  
def readfile():                               
    filename,argument=argv
    Var=open(argument,'r')
    tempcontent=Var.readlines()
    Var.close()
    content=[]
    for each in tempcontent:
        each=each.strip()
        content.append(each)
    return content

def formatstring(content):
    list1=[]
    for each in content:
        dictOfTask={}
        Event=each[:each.index('@')]
        Time=each[each.index('@')+1:each.index('#')]
        Status=each[each.index('#')+1:]
        dictOfTask={'event':Event,'Time':Time,'Status':Status}
        list1.append(dictOfTask)
    return list1

def showAllTodo(list1):
    for each in list1:
        Matter=list(each.items())
        for i in range(len(Matter)):
            print(f"{Matter[i][0]}::{Matter[i][1]}")

def showSearchedTodoByTime(list1):
    cnt=0
    Usertime = input("Enter the Task time to search the Task>>")
    for i in range(len(list1)):    
        Lol=list(list1[i].values())
        Matter=list(list1[i].items())
        if Usertime==Lol[1]:
            print(f"{Matter[0][0]}::{Matter[0][1]}")
            print(f"{Matter[1][0]}::{Matter[1][1]}")
            print(f"{Matter[2][0]}::{Matter[2][1]}")
            cnt+=1
    if cnt==0:
        print(">>Their is NO task assgned for this time<<")   

def showSearchedTodoByEvent(list1):
    UserEvent = input("Enter the Task time to search the Task>>")
    cnt=0
    for i in range(len(list1)):    
        Lol=list(list1[i].values())
        Matter=list(list1[i].items())
        if UserEvent==Lol[0]:
            print(f"{Matter[0][0]}::{Matter[0][1]}")
            print(f"{Matter[1][0]}::{Matter[1][1]}")
            print(f"{Matter[2][0]}::{Matter[2][1]}")
            cnt+=1
    if cnt==0:
        print(">>Their is NO task assigned by this event<<")
        

def showByStatus(list1):
    cnt=0
    UserStatus = input("Enter the Task time to search the Task>>")
    for i in range(len(list1)):    
        Lol=list(list1[i].values())
        Matter=list(list1[i].items())
        if UserStatus==Lol[2]:
            print(f"{Matter[0][0]}:: {Matter[0][1]}")
            print(f"{Matter[1][0]}:: {Matter[1][1]}")
            print(f"{Matter[2][0]}:: {Matter[2][1]}")
            cnt+=1
    if cnt==0:
        print(">>Their is NO task assigned by this status<<")

def addTodo():
    userInput="\n"
    n = input("Enter New Task >>with format event@time#ststus<< ")
    userInput+=n
    filename,argument=argv
    Var=open(argument,'a')
    Var.write(userInput)
    Var.close()
    print(">>>>Task Added<<<<")

def deleteTodoByEvent(content):
    cnt=0
    print(content)
    userEvent = input("Enter the Event you want to delete >>>>")
    for each in content:
        Evo = each[:each.index('@')]
        if userEvent==Evo:
            content.remove(each)
            cnt+=1
    if cnt>0:
        newdata=""       
        for data in content:
            newdata+=data
        filename,argument=argv
        Var=open(argument,'w')
        Var.write(newdata)
        Var.close()
        print(">>>>Event deleted<<<<")
    else:
        print(">>Their is NO task by this event<<")
        
filename,argument=argv
var=open(argument,'r')
dlt=var.readlines()
var.close()

fileData=readfile()
Data=formatstring(fileData)
while(1):
    print("Enter 1 if You want to see all Todo's")
    print("Enter 2 if You want to search Todo by Time")
    print("Enter 3 if You want to search Todo by Event")
    print("Enter 4 if You want to search Todo by status")
    print("Enter 5 if You want to Add Extra tasks to Todo")
    print("Enter 6 if You want to Remove task by Event")
    print("To Exit the Program Enter > exit <")
    userInput = input()
    
    if userInput=='1':
        showAllTodo(Data)
    elif userInput=='2':
        showSearchedTodoByTime(Data)
    elif userInput=='3':
        showSearchedTodoByEvent(Data)
    elif userInput=='4':
        showByStatus(Data)
    elif userInput=='5':
        addTodo()
    elif userInput=='6':
        var=open(argument,'r')
        dlt=var.readlines()
        var.close()
        deleteTodoByEvent(dlt)
    elif userInput=='exit':
        from sys import exit
        exit()
    else:
        print("INVALID INPUT  *Enter Again*")
