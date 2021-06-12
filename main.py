import wx
import view
import model


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

class tampilJenis(view.tampilanJenis):
    def __init__(self, parent):
        view.tampilanJenis.__init__(self, parent.jenisPanel)
        self.parent = parent
        self.jenisPanel = parent.jenisPanel
        self.jns = parent.jns
        self.lstIdPerson = []
        self.baris = 0

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

    def klikTambahJenis( self, event ):
        self.parent.tampilJenis.Show(False)
        self.parent.tampilTambahJenis.Show(True)


class tampilTambahJenis(view.insrtJenis):
    def __init__(self, parent):
        view.insrtJenis.__init__(self, parent.jenisPanel)
        self.parent = parent

    def btnKembali( self, event ):
        self.parent.tampilTambahJenis.Show(False)
        self.parent.tampilJenis.Show(True)

    def btnSimpan( self, event ):
        event.Skip()

class tampilPelanggan(view.tampilanPelanggan):
    def __init__(self, parent):
        view.tampilanPelanggan.__init__(self, parent.pelangganPanel)

class tampilTambahPelanggan(view.insrtPelanggan):
    def __init__(self, parent):
        view.insrtPelanggan.__init__(self, parent.pelangganPanel)


class tampilPegawai(view.tampilanPegawai):
    def __init__(self, parent):
        view.tampilanPegawai.__init__(self, parent.pegawaiPanel)

class tampilTambahPegawai(view.insrtPegawai):
    def __init__(self, parent):
        view.insrtPegawai.__init__(self, parent.pegawaiPanel)

class tampilhalamanutama(view.halaman_utama):
    def __init__(self, parent):
        view.halaman_utama.__init__(self, parent)
        self.isDebug = False

        self.jns = model.Jenis()
        self.tampilJenis = tampilJenis(self)
        self.tampilTambahJenis = tampilTambahJenis(self)
        self.tampilTambahJenis.Show(False)
        self.tampilJenis.initData()

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
