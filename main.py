import wx
import view
import model
import sys
from datetime import datetime as dtm

# saat_ini = dtm.now()
# saat_ini =saat_ini.strftime('%d/%m/%Y')
# print(type(saat_ini))


# ====================================================================================================================
# ----------------------------------------------------- Login --------------------------------------------------------
# ====================================================================================================================
class tampilLogin(view.Login):
    def __init__(self, parent):
        view.Login.__init__(self, parent)
        self.isDebug = False
        self.akses = model.ManageLogin()
        self.userPass = model.Pegawai()
        self.parent=parent
        

    def klikLogin( self, event ):
        self.daftarusepas=self.akses.getUsernamePass()
        self.baris = 0
        self.arrid = []
        self.arrUsernames = []
        self.arrPasss = []
        for self.usepas_row in self.daftarusepas:
            for self.a in self.usepas_row:
                self.arrid.append(self.a[0])
                self.arrUsernames.append(self.a[5])
                self.arrPasss.append(self.a[6])
   
        if self.inpUsername.GetValue() == '' or self.inpPass.GetValue()=='':
            wx.MessageBox('Mohon lengkapi data', 'Login gagal')
        elif self.inpUsername.GetValue() in self.arrUsernames:
            indx = self.arrUsernames.index(self.inpUsername.GetValue())
            if self.inpPass.GetValue() == self.arrPasss[indx]:
                saat_ini = dtm.now()
                saat_ini =saat_ini.strftime('%d/%m/%Y')
                # self.catatAkses('coba',111)
                # self.catatAkses(self.arrid[indx], saat_ini)
                errMsg = self.akses.setAkses(self.arrid[indx], saat_ini)

                # self.Destroy()
                # self.halamanUtama = tampilhalamanutama(None)
                # self.halamanUtama.Show()
                # self.parent.catatAkses(self.arrid[indx], self.saat_ini)
                if self.isDebug:
                    print('errMsg: ', errMsg)
                if errMsg != '':
                    wx.MessageBox(errMsg, 'Terjadi kesalahan')
                else:
                    self.Destroy()
                    self.halamanUtama = tampilhalamanutama(None)
                    self.halamanUtama.Show()
            else:
                wx.MessageBox('Password salah', 'Gagal Login')
        else:
            wx.MessageBox('Username atau password salah', 'Gagal Login')


    def catatAkses(self,id_pegawai, tgl_login):
        self.akses.setAkses(id_pegawai, tgl_login)
        # errMsg = self.akses.setAkses(id_pegawai, tgl_login)
        # if self.isDebug:
        #     print('errMsg: ', errMsg)
        # if errMsg != '':
        #     wx.MessageBox(errMsg, 'Terjadi kesalahan')
        # else:
        #     self.Destroy()
        #     # self.halamanUtama = tampilhalamanutama(None)
        #     self.halamanUtama.Show()

