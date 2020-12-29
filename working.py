import time
import threading 
from threading import*

Dict={}

def create(key,key_value,timing=0):
    if key in Dict:
        print("ERROR: Key Already Exist")
    else:
        if(isinstance(key, str) and key !=""):
            if len(Dict)<(1024*1020*1024) and key_value<=(16*1024*1024):
                if timing==0:
                    Value=[key_value,timing]
                else:
                    Value=[key_value,time.time()+timing]
                if len(key)<=32:
                    Dict[key]=Value
            else:
                print("ERROR: Exceeding Memory ")
        else:
            print("ERROR: Key Name Is Not Valid. Enter Only Strings")

def read(key):
    if key not in Dict:
        print("ERROR: Key Name Is Not Present IN Data. Enter Valid Key")
    else:
        Value=Dict[key]
        if Value[1]!=0:
            if time.time()<Value[1]:
                data='{ "'+str(key)+'"'+" : "+str(Value[0])+' }'
                return data
            else:
                print("ERROR: Time-To-Live-For",key,"Has Expired")
        else:
            data='{ "'+str(key)+'"'+" : "+str(Value[0])+' }'
            return data


def delete(key):
    if key not in Dict:
        print("ERROR: Key Name Is Not Present IN Data. Enter Valid Key")
    else:
        b=Dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del Dict[key]
                print("key Deleted")
            else:
                print("ERROR: Time-To-Live-For",key,"Has Expired")
        else:
            del Dict[key]
            print("key Deleted")

##########################################################################3

while(True):
    value=input("1 to create. 2 to read. 3 to delete and 4 to exit : ")
    if(value=="1"):
        key=input("enter key : ")
        num=int(input("enter num : "))
        times=input("enter time optional : ")
        if(times==''):
            times=0
        else:
            times=int(times)
        #tim=int(time)
        create(key,num,times)
    if(value=="2"):
        key=input("enter key to read : ")
        print(read(key))
    if(value=="3"):
        key=input("enter key to read : ")
        print(delete(key))
    if(value=="4"):
        break
