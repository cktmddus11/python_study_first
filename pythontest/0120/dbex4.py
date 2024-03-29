'''
Created on 2020. 1. 20.

@author: GDJ_19
mariadb에 데이터 입력하기
'''
import pymysql
conn = pymysql.connect(host="localhost", port=3306, 
                       user="scott", passwd="1234", db="classdb", charset="utf8")
cur = conn.cursor()
data = [(15, "바나나", 3000, "바나나는 길다"), 
        (16, "망고", 30000, "망고는 열대 과일이다."),
        (17, "사과", 10000, "사과는 많이 먹자")]
for i in data:
    cur.execute('''
        insert into item (id, name, price, description)
        values (%s, %s, %s, %s)
    ''', i)
#conn.commit()
cur.execute("select *from item")
for row in cur.fetchall():
    print(row)
conn.rollback()
