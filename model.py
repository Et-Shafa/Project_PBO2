import sqlite3

# db = 'laundryin.db'
# conn = sqlite3.connect(db)
# cursor = conn.cursor()

# class Data:
# 	def __init__(self):
# 		pass

class DataManager:
	def __init__(self):
		self.conn = sqlite3.connect('dbLaundry.db')
		self.cursor = self.conn.cursor() # instantiate a cursor obj
	def executeQuery(self, query, retVal=False):
		self.cursor.execute(query)
		all_results = self.cursor.fetchall()
		self.con.commit()
		if retVal:
			return all_results