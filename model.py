import sqlite3
import sys

# db = 'laundryin.db'
# conn = sqlite3.connect(db)
# cursor = conn.cursor()

# class Data:
# 	def __init__(self):
# 		pass

class DataManager:
    def __init__(self):
        self.isDebug = False
        self.conn = sqlite3.connect('dbLaundry.db')
        self.cursor = self.conn.cursor() # instantiate a cursor obj
    def executeQuery(self, query, retVal=False):
        errMessage = ''
        all_results = ''
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            errMessage = str(sys.exc_info())
            if self.isDebug:
                print('errMessage: ', errMessage)

        if retVal:
            all_results = self.cursor.fetchall()
            return all_results, errMessage
        else:
            return errMessage


class Jenis(DataManager):
    def setDataJenis(self, id_jenis, nama_jenis, harga):
        self.query = 'INSERT INTO jenis (id_jenis, nama_jenis, harga) VALUES (\'%s\', \'%s\', %i)'
        self.query = self.query % (id_jenis, nama_jenis, harga)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

    def getDataJenis(self):
        self.query = 'SELECT id_jenis, nama_jenis, harga from jenis'
        # self.query = self.query % (id_jenis)
        if self.isDebug:
            print('self.query : ', self.query )
        id_jenis, errMsg = self.executeQuery(self.query, retVal=True)
        return id_jenis, errMsg

    def updateDataJenis(self,id_jenis, nama_jenis, harga):
        self.query = 'UPDATE jenis SET nama_jenis=\'%s\', harga= %i where id_jenis = \'%s\'' 
        self.query = self.query % (nama_jenis, harga, id_jenis)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

    def deleteDataJenis(self,id_jenis):
        self.query = 'DELETE FROM jenis where id_jenis = \'%s\'' 
        self.query = self.query % (id_jenis)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

class Pelanggan(DataManager):
    def setDataPelanggan(self,firstname, lastname, nohp, email):
        self.query = 'INSERT INTO pelanggan (firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan) VALUES (%i, \'%s\', \'%s\', \'%s\', \'%s\' )'
        self.query = self.query % (firstname, lastname, nohp, email)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

    def getDataPelanggan(self):
        self.query = 'SELECT id_pelanggan, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan from pelanggan'
        if self.isDebug:
            print('self.query : ', self.query )
        id_pelanggan, errMsg = self.executeQuery(self.query, retVal=True)
        return id_pelanggan, errMsg

    def updateDataPelanggan(self,id_pelanggan,firstname, lastname, nohp, email):
        self.query = 'UPDATE pelanggan SET firstname_pelanggan = \'%s\', lastname_pelanggan = \'%s\', nohp_pelanggan = \'%s\', email_pelanggan = \'%s\' where id_pelanggan = %i' 
        self.query = self.query % (nama_jenis, harga, id_jenis)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

    def deleteDataPelanggan(self,id_pelanggan):
        self.query = 'DELETE FROM pelanggan where id_pelanggan = \'%s\'' 
        self.query = self.query % (id_pelanggan)
        if self.isDebug:
            print('self.query : ', self.query )
        errMsg = self.executeQuery(self.query)
        return errMsg

# class Pegawai(DataManager):
#     def setDataJenis(self, id_jenis, nama_jenis, harga):
#         self.query = 'INSERT INTO jenis (id_jenis, nama_jenis, harga) VALUES (\'%s\', \'%s\', %i)'
#         self.query = self.query % (id_jenis, nama_jenis, harga)
#         if self.isDebug:
#             print('self.query : ', self.query )
#         errMsg = self.executeQuery(self.query)
#         return errMsg

#     def getDataJenis(self):
#         self.query = 'SELECT id_jenis, nama_jenis, harga from jenis'
#         # self.query = self.query % (id_jenis)
#         if self.isDebug:
#             print('self.query : ', self.query )
#         id_jenis, errMsg = self.executeQuery(self.query, retVal=True)
#         return id_jenis, errMsg

#     def updateDataJenis(self,id_jenis, nama_jenis, harga):
#         self.query = 'UPDATE jenis SET nama_jenis=\'%s\', harga= %i where id_jenis = \'%s\'' 
#         self.query = self.query % (nama_jenis, harga, id_jenis)
#         if self.isDebug:
#             print('self.query : ', self.query )
#         errMsg = self.executeQuery(self.query)
#         return errMsg

#     def deleteDataJenis(self,id_jenis):
#         self.query = 'DELETE FROM jenis where id_jenis = \'%s\'' 
#         self.query = self.query % (id_jenis)
#         if self.isDebug:
#             print('self.query : ', self.query )
#         errMsg = self.executeQuery(self.query)
#         return errMsg

# if __name__ == '__main__':
#     jns = Jenis()
#     daftarJenis = jns.getDataJenis()
#     baris = 1
#     for jenis_row in daftarJenis:
#         print(baris, '. ', jenis_row)
#         baris += 1
