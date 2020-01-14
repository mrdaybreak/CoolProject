import wx
import cv2
from threading import Thread
import numpy as np
from moviepy.editor import *


class getFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, title='修改视频分辨率小工具', size=(380, 220))
        self.panel = wx.Panel(self)
        self.text1 = wx.TextCtrl(self.panel, pos=(30, 100), size=(200, 25))
        self.textw = wx.TextCtrl(self.panel, pos=(120, 30), size=(80, 25))
        self.texth = wx.TextCtrl(self.panel, pos=(120, 65), size=(80, 25))
        self.labelw = wx.StaticText(self.panel, label='宽', pos=(60, 32))
        self.labelh = wx.StaticText(self.panel, label='高', pos=(60, 67))
        self.btn0 = wx.Button(self.panel, label='选择视频', pos=(255, 100), size=(90, 25))
        self.btn1 = wx.Button(self.panel, label='生成', pos=(145, 140), size=(90, 25))
        self.count = 0
        self.btn0.Bind(wx.EVT_BUTTON, self.openfile)
        self.btn1.Bind(wx.EVT_BUTTON, self.changewh)
        # 进度条
        # self.gauge = wx.Gauge(self.panel, -1, 100, pos=(30, 160), size=(320, 30), style=wx.GA_HORIZONTAL)
        # self.gauge.SetBezelFace(3)
        # self.gauge.SetShadowWidth(3)

    def openfile(self, event):
        fileallow = "All files (*.*)|*.*"
        self.dir = wx.FileDialog(self, '选择视频', wildcard=fileallow)
        if self.dir.ShowModal() == wx.ID_OK:
            self.text1.AppendText(self.dir.GetPath())

    def changewh(self, event):
        wx.MessageBox('正在制作中，请安静的等待')
        capture = cv2.VideoCapture(self.dir.GetPath())
        width = int(self.textw.GetValue())
        height = int(self.texth.GetValue())
        fps = capture.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter('./source.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))
        sucess, framecapture = capture.read()
        while sucess:
            # def guagerun():
            #     self.count += 1
            #     if self.count > 100:
            #         self.count = 0
            #     self.gauge.SetValue(self.count)
            # Thread(target=guagerun).start()
            framecapture = cv2.resize(framecapture, (width, height), interpolation=cv2.INTER_CUBIC)
            cv2.putText(framecapture, str(width) + '*' + str(height), (int(float(width)/2.5), int(height/2)),
                        cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255), 2)
            out.write(framecapture)
            sucess, framecapture = capture.read()
        out.release()
        capture.release()
        mv = VideoFileClip(self.dir.GetPath())
        mvsource = VideoFileClip('source.mp4')
        bgm = mv.audio
        addbgmvideo = mvsource.set_audio(bgm)
        addbgmvideo.write_videofile('./{}.mp4'.format(str(width) + '_' + str(height)), codec='mpeg4', audio=True)
        # self.gauge.Hide()
        wx.MessageBox('done')


if __name__ == '__main__':
    app = wx.App()
    frame = getFrame(None)
    frame.Show()
    app.MainLoop()