# ========================================================================================================================
# ----------------------------------------------------- Transaksi --------------------------------------------------------
# ========================================================================================================================
class tampilTransaksi(view.tampilanTransaksi):
    def __init__(self, parent):
        view.tampilanTransaksi.__init__(self, parent.transaksiPanel)
        self.parent = parent
        self.transaksiPanel = parent.transaksiPanel
        self.transaksi = parent.transaksi
        self.lstIdPerson = []
        self.baris = 0

    def addBtnEditDelete(self):
        jmlKolom = self.dataTransaksi.GetNumberCols()
        self.dataTransaksi.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.dataTransaksi.SetColLabelValue(colEdit, '')
        self.dataTransaksi.SetColLabelValue(colDelete, '')

        for row in range(self.baris):
            self.dataTransaksi.SetCellValue(row, colEdit, 'Edit')
            self.dataTransaksi.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.dataTransaksi.SetCellTextColour(row, colEdit, wx.WHITE)
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, row, colEdit)

            self.dataTransaksi.SetCellValue(row, colDelete, 'Delete')
            self.dataTransaksi.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.dataTransaksi.SetCellTextColour(row, colDelete, wx.WHITE)
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, row, colDelete)
        # self.dataTransaksi.Fit()

        self.dataTransaksi.AutoSize()
        self.Layout()

    def initData(self):
        n_cols = self.dataTransaksi.GetNumberCols()
        n_rows = self.dataTransaksi.GetNumberRows()
        if n_cols > 0:
            self.dataTransaksi.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.dataTransaksi.DeleteRows(0, n_rows, True)
        koloms = ['ID Pegawai', 'ID Pelanggan', 'tglTerima', 'tglSelesai','Total Pakaian', 'Jenis', 'Berat Jenis']
        self.dataTransaksi.AppendCols(len(koloms))
        
        daftarTransaksi, errMsg = self.parent.transaksi.getDataTransaksi()
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')

        self.baris = 0
        self.lstIdPerson.clear()
        for col in range(len(koloms)):
            self.dataTransaksi.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        
        for transaksi_row in daftarTransaksi:
            self.dataTransaksi.AppendRows(1)
            if self.parent.isDebug:
                print(self.baris, '. ', transaksi_row)
            idtransaksi, id_pegawai, id_pelanggan, tglterima, tglselesai, totalpakaian, id_jenis, jumlahberatjenis = transaksi_row
            self.dataTransaksi.SetCellValue(self.baris, 0, id_pegawai)
            self.dataTransaksi.SetCellValue(self.baris, 1, str(id_pelanggan))
            self.dataTransaksi.SetCellValue(self.baris, 2, tglterima)
            self.dataTransaksi.SetCellValue(self.baris, 3, tglselesai)
            self.dataTransaksi.SetCellValue(self.baris, 4, str(totalpakaian))
            self.dataTransaksi.SetCellValue(self.baris, 5, id_jenis)
            self.dataTransaksi.SetCellValue(self.baris, 6, str(jumlahberatjenis))
            self.lstIdPerson.append(idtransaksi)
            self.baris += 1

    def dataTransaksiOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()
        if self.parent.isDebug:
            print('baris: ', baris)
            print('kolom: ', kolom)
        if baris >= self.baris:
            return False
        idtransaksi = self.lstIdPerson[baris]
        if kolom == 7:
            self.parent.tampilEditTransaksi.idtransaksi = idtransaksi  # (self.parent, id_person)
            # id_pegawai = self.dataTransaksi.GetCellValue(baris, 0)
            # id_pelanggan = self.dataTransaksi.GetCellValue(baris, 1)
            # tglterima = self.dataTransaksi.GetCellValue(baris, 2)
            tglselesai = self.dataTransaksi.GetCellValue(baris, 3)
            # totalpakaian = self.dataTransaksi.GetCellValue(baris,4)
            # id_jenis = self.dataTransaksi.GetCellValue(baris, 5)
            # jumlahberatjenis = self.dataTransaksi.GetCellValue(baris, 6)
            # self.parent.tampilEditTransaksi.isiDatatransaksi(id_pegawai,id_pelanggan,tglterima,tglselesai,totalpakaian,id_jenis,jumlahberatjenis)
            self.parent.tampilEditTransaksi.isiDatatransaksi(tglselesai)

            self.parent.tampilTransaksi.Show(False)
            self.parent.tampilEditTransaksi.Show(True)
        elif kolom == 8:
            self.parent.deleteDataTransaksi(idtransaksi)


    def klikTambahTransaksi( self, event ):
        self.parent.tampilTransaksi.Show(False)
        self.parent.tampilTambahTransaksi.Show(True)
        self.parent.tampilTambahJenis.inputIdJenis.SetValue('')
        self.parent.tampilTambahJenis.inputNamaJenis.SetValue('')
        self.parent.tampilTambahJenis.inputHarga.SetValue('')


class tampilTambahTransaksi(view.insrtTransaksi):
    def __init__(self, parent, idtransaksi=-1):
        view.insrtTransaksi.__init__(self, parent.transaksiPanel)
        self.parent = parent
        self.idtransaksi = idtransaksi

    def klikKembali( self, event ):
        self.parent.tampilTambahTransaksi.Show(False)
        self.parent.tampilTransaksi.Show(True)

    def klikLanjut( self, event ):
        if self.inputIdPelanggan.GetValue() == '' or self.inputTotalPakaian.GetValue() == '' or self.datetglTerima.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data sebelum melanjutkan', 'Informasi')
        else:
            # self.idpelanggan = self.inputIdPelanggan.GetValue()
            # self.totalpakaian = self.inputTotalPakaian.GetValue()
            # self.tglterima =self.datetglTerima.GetValue()
            # self.tglselesai = self.datetglSelesai.GetValue()
            self.parent.tampilTambahTransaksi.Show(False)
            self.parent.tampilTambahTransaksi2.Show(True)


class tampilTambahTransaksi2(view.insrtTransaksi2):
    def __init__(self, parent):
        view.insrtTransaksi2.__init__(self, parent.transaksiPanel)
        self.parent=parent

    def btnKembali( self, event ):
        self.parent.tampilTambahTransaksi2.Show(False)
        self.parent.tampilTambahTransaksi.Show(True)

    def btnTambah( self, event ):
        if self.inputJenis.GetValue() == '' or self.inputBeratJenis.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        else:
            self.parent.insertDataTransaksi(self.inputIdPelanggan.GetValue(),self.inputTotalPakaian.GetValue(),
             self.datetglTerima.GetValue(),self.datetglSelesai.GetValue(),self.inputJenis.GetValue(),self.inputBeratJenis.GetValue() )

    def btnHome( self, event ):
        self.parent.tampilTambahTransaksi2.Show(False)
        self.parent.tampilTransaksi.Show(True)

