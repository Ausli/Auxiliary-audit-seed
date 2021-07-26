from tkinter import messagebox,Label,Button
import tkinter as tk
import os
from tkinter import scrolledtext
from cookie_test import cookie_test
from start_check import start_process
import re

class MyApp (object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.protocol ("WM_DELETE_WINDOW", self.on_closing)
        self.root.geometry ('350x300')
        self.root.resizable (0, 0)
        self.root.title ("lemon审核工具")
        self.frame = tk.Frame (parent)
        self.btn = tk.Button (self.frame, text="开始审核", height=3,
                              width=19, fg='red', command=self.openFrame)
        self.insert_photo ()
        self.check_Cookie ()
        self.frame.place (x=208, y=240)


    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw ()

    # ----------------------------------------------------------------------
    def on_closing(self):
        self.close = 'Quit'
        if messagebox.askokcancel (self.close, "Do you want to quit?", ):
            self.root.destroy ()

    def openFrame(self):
        """"""
        self.hide ()
        otherFrame = tk.Toplevel ()
        otherFrame.geometry ("700x300")
        otherFrame.resizable (0, 0)
        otherFrame.title ("lemon审核", )
        otherFrame.protocol ("WM_DELETE_WINDOW", self.on_closing)

        handler = lambda: self.onCloseOtherFrame (otherFrame)
        self.url_txt = tk.Entry (otherFrame, width=65)
        self.url_txt.place (x=25)
        Label (otherFrame, text="url:", font=('微软雅黑', '10')).place (x=0, y=0)
        check = tk.Button (otherFrame, text="check", width=12, height=5, command=lambda: btn_func ())
        check.place (x=607, y=202)
        btn = tk.Button (otherFrame, text="back", command=handler)
        btn.place (x=620, y=152, width=80, height=50)
        # -----------------------------------------------------------------------
        Text1 = Label (otherFrame, text='标题：')
        Text2 = Label (otherFrame, text='副标题：')
        Text3 = Label (otherFrame, text='类型：')
        Text4 = Label (otherFrame, text='详细信息：')
        Text5 = Label (otherFrame, text='媒介检查：')
        Text6 = Label (otherFrame, text='编码检查：')
        Text7 = Label (otherFrame, text='音频检查：')
        Text8 = Label (otherFrame, text='分辨率检查：')
        Text9 = Label (otherFrame, text='地区检查：')
        Text10 = Label (otherFrame, text='制作组检查：')
        Text11 = Label (otherFrame, text='标签检查：')
        Text12 = Label (otherFrame, text='链接及info检查：')
        Text13 = Label (otherFrame, text='全局检查：', font=('微软雅黑', '20'))
        Text14 = Label (otherFrame, text='', fg='red')
        Text1.place (y=25), Text2.place (y=45), Text3.place (y=65), Text4.place (y=85)
        Text5.place (y=105), Text6.place (x=300, y=105), Text7.place (y=125), Text8.place (x=300, y=125)
        Text9.place (y=145), Text10.place (x=300, y=145), Text11.place (y=165), Text12.place (y=185)
        Text13.place (x=200, y=265), Text14.place (x=500)

        # ----------------------------------------------------------------------
        # Label_nums()
        def btn_func():
            """按键的触发事件"""
            url_search = re.search ('lemonhd.org', self.url_txt.get ())
            try:
                if url_search:
                    input_data = start_process (self.url_txt.get ())
                    Text14['text'] = ''
                    Text1['text'] = '标题：' + input_data[0]
                    Text2['text'] = '副标题：' + input_data[1]
                    Text3['text'] = '类型：' + input_data[2]
                    Text4['text'] = '详细信息：' + str (input_data[3])
                    Text5['text'] = '媒介检查：' + input_data[4]
                    Text6['text'] = '编码检查：' + input_data[5]
                    Text7['text'] = '音频检查：' + input_data[6]
                    Text8['text'] = '分辨率检查：' + input_data[7]
                    Text9['text'] = '地区检查：' + input_data[8]
                    Text10['text'] = '制作组检查：' + input_data[9]
                    Text11['text'] = '标签检查：' + input_data[10]
                    Text12['text'] = '链接及info检查：' + input_data[11]
                    pass_false = re.search ('错误', str (input_data))
                    pass_Confirm = re.search ('待确认', str (input_data))
                    if pass_false:
                        Text13['text'] = '全局检查：检查有错误发生'
                        Text13['fg'] = 'red'
                    elif pass_Confirm:
                        Text13['text'] = '全局检查：标签待确认'
                    else:
                        Text13['text'] = '全局检查：全部正常'
                else:
                    Text14['text'] = '请输入正确的url'
            except:
                Text14['text'] = '请输入正确的url'

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy ()
        self.show ()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update ()
        self.root.deiconify ()

    # ----------------------------------------------------------------------
    def insert_photo(self):
        from logo import img_data
        from base64 import b64decode
        def get_pic(pic_code, pic_name):
            image = open (pic_name, 'wb')
            image.write (b64decode (pic_code))
            image.close ()

        get_pic (img_data, 'logo.png')
        global photo
        photo = tk.PhotoImage (file='logo.png')
        theLabel = tk.Label (self.root,
                             image=photo,  # 加入图片
                             compound='bottom')
        theLabel.pack ()
        os.remove ('logo.png')

    # ----------------------------------------------------------------------
    def check_Cookie(self):
        lbl = Label (self.root, text="Cookie:")
        lbl.place (x=0, y=160)
        txt = scrolledtext.ScrolledText (self.root, width=40, height=9)
        txt.place (x=50, y=110)
        checkrequest = Label (self.root, text="点击添加Cookie", font=('微软雅黑', '13'))
        if os.path.exists ('cookie.txt'):
            if len (open ('cookie.txt').read ()) > 10:
                checkrequest.configure (text="已保存cookie，请测试")
                self.btn.pack ()
        checkrequest.place (x=0, y=240)
        click_ = Button (self.root, text="Click Me", width=20, command=lambda: self.clicked (checkrequest, txt))
        click_.place (y=270)

    # ----------------------------------------------------------------------
    def clicked(self, checkrequest, txt):
        if os.path.exists ('cookie.txt'):
            test_cookie = cookie_test (open ('cookie.txt').read ())
            if test_cookie is True:
                checkrequest.configure (text="状态正常")
                self.btn.pack ()
                return True
            elif test_cookie is TimeoutError:
                checkrequest.configure (text="网络异常")
            else:
                checkrequest.configure (text="状态异常,请测试cookie")
                return False
        else:
            insert_cookie = txt.get (1.0, 'end').strip ('\n')
            if len (insert_cookie) < 20:
                checkrequest.configure (text="无cookie")
                return False
            test_cookie2 = cookie_test (insert_cookie)
            print (insert_cookie)
            print (test_cookie2)
            if test_cookie2 is TimeoutError:
                checkrequest.configure (text="网络异常")
                return False
            elif test_cookie2 is True:
                checkrequest.configure (text="状态正常")
                self.btn.pack ()
                return True
            else:
                checkrequest.configure (text="状态异常,请测试cookie")
                return False


if __name__ == '__main__':
    root = tk.Tk ()
    app = MyApp (root)
    root.mainloop ()
