import os
from datetime import datetime
import glob
from difflib import SequenceMatcher
print("Press 1 to -Enter Data-")
print("Press 2 to -Get Result-")
print("Press 3 to -Quit-")
def fn1():
    os.chdir(r'C:\\Users\\Aaryyan\\data')
    name=input('Enter the name of the person: ')
    sex=input('Enter the sex of the person: ')
    f=open(f'({sex}) {name}.txt','w')
    num_ques=int(input('Enter the Number of questions: '))
    lst=[]
    n=1
    while num_ques>=n:
        lst.append(f'{n}'+input(f'Enter Answer {n}: '))
        n=n+1
    f.write(str(lst))
    f.close()
    print()
    print()
    
def fn2():
    current_time = datetime.now()
    targets=[]
    original_dir= os.getcwd()
    os.chdir(r'C:\\Users\\Aaryyan\\data')
    for file in glob.glob("*.txt"):
        targets.append(file)
    len_targets=len(targets)
    source_name=input("Enter the name of the source: ")
    sex_name=input("Enter the sex of the source: ")
    print(f'Calculating Compatibility of {source_name.capitalize()} with {len_targets} Participant(s)')
    f=open(f'({sex_name}) {source_name}.txt')
    source=f.readline()        
    source=source.split(',')  
    f.close()
    details=f'''Details of Compatibility Checking:
            No. of Targets : {len_targets}
            Time and Date of execution: {current_time}
            Source File: {source_name.capitalize()}'''
    print('>>'+details)
    n=0
    while n<len_targets:
        f=open(targets[n])
        dest=f.readline()
        f.close()
        dest=dest.split(',')
        results=f'Similarity of {source_name.capitalize()} with {targets[n]} is {SequenceMatcher(None,source, dest).ratio()*100}'+'%'
        print(results)
        n=n+1
    print()
    print()
    
while True:
    a=int(input())
    if a==1:
        fn1()
    elif a==2:
        
        fn2()
    else:
        break
    print("Press 1 to -Enter Data-")
    print("Press 2 to -Get Result-")
    print("Press 3 to -Quit-")