class tampilEditTransaksi(view.editTransaksi):
    def __init__(self, parent):
        view.editTransaksi.__init__(self, parent.transaksiPanel)
        self.parent = parent

    def isiDatatransaksi(self, tglselesai):
        # self.datetglSelesai.SetValue(tglselesai)
        conv= dtm.strptime(tglselesai,'%d-%m-%y %H:%M:%S')
        self.datetglSelesai.SetValue(conv)

    def btnKembali( self, event ):
        self.parent.tampilEditTransaksi.Show(False)
        self.parent.tampilTransaksi.Show(True)

    def btnSimpan( self, event ):
        if self.datetglSelesai.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        else:
            # conv= dtm.strptime(tglselesai,'%Y-%m-%d')
            # self.datetglSelesai.SetValue(conv)
            self.parent.updateDataTransaksi(self.idtransaksi, self.datetglSelesai.GetValue())

# ====================================================================================================================
# ----------------------------------------------------- Jenis --------------------------------------------------------
# ====================================================================================================================
class tampilJenis(view.tampilanJenis):
    def __init__(self, parent):
        view.tampilanJenis.__init__(self, parent.jenisPanel)
        self.parent = parent
        self.jenisPanel = parent.jenisPanel
        self.jns = parent.jns
        self.lstIdPerson = []
        self.baris = 0

    def addBtnEditDelete(self):
        jmlKolom = self.dataJenis.GetNumberCols()
        self.dataJenis.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.dataJenis.SetColLabelValue(colEdit, '')
        self.dataJenis.SetColLabelValue(colDelete, '')

        for row in range(self.baris):
            self.dataJenis.SetCellValue(row, colEdit, 'Edit')
            self.dataJenis.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.dataJenis.SetCellTextColour(row, colEdit, wx.WHITE)
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, row, colEdit)

            self.dataJenis.SetCellValue(row, colDelete, 'Delete')
            self.dataJenis.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.dataJenis.SetCellTextColour(row, colDelete, wx.WHITE)
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, row, colDelete)
        # self.dataJenis.Fit()

        self.dataJenis.AutoSize()
        # sz = self.dataJenis.GetSize()
        # self.SetSize(sz.GetWidth() + self.btnTambahJenis.GetSize().GetWidth() + 50, sz.GetHeight() + 100)
        # self.parent.SetMinSize(wx.Size( sz.GetWidth() + self.btnTambah.GetSize().GetWidth()+80, sz.GetHeight() + 180) )
        # self.parent.Layout()
        self.Layout()

    def initData(self):
        n_cols = self.dataJenis.GetNumberCols()
        n_rows = self.dataJenis.GetNumberRows()
        if n_cols > 0:
            self.dataJenis.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.dataJenis.DeleteRows(0, n_rows, True)
        koloms = ['ID', 'Jenis', 'Harga']
        self.dataJenis.AppendCols(len(koloms))
        
        daftarJenis, errMsg = self.parent.jns.getDataJenis()
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')

        self.baris = 0
        self.lstIdPerson.clear()
        for col in range(len(koloms)):
            self.dataJenis.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        
        for jenis_row in daftarJenis:
            self.dataJenis.AppendRows(1)
            if self.parent.isDebug:
                print(self.baris, '. ', jenis_row)
            id_jenis,nama_jenis,harga = jenis_row
            self.dataJenis.SetCellValue(self.baris, 0, id_jenis)
            self.dataJenis.SetCellValue(self.baris, 1, nama_jenis)
            self.dataJenis.SetCellValue(self.baris, 2, str(harga))
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, baris,3 )
            self.lstIdPerson.append(id_jenis)
            self.baris += 1

    def dataJenisOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()
        if self.parent.isDebug:
            print('baris: ', baris)
            print('kolom: ', kolom)
        if baris >= self.baris:
            return False
        id_jenis = self.lstIdPerson[baris]
        if kolom == 3:
            self.parent.tampilEditJenis.id_jenis = id_jenis
            idjenis = self.dataJenis.GetCellValue(baris, 0)
            namajenis = self.dataJenis.GetCellValue(baris, 1)
            hrg = self.dataJenis.GetCellValue(baris, 2)
            self.parent.tampilEditJenis.isiDatajenis(namajenis, hrg)

            self.parent.tampilJenis.Show(False)
            self.parent.tampilEditJenis.Show(True)
        elif kolom == 4:
            self.parent.deleteDataJenis(id_jenis)

    def klikTambahJenis( self, event ):
        self.parent.tampilJenis.Show(False)
        self.parent.tampilTambahJenis.Show(True)
        self.parent.tampilTambahJenis.inputIdJenis.SetValue('')
        self.parent.tampilTambahJenis.inputNamaJenis.SetValue('')
        self.parent.tampilTambahJenis.inputHarga.SetValue('')


class tampilTambahJenis(view.insrtJenis):
    def __init__(self, parent):
        view.insrtJenis.__init__(self, parent.jenisPanel)
        self.parent = parent

    def btnKembali( self, event ):
        self.parent.tampilTambahJenis.Show(False)
        self.parent.tampilJenis.Show(True)

    def isiDatajenis(self, id_jenis, nama_jenis, harga):
        self.inputIdJenis.SetValue(id_jenis)
        self.inputNamaJenis.SetValue(nama_jenis)
        self.inputHarga.SetValue(harga)

    def btnSimpan( self, event ):
        if self.inputIdJenis.GetValue() == '' or self.inputNamaJenis.GetValue() == '' or self.inputHarga.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False

        else:
            self.parent.insertDataJenis(self.inputIdJenis.GetValue(), self.inputNamaJenis.GetValue(),
                                      self.inputHarga.GetValue())

    

