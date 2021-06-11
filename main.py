import wx
import view
import model


class tampilLogin(view.Login):
    def __init__(self, parent):
        view.Login.__init__(self, parent)


class tampilhalamanutama(view.halaman_utama):
    def __init__(self, parent):
        view.halaman_utama.__init__(self, parent)
        self.initData()

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
        for col in range(len(koloms)):
            self.dataJenis.SetColLabelValue(col, koloms[col])  # mengubah nama kolom
        self.lstIdPerson = []
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




app = wx.App()
frame = tampilhalamanutama(parent=None)
frame.Show()
app.MainLoop()
