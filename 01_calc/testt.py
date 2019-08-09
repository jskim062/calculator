import pymysql


list1 = []
from flask import Flask, jsonify
app = Flask (__name__)
 
conn = pymysql.connect(host='localhost', user='CHANGEHERE', password='CHANGEHERE',
                       db='CHANGEHERE', charset='utf8')

curs = conn.cursor()

apple = 0

@app.route('/')
def hello_world():
    return 'Hello, World!'
 
@app.route('/user/<userName>')
def hello_user(userName):
    return 'Hello, %s'%(userName)

@app.route('/item/<userName>')
def hello_saveitem(userName):
    global apple
    apple = apple + 1
    data = {'name' : 'Aaron', 'family' : 'Byun'}
    return jsonify(data)
    
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




if __name__ == "__main__":
    app.run()