class tampilEditJenis(view.editJenis):
    def __init__(self, parent):
        view.editJenis.__init__(self, parent.jenisPanel)
        self.parent = parent

    def isiDatajenis(self, nama_jenis, harga):
        # self.inputIdJenis.SetValue(id_jenis)
        self.inputNamaJenis.SetValue(nama_jenis)
        self.inputHarga.SetValue(harga)

    def btnSimpan( self, event ):
        if self.inputNamaJenis.GetValue() == '' or self.inputHarga.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        # elif self.inputIdJenis.GetValue() in daftarJenis or self.inputNamaJenis.GetValue() in daftarJenis:
        #     wx.MessageBox('ID atau Nama jenis sudah tersedia', 'Terjadi kesalahan')
        #     return False
        else:
            self.parent.updateDataJenis(self.id_jenis, self.inputNamaJenis.GetValue(),self.inputHarga.GetValue())

    

    def btnKembali( self, event ):
        self.parent.tampilEditJenis.Show(False)
        self.parent.tampilJenis.Show(True)

# ========================================================================================================================
# ----------------------------------------------------- Pelanggan --------------------------------------------------------            
# ========================================================================================================================
class tampilPelanggan(view.tampilanPelanggan):
    def __init__(self, parent):
        view.tampilanPelanggan.__init__(self, parent.pelangganPanel)
        self.parent = parent
        self.pelangganPanel = parent.pelangganPanel
        self.pelanggan = parent.pelanggan
        self.lstIdPerson = []
        self.baris = 0

    def addBtnEditDelete(self):
        jmlKolom = self.dataPelanggan.GetNumberCols()
        self.dataPelanggan.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.dataPelanggan.SetColLabelValue(colEdit, '')
        self.dataPelanggan.SetColLabelValue(colDelete, '')

        for row in range(self.baris):
            self.dataPelanggan.SetCellValue(row, colEdit, 'Edit')
            self.dataPelanggan.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.dataPelanggan.SetCellTextColour(row, colEdit, wx.WHITE)

            self.dataPelanggan.SetCellValue(row, colDelete, 'Delete')
            self.dataPelanggan.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.dataPelanggan.SetCellTextColour(row, colDelete, wx.WHITE)
        #     self.dataPelanggan.SetCellAlignment(wx.ALIGN_CENTER, row, colDelete)
        # self.dataPelanggan.Fit()

        self.dataPelanggan.AutoSize()
        self.Layout()

    def initData(self):
        n_cols = self.dataPelanggan.GetNumberCols()
        n_rows = self.dataPelanggan.GetNumberRows()
        if n_cols > 0:
            self.dataPelanggan.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.dataPelanggan.DeleteRows(0, n_rows, True)
        koloms = ['firstname', 'lastname', 'phone number', 'email']
        self.dataPelanggan.AppendCols(len(koloms))
        
        daftarPelanggan, errMsg = self.parent.pelanggan.getDataPelanggan()
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')

        self.baris = 0
        self.lstIdPerson.clear()
        for col in range(len(koloms)):
            self.dataPelanggan.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        
        for pelanggan_row in daftarPelanggan:
            self.dataPelanggan.AppendRows(1)
            if self.parent.isDebug:
                print(self.baris, '. ', pelanggan_row)
            id_pelanggan, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan = pelanggan_row
            self.dataPelanggan.SetCellValue(self.baris, 0, firstname_pelanggan)
            self.dataPelanggan.SetCellValue(self.baris, 1, lastname_pelanggan)
            self.dataPelanggan.SetCellValue(self.baris, 2, nohp_pelanggan)
            self.dataPelanggan.SetCellValue(self.baris, 3, email_pelanggan)
            self.lstIdPerson.append(id_pelanggan)
            self.baris += 1

    def dataPelangganOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()
        if self.parent.isDebug:
            print('baris: ', baris)
            print('kolom: ', kolom)
        if baris >= self.baris:
            return False
        id_pelanggan = self.lstIdPerson[baris]
        if kolom == 4:
            self.parent.tampilEditPelanggan.id_pelanggan = id_pelanggan  # (self.parent, id_person)
            firstname_pelanggan = self.dataPelanggan.GetCellValue(baris, 0)
            lastname_pelanggan = self.dataPelanggan.GetCellValue(baris, 1)
            nohp_pelanggan = self.dataPelanggan.GetCellValue(baris, 2)
            email_pelanggan = self.dataPelanggan.GetCellValue(baris, 3)
            self.parent.tampilEditPelanggan.isiDatapelanggan(firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan)

            self.parent.tampilPelanggan.Show(False)
            self.parent.tampilEditPelanggan.Show(True)
        elif kolom == 5:
            self.parent.deleteDataPelanggan(id_pelanggan)

    def klikTambahPelanggan( self, event ):
        self.parent.tampilPelanggan.Show(False)
        self.parent.tampilTambahPelanggan.Show(True)
        self.parent.tampilTambahPelanggan.inputFirstName.SetValue('')
        self.parent.tampilTambahPelanggan.inputLastName.SetValue('')
        self.parent.tampilTambahPelanggan.inputNohp.SetValue('')
        self.parent.tampilTambahPelanggan.inputEmail.SetValue('')



