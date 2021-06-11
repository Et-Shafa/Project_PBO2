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
        self.cursor = self.conn.cursor()  # instantiate a cursor obj

    def executeQuery(self, query, retVal=False):
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.conn.commit()
        if retVal:
            return all_results


class Jenis(DataManager):
    def setDataJenis(self, id_jenis, nama_jenis, harga):
        self.query = 'INSERT INTO jenis (id_jenis, nama_jenis, harga) VALUES (\'%s\', \'%s\', \'%s\')'
        self.query = self.query % (id_jenis, nama_jenis, harga)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataJenis(self):
        self.query = 'SELECT id_jenis, nama_jenis, harga from jenis'
        # self.query = self.query % (id_jenis)
        print('self.query : ', self.query)
        id_jenis = self.executeQuery(self.query, retVal=True)
        return id_jenis


if __name__ == '__main__':
    jns = Jenis()
    daftarJenis = jns.getDataJenis()
    baris = 1
    for jenis_row in daftarJenis:
        print(baris, '. ', jenis_row)
        baris += 1
