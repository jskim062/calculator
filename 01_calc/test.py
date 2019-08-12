import pymysql
import requests
import json
import tkinter
from tkinter import *
from flask import request

window=tkinter.Tk()
window.title("jskim")
window.geometry("640x400+100+100")
window.resizable(False, False)


m = 0

list1 = []
from flask import Flask, jsonify
app = Flask (__name__)
 
conn = pymysql.connect(host='localhost', user='root', password='blue1004!',
                       db='jskimdb', charset='utf8')

curs = conn.cursor()
@app.route('/useritem/<userName>')
def hello_useritem(userName):
    global list1
    sql = "select * from usertable"
    curs.execute(sql)
    rows = curs.fetchall()
    payload = []
    content = {}
    for result in rows:
        content = {'username': result[0], 'exppoint': result[1], 'userpoint': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)


@app.route('/userexp/<userName>')
def hello_userexp(userName):
    global list1
    sql = "update usertable set userpoint = userpoint + 100, exppoint = exppoint + 100 where username like 'jskim'"
    curs.execute(sql)
    rows = curs.fetchall()
    payload = []
    content = {}
    for result in rows:
        content = {'username': result[0], 'exppoint': result[1], 'userpoint': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/insert/<userName>')
def hello_insert(userName):
    username = request.args.get('username')
    userexp = request.args.get('userexp')
    userpoint = request.args.get('userpoint')
    insert_stmt = (
        "INSERT INTO usertable (username, exppoint, userpoint) "
        "VALUES (%s, %s, %s)"
    )
    data = (conn.escape_string(username), userexp, userpoint)
    curs.execute(insert_stmt, data)
    rows = curs.fetchall()
    payload = []
    content = {}
    for result in rows:
        content = {'username': result[0], 'exppoint': result[1], 'userpoint': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/update/<userName>')
def hello_update(userName):
    username = request.args.get('username')
    userexp = request.args.get('userexp')
    userpoint = request.args.get('userpoint')
    
    #update usertable set userpoint = userpoint + 100, exppoint = exppoint + 100 where username like 'jskim'	
    update_stmt = (
        "update usertable set userpoint = userpoint + (%s), exppoint = exppoint + (%s) where username like (%s)"
    )
    
    data = (userpoint, userexp, conn.escape_string(username))
    #print(update_stmt)
    curs.execute(update_stmt, data)
    rows = curs.fetchall()
    payload = []
    content = {}
    for result in rows:
        content = {'username': result[0], 'exppoint': result[1], 'userpoint': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)


@app.route('/delete/<userName>')
def hello_delete(userName):
    username = request.args.get('username')
    
    #delete from usertable where userpoint = 50
    delete_stmt = (
        "delete from usertable where username like (%s)"
    )
    
    data = (conn.escape_string(username))
   
    curs.execute(delete_stmt, data)
    rows = curs.fetchall()
    payload = []
    content = {}
    for result in rows:
        content = {'username': result[0], 'exppoint': result[1], 'userpoint': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)



if __name__ == "__main__":
    
    app.run()




