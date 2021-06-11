import wx
import view

class tampilLogin(view.Login):
	def __init__(self, parent):
		view.Login.__init__(self, parent)

class tampilhalamanutama(view.halaman_utama):
	def __init__(self,parent):
		view.halaman_utama.__init__(self,parent)



app = wx.App()
frame = tampilhalamanutama(parent=None)
frame.Show()
app.MainLoop()
