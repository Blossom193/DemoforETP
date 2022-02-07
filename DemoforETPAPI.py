#! /usr/local/bin/python3.8
#_*_ coding: utf-8 _*_
#_*_ coding: gbk _*_
#Author: Collin Liew


import requests
import json

URL = "http://127.0.0.1:8008/api-token-auth/"

paras = {
    "username":"admin",
    "password":"admin",
}


def getcode(link,para):
    req = requests.post(link,para)
    respon = req.json()
    return json.dumps(respon, indent=4, sort_keys=True)

dic_str = getcode(URL, paras)

dic_t = json.loads(dic_str)
for K,V in dic_t.items():
    print(dic_t["token"][1])
rest = list(dic_t.values())
print(rest)

GETur = "http://127.0.0.1:8008/personnel/api/employees/4711971733/"
auth = {
    "Authorization":"Token da328540365716418d22a81947c195a70639e5cd",
    "Content-Type":"application/json",
}

def getUser(GETur,auth):
    obtain = requests.get(GETur,headers=auth)
    resp = obtain.json()
    return json.dumps(resp,indent=4)

dic_PIN = getUser(GETur,auth)
dic_e = json.loads(dic_PIN)
for Ke,Va in dic_e.items():
    print(dic_e["first_name"][1])
ret = list(dic_e.values())

def Convert(list_name):
    for lis in list_name:
        if isinstance(lis,list):
            Convert(lis)
        else:
            print(lis)
Convert(ret)
