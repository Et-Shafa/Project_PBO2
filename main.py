import wx
import view
import model
import sys

class tampilLogin(view.Login):
    def __init__(self, parent):
        view.Login.__init__(self, parent)

class tampilTransaksi(view.tampilanTransaksi):
    def __init__(self, parent):
        view.tampilanTransaksi.__init__(self, parent.transaksiPanel)
        # self.initData()
        self.parent = parent
        self.transaksiPanel = parent.transaksiPanel
        # self.jns = parent.jns
        self.lstIdPerson = []
        self.baris = 0
        # self.tampilTambahTransaksi = tampilTambahTransaksi(self)
        # self.tampilTambahPelanggan = tampilTambahPelanggan(self)
        # self.tampilTambahJenis = tampilTambahJenis(self)
        # self.tampilTambahPegawai = tampilTambahPegawai(self)
        # self.tampilTambahTransaksi.Show(False)
        # self.tampilTambahJenis.Show(False)
        # self.tampilTambahPelanggan.Show(False)
        # self.tampilTambahPegawai.Show(False)

    def initData(self):
        n_cols = self.dataJenis.GetNumberCols()
        n_rows = self.dataJenis.GetNumberRows()
        if n_cols > 0:
            self.dataJenis.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.dataJenis.DeleteRows(0, n_rows, True)
        koloms = ['ID', 'Jenis', 'Harga']
        self.dataJenis.AppendCols(len(koloms))
        
        self.jns = model.Jenis()
        daftarJenis = self.jns.getDataJenis()
        baris = 0
        self.lstIdPerson = []
        for col in range(len(koloms)):
            self.dataJenis.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        
        for jenis_row in daftarJenis:
            self.dataJenis.AppendRows(1)
            print(baris, '. ', jenis_row)
            id_jenis,nama_jenis,harga = jenis_row
            self.dataJenis.SetCellValue(baris, 0, id_jenis)
            self.dataJenis.SetCellValue(baris, 1, nama_jenis)
            self.dataJenis.SetCellValue(baris, 2, str(harga))
            # self.dataJenis.SetCellAlignment(wx.ALIGN_CENTER, baris,3 )
            self.lstIdPerson.append(id_jenis)
            baris += 1

    def klikTambahTransaksi( self, event ):
        self.parent.tampilTransaksi(False)
        self.parent.tampilTambahTransaksi(True)

class tampilTambahTransaksi(view.insrtTransaksi):
    def __init__(self, parent):
        view.insrtTransaksi.__init__(self, parent.transaksiPanel)
        self.parent = parent

class tampilTambahTransaksi2(view.insrtTransaksi2):
    def __init__(self, parent):
        view.insrtTransaksi2.__init__(self, parent.transaksiPanel)

class tampilEditTransaksi(view.editTransaksi):
    def __init__(self, parent):
        view.editTransaksi.__init__(self, parent.transaksiPanel)

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

        # self.dataJenis.AutoSize()
        # sz = self.dataJenis.GetSize()
        # self.SetSize(sz.GetWidth() + self.btnTambahJenis.GetSize().GetWidth() + 50, sz.GetHeight() + 100)
        # ~ self.parent.SetMinSize(wx.Size( sz.GetWidth() + self.btnTambah.GetSize().GetWidth()+80, sz.GetHeight() + 180) )
        # ~ self.parent.Layout()
        # self.Layout()

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
            # wx.MessageBox('Edit data', 'Informasi')
            # self.parent.statusBar.SetStatusText('Update data')
            self.parent.tampilEditJenis.id_jenis = id_jenis  # (self.parent, id_person)
            idjenis = self.dataJenis.GetCellValue(baris, 0)
            namajenis = self.dataJenis.GetCellValue(baris, 1)
            hrg = self.dataJenis.GetCellValue(baris, 2)
            self.parent.tampilEditJenis.isiDatajenis(namajenis, hrg)

            self.parent.tampilJenis.Show(False)
            self.parent.tampilEditJenis.Show(True)
        elif kolom == 4:
            # self.parent.statusBar.SetStatusText('Hapus data')
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
        # elif self.inputIdJenis.GetValue() in daftarJenis or self.inputNamaJenis.GetValue() in daftarJenis:
        #     wx.MessageBox('ID atau Nama jenis sudah tersedia', 'Terjadi kesalahan')
        #     return False
        # elif type(self.inputHarga.GetValue()) == str:
        #     wx.MessageBox('Harga yang diinputkan salah', 'Informasi')
        else:
            self.parent.insertDataJenis(self.inputIdJenis.GetValue(), self.inputNamaJenis.GetValue(),
                                      self.inputHarga.GetValue())


        # if self.id_jenis == -1:
        #     self.parent.insertDataJenis(self.inputIdJenis.GetValue(), self.inputNamaJenis.GetValue(),
        #                               self.inputHarga.GetValue())
        # else:
        #     self.parent.updateDataJenis(self.id_person, self.txtNama.GetValue(), self.txtEmail.GetValue(),
        #                               self.txtNim.GetValue())

    

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
            
class tampilPelanggan(view.tampilanPelanggan):
    def __init__(self, parent):
        view.tampilanPelanggan.__init__(self, parent.pelangganPanel)



class tampilTambahPelanggan(view.insrtPelanggan):
    def __init__(self, parent):
        view.insrtPelanggan.__init__(self, parent.pelangganPanel)


class tampilEditPelanggan(view.editPelanggan):
    def __init__(self, parent):
        view.editPelanggan.__init__(self, parent.pelangganPanel)


class tampilPegawai(view.tampilanPegawai):
    def __init__(self, parent):
        view.tampilanPegawai.__init__(self, parent.pegawaiPanel)

class tampilTambahPegawai(view.insrtPegawai):
    def __init__(self, parent):
        view.insrtPegawai.__init__(self, parent.pegawaiPanel)

class tampilEditPegawai(view.editPegawai):
    def __init__(self, parent):
        view.editPegawai.__init__(self, parent.pegawaiPanel)



class tampilhalamanutama(view.halaman_utama):
    def __init__(self, parent):
        view.halaman_utama.__init__(self, parent)
        self.isDebug = False

        self.jns = model.Jenis()
        self.tampilJenis = tampilJenis(self)
        self.tampilTambahJenis = tampilTambahJenis(self)
        self.tampilTambahJenis.Show(False)
        self.tampilEditJenis = tampilEditJenis(self)
        self.tampilEditJenis.Show(False)
        self.tampilJenis.initData()
        self.tampilJenis.addBtnEditDelete()

        # self.transaksi = model.Jenis()
        # self.tampilTransaksi = tampilTransaksi(self)
        # self.tampilTambahTransaksi = tampilTambahTransaksi(self)
        # self.tampilTambahTransaksi.Show(False)
        # self.tampilTransaksi.initData()

        # self.jns = model.Jenis()
        # self.tampilJenis = tampilJenis(self)
        # self.tampilTambahJenis = tampilTambahJenis(self)
        # self.tampilTambahJenis.Show(False)
        # self.tampilJenis.initData()

        # self.jns = model.Jenis()
        # self.tampilJenis = tampilJenis(self)
        # self.tampilTambahJenis = tampilTambahJenis(self)
        # self.tampilTambahJenis.Show(False)
        # self.tampilJenis.initData()

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
