#! /usr/local/bin/python3.8
#_*_ coding: utf-8 _*_
#_*_ coding: gbk _*_
#Author: Collin Liew

import psycopg2

PG_SQL_LOCAL = {
    "database":"postgres",
    "user":"postgres",
    "password":"123456",
    "port":"7496",
    "host":"localhost",
}

def Connection():
    conn = psycopg2.connect(**PG_SQL_LOCAL)
    print("connection success")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE test6(
        ID INT PRIMARY KEY   NOT NULL,
        NAME      TEXT  NOT NULL,
        PIN      INT   NOT NULL,
        CARD    CHAR(50),
        PWD     CHAR(16));''')
    conn.commit()
    conn.close()
    print("table created")



def InsertOp():
    conn = psycopg2.connect(**PG_SQL_LOCAL)
    cursor = conn.cursor()
    cursor.execute("insert into test5(ID,NAME,PIN,CARD,PWD) values(5,'Sean','1233','1234569','1200907')")
    conn.commit()
    conn.close()
    print("insert the data into your database")

def Delt():
    conn = psycopg2.connect(**PG_SQL_LOCAL)
    cursor = conn.cursor()
    cursor.execute("drop table test3")
    conn.commit()
    cursor.execute("select * from test3")
    row = cursor.fetchone()
    print(row)
    conn.close()


if __name__=='__main__':
    #Connection()
    InsertOp()
    #Delt()