class tampilTambahPelanggan(view.insrtPelanggan):
    def __init__(self, parent, id_pelanggan=-1):
        view.insrtPelanggan.__init__(self, parent.pelangganPanel)
        self.parent = parent
        self.id_pelanggan = id_pelanggan

    def btnKembali( self, event ):
        self.parent.tampilTambahPelanggan.Show(False)
        self.parent.tampilPelanggan.Show(True)

    def isiDatapelanggan(self, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan):
        self.inputFirstName.SetValue(firstname_pelanggan)
        self.inputLastName.SetValue(lastname_pelanggan)
        self.inputNohp.SetValue(nohp_pelanggan)
        self.inputEmail.SetValue(email_pelanggan)

    def btnSimpan( self, event ):
        if self.inputFirstName.GetValue() == '' or self.inputNohp.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        else:
            self.parent.insertDataPelanggan(self.inputFirstName.GetValue(), self.inputLastName.GetValue(),
                                            self.inputNohp.GetValue(), self.inputEmail.GetValue())

class tampilEditPelanggan(view.editPelanggan):
    def __init__(self, parent):
        view.editPelanggan.__init__(self, parent.pelangganPanel)
        self.parent = parent

    def isiDatapelanggan(self, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan):
        self.inputFirstName.SetValue(firstname_pelanggan)
        self.inputLastName.SetValue(lastname_pelanggan)
        self.inputNohp.SetValue(nohp_pelanggan)
        self.inputEmail.SetValue(email_pelanggan)

    def btnSimpan( self, event ):
        if self.inputFirstName.GetValue() == '' or self.inputNohp.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        else:
            self.parent.updateDataPelanggan(self.id_pelanggan , self.inputFirstName.GetValue(), self.inputLastName.GetValue(),
                                      self.inputNohp.GetValue(), self.inputEmail.GetValue())

    def btnKembali( self, event ):
        self.parent.tampilEditPelanggan.Show(False)
        self.parent.tampilPelanggan.Show(True)

