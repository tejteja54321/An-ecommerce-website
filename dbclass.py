import mysql.connector
def getconn():
    conn=mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        port=3307,
        database="yourown")
    return conn

def fetchall(sql):
    conn=getconn()
    cursor=conn.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    return data

def excuteupdate(sql):
    conn=getconn()
    cursor=conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    return True
