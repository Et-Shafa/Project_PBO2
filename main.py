import wx
import view
import model


class tampilLogin(view.Login):
    def __init__(self, parent):
        view.Login.__init__(self, parent)

class tampilTambahTransaksi(view.insrtTransaksi):
    def __init__(self, parent):
        view.insrtTransaksi.__init__(self, parent.transaksi)
        self.parent = parent

class tampilTambahTransaksi2(view.insrtTransaksi2):
    def __init__(self, parent):
        view.insrtTransaksi2.__init__(self, parent)

class tampilTambahJenis(view.insrtJenis):
    def __init__(self, parent):
        view.insrtJenis.__init__(self, parent)

class tampilTambahPelanggan(view.insrtPelanggan):
    def __init__(self, parent):
        view.insrtPelanggan.__init__(self, parent)

class tampilTambahPegawai(view.insrtPegawai):
    def __init__(self, parent):
        view.insrtPegawai.__init__(self, parent)

class tampilhalamanutama(view.halaman_utama):
    def __init__(self, parent):
        view.halaman_utama.__init__(self, parent)
        self.initData()
        self.parent = parent
        self.tampilTambahTransaksi = tampilTambahTransaksi(self)
        self.tampilTambahPelanggan = tampilTambahPelanggan(self)
        self.tampilTambahJenis = tampilTambahJenis(self)
        self.tampilTambahPegawai = tampilTambahPegawai(self)
        self.tampilTambahTransaksi.Show(False)
        self.tampilTambahJenis.Show(False)
        self.tampilTambahPelanggan.Show(False)
        self.tampilTambahPegawai.Show(False)

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

    def klikTambahTransaksi( self, event ):
        self.tampilTambahTransaksi.Show(True)
        self.transaksi.Show(False)

    def klikTambahJenis( self, event ):
        event.Skip()

    def klikTambahPelanggan( self, event ):
        event.Skip()

    def klikTambahPegawai( self, event ):
        event.Skip()





app = wx.App()
frame = tampilhalamanutama(parent=None)
frame.Show()
app.MainLoop()