# ======================================================================================================================
# ----------------------------------------------------- Pegawai --------------------------------------------------------
# ======================================================================================================================
class tampilPegawai(view.tampilanPegawai):
    def __init__(self, parent):
        view.tampilanPegawai.__init__(self, parent.pegawaiPanel)
        self.parent = parent
        self.pegawaiPanel = parent.pegawaiPanel
        self.pegawai = parent.pegawai
        self.lstIdPerson = []
        self.baris = 0

    def addBtnEditDelete(self):
        jmlKolom = self.dataPegawai.GetNumberCols()
        self.dataPegawai.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.dataPegawai.SetColLabelValue(colEdit, '')
        self.dataPegawai.SetColLabelValue(colDelete, '')

        for row in range(self.baris):
            self.dataPegawai.SetCellValue(row, colEdit, 'Edit')
            self.dataPegawai.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.dataPegawai.SetCellTextColour(row, colEdit, wx.WHITE)

            self.dataPegawai.SetCellValue(row, colDelete, 'Delete')
            self.dataPegawai.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.dataPegawai.SetCellTextColour(row, colDelete, wx.WHITE)
        #     self.dataPegawai.SetCellAlignment(wx.ALIGN_CENTER, row, colDelete)
        self.dataPegawai.Fit()

        self.dataPegawai.AutoSize()
        sz = self.dataPegawai.GetSize()
        self.SetSize(sz.GetWidth() + self.btnTambahPegawai.GetSize().GetWidth() + 50, sz.GetHeight() + 100)
        # ~ self.parent.SetMinSize(wx.Size( sz.GetWidth() + self.btnTambah.GetSize().GetWidth()+80, sz.GetHeight() + 180) )
        # ~ self.parent.Layout()
        self.Layout()

    def initData(self):
        n_cols = self.dataPegawai.GetNumberCols()
        n_rows = self.dataPegawai.GetNumberRows()
        if n_cols > 0:
            self.dataPegawai.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.dataPegawai.DeleteRows(0, n_rows, True)
        koloms = ['ID','firstname', 'lastname', 'phone number', 'email']
        self.dataPegawai.AppendCols(len(koloms))
        
        daftarPegawai, errMsg = self.parent.pegawai.getDataPegawai()
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')

        self.baris = 0
        self.lstIdPerson.clear()
        for col in range(len(koloms)):
            self.dataPegawai.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        
        for pegawai_row in daftarPegawai:
            self.dataPegawai.AppendRows(1)
            if self.parent.isDebug:
                print(self.baris, '. ', pegawai_row)
            id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai = pegawai_row
            self.dataPegawai.SetCellValue(self.baris, 0, id_pegawai)
            self.dataPegawai.SetCellValue(self.baris, 1, firstname_pegawai)
            self.dataPegawai.SetCellValue(self.baris, 2, lastname_pegawai)
            self.dataPegawai.SetCellValue(self.baris, 3, nohp_pegawai)
            self.dataPegawai.SetCellValue(self.baris, 4, email_pegawai)
            # self.dataPegawai.SetCellAlignment(wx.ALIGN_CENTER, baris,3 )
            self.lstIdPerson.append(id_pegawai)
            self.baris += 1

    def dataPegawaiOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()
        if self.parent.isDebug:
            print('baris: ', baris)
            print('kolom: ', kolom)
        if baris >= self.baris:
            return False
        id_pegawai = self.lstIdPerson[baris]
        if kolom == 5:
            # wx.MessageBox('Edit data', 'Informasi')
            # self.parent.statusBar.SetStatusText('Update data')
            self.parent.tampilEditPegawai.id_pegawai = id_pegawai  # (self.parent, id_person)
            firstname_pegawai = self.dataPegawai.GetCellValue(baris, 1)
            lastname_pegawai = self.dataPegawai.GetCellValue(baris, 2)
            nohp_pegawai = self.dataPegawai.GetCellValue(baris, 3)
            email_pegawai = self.dataPegawai.GetCellValue(baris, 4)
            self.parent.tampilEditPegawai.isiDatapegawai( firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai)

            self.parent.tampilPegawai.Show(False)
            self.parent.tampilEditPegawai.Show(True)
        elif kolom == 6:
            # self.parent.statusBar.SetStatusText('Hapus data')
            self.parent.deleteDataPegawai(id_pegawai)

    def klikTambahPegawai( self, event ):
        self.parent.tampilPegawai.Show(False)
        self.parent.tampilTambahPegawai.Show(True)
        self.parent.tampilTambahPegawai.inputID.SetValue('')
        self.parent.tampilTambahPegawai.inputFirstName.SetValue('')
        self.parent.tampilTambahPegawai.inputLastName.SetValue('')
        self.parent.tampilTambahPegawai.inputNoHP.SetValue('')
        self.parent.tampilTambahPegawai.inputEmail.SetValue('')
        self.parent.tampilTambahPegawai.inputUsername.SetValue('')
        self.parent.tampilTambahPegawai.inputPassword.SetValue('')

class tampilTambahPegawai(view.insrtPegawai):
    def __init__(self, parent):
        view.insrtPegawai.__init__(self, parent.pegawaiPanel)
        self.parent = parent

    def isiDatapegawai(self, id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai, username, password):
        self.inputID.SetValue(id_pegawai)
        self.inputFirstName.SetValue(firstname_pegawai)
        self.inputLastName.SetValue(lastname_pegawai)
        self.inputNoHP.SetValue(nohp_pegawai)
        self.inputEmail.SetValue(email_pegawai)
        self.inputUsername.SetValue(username)
        self.inputPassword.SetValue(password)

    def btnSimpan( self, event ):
        if self.inputFirstName.GetValue() == '' or self.inputNoHP.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        # elif self.inputIdJenis.GetValue() in daftarJenis or self.inputNamaJenis.GetValue() in daftarJenis:
        #     wx.MessageBox('ID atau Nama jenis sudah tersedia', 'Terjadi kesalahan')
        #     return False
        # elif type(self.inputHarga.GetValue()) == str:
        #     wx.MessageBox('Harga yang diinputkan salah', 'Informasi')
        else:
            self.parent.insertDataPegawai(self.inputID.GetValue(), self.inputFirstName.GetValue(), self.inputLastName.GetValue(),
                                            self.inputNoHP.GetValue(), self.inputEmail.GetValue(),self.inputUsername.GetValue(),
                                            self.inputPassword.GetValue())


        # if self.id_jenis == -1:
        #     self.parent.insertDataJenis(self.inputIdJenis.GetValue(), self.inputNamaJenis.GetValue(),
        #                               self.inputHarga.GetValue())
        # else:
        #     self.parent.updateDataJenis(self.id_person, self.txtNama.GetValue(), self.txtEmail.GetValue(),
        #                               self.txtNim.GetValue())
    def btnKembali( self, event ):
        self.parent.tampilTambahPegawai.Show(False)
        self.parent.tampilPegawai.Show(True)

    

