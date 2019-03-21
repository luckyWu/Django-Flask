import pymysql

def get_con():
	host = '47.106.211.81'
	port = 3308
	user = 'root'
	password = '123456'
	database = 'whosh'
	db = pymysql.connect(host=host,user=user,password=password,database=database,charset='utf8',port=port)
	return db

def insert(db,cursor,item):
	cursor.execute(query='insert into news(title,content) values (%s,%s)',args=(item['title'],item['content']))
	# print(db)
	db.commit()

def close(db):

	db.close()
