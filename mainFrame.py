# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from NDVI import NDVI
from PIL import Image
import matplotlib.pyplot as plot
import matplotlib.cm as cm

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NDVI", pos = wx.DefaultPosition, size = wx.Size( 1035,681 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"RED" ), wx.VERTICAL )

		sbSizer5.SetMinSize( wx.Size( -1,10 ) )
		self.m_bitmap_red = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 280,280 ), 0 )
		self.m_bitmap_red.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer5.Add( self.m_bitmap_red, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_filePickerB4 = wx.FilePickerCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer5.Add( self.m_filePickerB4, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( sbSizer5, 0, wx.EXPAND, 5 )

		sbSizer52 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Crop Coordinate" ), wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( sbSizer52.GetStaticBox(), wx.ID_ANY, u"Start Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textLonStart = wx.TextCtrl( sbSizer52.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textLonStart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer52.GetStaticBox(), wx.ID_ANY, u"End Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textLonEnd = wx.TextCtrl( sbSizer52.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textLonEnd, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( sbSizer52.GetStaticBox(), wx.ID_ANY, u"Start Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer3.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textLatStart = wx.TextCtrl( sbSizer52.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textLatStart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizer52.GetStaticBox(), wx.ID_ANY, u"End Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer3.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textLatEnd = wx.TextCtrl( sbSizer52.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textLatEnd, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer13.Add( bSizer3, 1, 0, 5 )


		sbSizer52.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_btn_crop = wx.Button( sbSizer52.GetStaticBox(), wx.ID_ANY, u"Crop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer52.Add( self.m_btn_crop, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( sbSizer52, 0, wx.EXPAND, 5 )


		gSizer2.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NIR" ), wx.VERTICAL )

		sbSizer51.SetMinSize( wx.Size( -1,10 ) )
		self.m_bitmap_nir = wx.StaticBitmap( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 280,280 ), 0 )
		self.m_bitmap_nir.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer51.Add( self.m_bitmap_nir, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_filePickerB5 = wx.FilePickerCtrl( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer51.Add( self.m_filePickerB5, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( sbSizer51, 0, wx.EXPAND, 5 )

		sbSizer511 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Metadata" ), wx.HORIZONTAL )

		sbSizer511.SetMinSize( wx.Size( -1,10 ) )
		self.m_filePickerMTL = wx.FilePickerCtrl( sbSizer511.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		sbSizer511.Add( self.m_filePickerMTL, 1, wx.ALL, 5 )


		bSizer9.Add( sbSizer511, 0, wx.EXPAND, 5 )


		gSizer2.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NDVI" ), wx.VERTICAL )

		self.m_bitmap_ndvi = wx.StaticBitmap( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 280,280 ), 0 )
		self.m_bitmap_ndvi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		sbSizer6.Add( self.m_bitmap_ndvi, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_btn_ndvi = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Start NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_btn_ndvi, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( sbSizer6, 0, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"File" ), wx.VERTICAL )

		self.m_btn_save = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_btn_save, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer11.Add( sbSizer3, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		gSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer10.Add( gSizer2, 1, wx.EXPAND, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_HELP,  ), wx.DefaultPosition, wx.Size( 30,30 ), wx.BU_AUTODRAW )
		bSizer10.Add( self.m_bpButton1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_filePickerB4.Bind( wx.EVT_FILEPICKER_CHANGED, self.onB4FileChanged )
		self.m_btn_crop.Bind( wx.EVT_BUTTON, self.onClickCrop )
		self.m_filePickerB5.Bind( wx.EVT_FILEPICKER_CHANGED, self.onB5FileChanged )
		self.m_filePickerMTL.Bind( wx.EVT_FILEPICKER_CHANGED, self.onMTLFileChanged )
		self.m_btn_ndvi.Bind( wx.EVT_BUTTON, self.onClickNDVI )
		self.m_btn_save.Bind( wx.EVT_BUTTON, self.onClickSave )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.onClickHelp )

		self.ndvi = NDVI()
		self.ndvi.SetOnProcessFinishListener(self)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onB4FileChanged( self, event ):
		path = event.GetPath()
		self.ndvi.OpenB4File(path)
		bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
		image = wx.Bitmap.ConvertToImage(bitmap)
		scaledImage = image.Scale(280, 280, wx.IMAGE_QUALITY_HIGH)
		bitmap = wx.Bitmap(scaledImage)
		self.m_bitmap_red.SetBitmap(bitmap)
		event.Skip()

	def onB5FileChanged(self, event):
		path = event.GetPath()
		self.ndvi.OpenB5File(path)
		bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
		image = wx.Bitmap.ConvertToImage(bitmap)
		scaledImage = image.Scale(280, 280, wx.IMAGE_QUALITY_HIGH)
		bitmap = wx.Bitmap(scaledImage)
		self.m_bitmap_nir.SetBitmap(bitmap)
		event.Skip()

	def onClickCrop( self, event ):
		lonStart =  self.m_textLonStart.GetValue()
		lonEnd = self.m_textLonEnd.GetValue()
		latStart = self.m_textLatStart.GetValue()
		latEnd =  self.m_textLatEnd.GetValue()

		self.ndvi.SetCropCoordinate(lonStart, lonEnd, latStart, latEnd)
		self.ndvi.CropImage()

		event.Skip()

	def onMTLFileChanged( self, event ):
		path = event.GetPath()
		self.ndvi.setMetaData(path)
		event.Skip()

	def onClickNDVI( self, event ):
		self.ndvi.StartNDVI()
		event.Skip()

	def onClickSave( self, event ):
		saveFileDialog = wx.FileDialog(frame, 'Save to TIF', '', '', 'GeoTiff Files(*tif)|*.tif', wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

		if (saveFileDialog.ShowModal() == wx.ID_OK):
			path = saveFileDialog.GetPath()
			self.ndvi.SaveResult(path)
			self.ShowMessage("Info", "File has been saved.")
		else:
			self.ShowMessage("Info", "Failed to save file")

		event.Skip()

	def onClickHelp( self, event ):
		self.ShowMessage("Application Info", "Nama: I Gusti Ngurah Dwiva Hardijaya \nNIM   : 1504505079")
		event.Skip()

	def ShowMessage(self, title, message):
		dialog = wx.MessageDialog(None, message, title, wx.OK | wx.ICON_INFORMATION)
		dialog.ShowModal()

	def onCropFinish(self, red, nir):
		red_image = self.convertToImage(red, False)
		nir_image = self.convertToImage(nir, False)

		self.m_bitmap_red.SetBitmap(wx.Bitmap(red_image))
		self.m_bitmap_nir.SetBitmap(wx.Bitmap(nir_image))
		frame.Layout()

	def onNDVIFinish(self, result):
		image = self.convertToImage(result, True)
		self.m_bitmap_ndvi.SetBitmap(wx.Bitmap(image))
		frame.Layout()

	def convertToImage(self, array, isfloat):
		if isfloat:
			rgb = array * 255
		else:
			rgb = array / 255

		pilImage = Image.fromarray(rgb).convert('RGB')
		image = wx.EmptyImage(pilImage.size[0], pilImage.size[1])
		image.SetData(pilImage.tobytes())

		H = image.GetHeight()
		W = image.GetWidth()
		newH = 280
		newW = 280
		if (W > H):
			newH = 280 * H / W
		else:
			newW = 280 * W / H

		image = image.Scale(newW, newH)
		return image


#Mandatory in wx, create an app, False stand for not deteriction stdin/stdout
#refer manual for detail
app = wx.App(False)

#create an object of MyFrame2
frame = MyFrame2(None)
#show the frame
frame.Show(True)
#start the application
app.MainLoop()