class tampilEditPegawai(view.editPegawai):
    def __init__(self, parent):
        view.editPegawai.__init__(self, parent.pegawaiPanel)
        self.parent = parent

    def isiDatapegawai(self, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai):
        self.inputFirstName.SetValue(firstname_pegawai)
        self.inputLastName.SetValue(lastname_pegawai)
        self.inputNoHP.SetValue(nohp_pegawai)
        self.inputEmail.SetValue(email_pegawai)

    def btnSimpan( self, event ):
        if self.inputFirstName.GetValue() == '' or self.inputNoHP.GetValue() == '':
            wx.MessageBox('Mohon lengkapi data', 'Terjadi kesalahan')
            return False
        # elif self.inputIdJenis.GetValue() in daftarJenis or self.inputNamaJenis.GetValue() in daftarJenis:
        #     wx.MessageBox('ID atau Nama jenis sudah tersedia', 'Terjadi kesalahan')
        #     return False
        # elif type(self.inputHarga.GetValue()) == str:
        #     wx.MessageBox('Harga yang diinputkan salah', 'Informasi')
        else:
            self.parent.updateDataPegawai(self.id_pegawai , self.inputFirstName.GetValue(), self.inputLastName.GetValue(),
                                      self.inputNoHP.GetValue(), self.inputEmail.GetValue())

    def btnkembali( self, event ):
        self.parent.tampilEditPegawai.Show(False)
        self.parent.tampilPegawai.Show(True)


