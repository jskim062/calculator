import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='blue1004!',
                       db='jskimdb', charset='utf8')
 
curs = conn.cursor()
sql = """update usertable
         set exppoint = exppoint+100 
         where exppoint = exppoint"""
curs.execute(sql)