# ============================================================================================================================
# ----------------------------------------------------- Halaman Utama --------------------------------------------------------
# ============================================================================================================================
class tampilhalamanutama(view.halaman_utama):
    def __init__(self, parent):
        view.halaman_utama.__init__(self, parent)
        self.isDebug = False
        # self.akses = model.ManageLogin()
        # self.aself.akses.geAkses()
        # self.tampilUsername.SetValue()

        self.jns = model.Jenis()
        self.tampilJenis = tampilJenis(self)
        self.tampilTambahJenis = tampilTambahJenis(self)
        self.tampilTambahJenis.Show(False)
        self.tampilEditJenis = tampilEditJenis(self)
        self.tampilEditJenis.Show(False)
        self.tampilJenis.initData()
        self.tampilJenis.addBtnEditDelete()

        self.transaksi = model.Transaksi()
        self.tampilTransaksi = tampilTransaksi(self)
        self.tampilTambahTransaksi = tampilTambahTransaksi(self)
        self.tampilTambahTransaksi.Show(False)
        self.tampilTambahTransaksi2 = tampilTambahTransaksi2(self)
        self.tampilTambahTransaksi2.Show(False)
        self.tampilEditTransaksi = tampilEditTransaksi(self)
        self.tampilEditTransaksi.Show(False)
        self.tampilTransaksi.initData()
        self.tampilTransaksi.addBtnEditDelete()

        self.pelanggan = model.Pelanggan()
        self.tampilPelanggan = tampilPelanggan(self)
        self.tampilTambahPelanggan = tampilTambahPelanggan(self)
        self.tampilTambahPelanggan.Show(False)
        self.tampilEditPelanggan = tampilEditPelanggan(self)
        self.tampilEditPelanggan.Show(False)
        self.tampilPelanggan.initData()
        self.tampilPelanggan.addBtnEditDelete()

        self.pegawai = model.Pegawai()
        self.tampilPegawai = tampilPegawai(self)
        self.tampilTambahPegawai = tampilTambahPegawai(self)
        self.tampilTambahPegawai.Show(False)
        self.tampilEditPegawai = tampilEditPegawai(self)
        self.tampilEditPegawai.Show(False)
        self.tampilPegawai.initData()
        self.tampilPegawai.addBtnEditDelete()

    # CRUD Transaksi
    def insertDataTransaksi(self, id_pegawai, id_pelanggan, tglterima, tglselesai, totalpakaian, id_jenis, jumlahberatjenis):
        errMsg = self.transaksi.setDataJenis(id_pegawai, id_pelanggan, tglterima, tglselesai, totalpakaian, id_jenis, jumlahberatjenis)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilTransaksi.Show(True)
            self.tampilTransaksi.Show(False)
            self.tampilTransaksi.initData()
            self.tampilTransaksi.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Jenis berhasil ditambahkan", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def updateDataTransaksi(self, idtransaksi, tglselesai):
        errMsg = self.transaksi.updateDataTransaksi(idtransaksi, tglselesai)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilTransaksi.Show(True)
            self.tampilEditTransaksi.Show(False)
            self.tampilTransaksi.initData()
            self.tampilTransaksi.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Update data jenis berhasil", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def deleteDataTransaksi(self, idtransaksi):
        try:
            dlg = wx.MessageDialog(self, 'Apakah anda yakin akan menghapus data yang dipilih?', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                errMsg = self.jns.deleteDataTransaksi(idtransaksi)
                if errMsg != '':
                    wx.MessageBox(errMsg, 'Terjadi kesalahan')
                else:
                    wx.MessageBox('Hapus data berhasil')
                self.tampilJenis.initData()
                self.tampilJenis.addBtnEditDelete()
        except:
            wx.MessageBox(str(sys.exc_info()), 'Terjadi kesalahan')
            if self.isDebug:
                print('error: ', str(sys.exc_info()))


    # CRUD Jenis
    def insertDataJenis(self, id_jenis, nama_jenis, harga):
        errMsg = self.jns.setDataJenis(id_jenis, nama_jenis, int(harga))
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilJenis.Show(True)
            self.tampilTambahJenis.Show(False)
            self.tampilJenis.initData()
            self.tampilJenis.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Jenis berhasil ditambahkan", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def updateDataJenis(self, id_jenis, nama_jenis, harga):
        errMsg = self.jns.updateDataJenis(id_jenis, nama_jenis, int(harga))
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilJenis.Show(True)
            self.tampilEditJenis.Show(False)
            self.tampilJenis.initData()
            self.tampilJenis.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Update data jenis berhasil", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def deleteDataJenis(self, id_jenis):
        try:
            dlg = wx.MessageDialog(self, 'Apakah anda yakin akan menghapus data yang dipilih?', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                errMsg = self.jns.deleteDataJenis(id_jenis)
                if errMsg != '':
                    wx.MessageBox(errMsg, 'Terjadi kesalahan')
                else:
                    wx.MessageBox('Hapus data berhasil')
                self.tampilJenis.initData()
                self.tampilJenis.addBtnEditDelete()
        except:
            wx.MessageBox(str(sys.exc_info()), 'Terjadi kesalahan')
            if self.isDebug:
                print('error: ', str(sys.exc_info()))

    # CRUD Pelanggan
    def insertDataPelanggan(self, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan):
        errMsg = self.pelanggan.setDataPelanggan(firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilPelanggan.Show(True)
            self.tampilTambahPelanggan.Show(False)
            self.tampilPelanggan.initData()
            self.tampilPelanggan.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Pelanggan berhasil ditambahkan", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def updateDataPelanggan(self, id_pelanggan, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan):
        errMsg = self.pelanggan.updateDataPelanggan(id_pelanggan, firstname_pelanggan, lastname_pelanggan, nohp_pelanggan, email_pelanggan)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilPelanggan.Show(True)
            self.tampilEditPelanggan.Show(False)
            self.tampilPelanggan.initData()
            self.tampilPelanggan.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Update data pelanggan berhasil", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def deleteDataPelanggan(self, id_pelanggan):
        try:
            dlg = wx.MessageDialog(self, 'Apakah anda yakin akan menghapus data yang dipilih?', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                errMsg = self.pelanggan.deleteDataPelanggan(id_pelanggan)
                if errMsg != '':
                    wx.MessageBox(errMsg, 'Terjadi kesalahan')
                else:
                    wx.MessageBox('Hapus data berhasil')
                self.tampilPelanggan.initData()
                self.tampilPelanggan.addBtnEditDelete()
        except:
            wx.MessageBox(str(sys.exc_info()), 'Terjadi kesalahan')
            if self.isDebug:
                print('error: ', str(sys.exc_info()))


    # CRUD Pegawai
    def insertDataPegawai(self, id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai, username, password):
        errMsg = self.pegawai.setDataPegawai(id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai, username, password)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilPegawai.Show(True)
            self.tampilTambahPegawai.Show(False)
            self.tampilPegawai.initData()
            self.tampilPegawai.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Pegawai berhasil ditambahkan", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def updateDataPegawai(self, id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai):
        errMsg = self.pegawai.updateDataPegawai(id_pegawai, firstname_pegawai, lastname_pegawai, nohp_pegawai, email_pegawai)
        if self.isDebug:
            print('errMsg: ', errMsg)
        if errMsg != '':
            wx.MessageBox(errMsg, 'Terjadi kesalahan')
        else:
            self.tampilPegawai.Show(True)
            self.tampilEditPegawai.Show(False)
            self.tampilPegawai.initData()
            self.tampilPegawai.addBtnEditDelete()
            dlg= wx.MessageDialog(self, "Update data pegawai berhasil", "Informasi", style=wx.YES_DEFAULT)
            dlg.ShowModal()

    def deleteDataPegawai(self, id_pegawai):
        try:
            dlg = wx.MessageDialog(self, 'Apakah anda yakin akan menghapus data yang dipilih?', 'Informasi', style=wx.YES_NO)
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                errMsg = self.pegawai.deleteDataPegawai(id_pegawai)
                if errMsg != '':
                    wx.MessageBox(errMsg, 'Terjadi kesalahan')
                else:
                    wx.MessageBox('Hapus data berhasil')
                self.tampilPegawai.initData()
                self.tampilPegawai.addBtnEditDelete()
        except:
            wx.MessageBox(str(sys.exc_info()), 'Terjadi kesalahan')
            if self.isDebug:
                print('error: ', str(sys.exc_info()))

    def klikProfil( self, event ):
        event.Skip()

    def klikLogout( self, event ):
        dlg = wx.MessageDialog(self, "Apakah anda yakin akan Logout dari apalikasi", "Logout", style=wx.YES_NO)
        pilih = dlg.ShowModal()
        if pilih == wx.ID_YES:
            self.Destroy()
            tampilLogin(None).Show()
        else:
            pass


app = wx.App()
frame = tampilhalamanutama(parent=None)
frame.Show()
app.MainLoop()



