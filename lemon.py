from tkinter import messagebox,Label,Button
import tkinter as tk
from tkinter import BOTTOM
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
        self.root.protocol ("WM_DELETE_checkFrame", self.on_closing)
        self.root.geometry ('700x300')
        self.root.resizable (0, 0)
        self.root.title ("lemon审核工具")
        #self.frame = tk.Frame (parent)
        self.start_check_btn = tk.Button (self.root, text="开始审核", height=3,
                              width=19, fg='red', command=self.openFrame)
        self.insert_photo ()
        self.check_Cookie ()
        #self.frame.place (x=208, y=240)


    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw ()

    # ----------------------------------------------------------------------
    def on_closing(self):
        self.close = 'Quit'
        if messagebox.askokcancel (self.close, "Do you want to quit?", ):
            self.root.destroy ()

    # ----------------------------------------------------------------------
    def check_Frame(self,url):
        checkFrame = tk.Toplevel()
        checkFrame.geometry("300x230")
        #checkFrame.resizable(0, 0)
        checkFrame.title("审核", )
        var = tk.StringVar()  # 创建变量var 用来将 radiobutton 的值和 Label 的值联系在一起
        l = tk.Label(checkFrame,
                     bg='yellow',
                     width=25,
                     text='请选择审核结果，默认审核通过')
        l.pack()
        var.set('通过')
        def print_selection():
            l.config(text='审核 ' + var.get())
        r1 = tk.Radiobutton(checkFrame,
                            text='通过',
                            # 当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
                            variable=var,
                            value='通过',
                            command=print_selection,
                            )
        r1.place(x=75,y=25)
        r2 = tk.Radiobutton(checkFrame,
                            text='不通过',
                            variable=var,
                            value='不通过',
                            command=print_selection
                            )
        r2.place(x=150,y=25)
        check_txt =  scrolledtext.ScrolledText (checkFrame, width=40, height=10)
        check_txt.place(y=50)
        from pyhtml.lemon_check_submit import check_submit
        def submit_check():
            if var.get() =='通过':
                s=check_submit(url,'ok')
            else:
                s=check_submit(url, 'fail',check_txt.get(1.0, 'end').strip('\n'))
            self.Text13['text']='操作成功' if s == 200 else '操作失败'
            checkFrame.withdraw()


        check_submit_btn = tk.Button(checkFrame, text="提交", width=8, height=1,command=lambda: submit_check())
        check_submit_btn.pack(side=BOTTOM)
    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide ()
        otherFrame = tk.Toplevel ()
        otherFrame.geometry ("700x300")
        otherFrame.resizable (0, 0)
        otherFrame.title ("lemon审核", )
        otherFrame.protocol ("WM_DELETE_checkFrame", self.on_closing)
        self.url_txt = tk.Entry (otherFrame, width=65)
        self.url_txt.place (x=25)
        Label (otherFrame, text="url:", font=('微软雅黑', '10')).place (x=0, y=0)
        check = tk.Button (otherFrame, text="check", width=12, height=5, command=lambda: btn_func ())
        check.place (x=608, y=204)
        btn = tk.Button (otherFrame, text="back", command=lambda: self.onCloseOtherFrame (otherFrame))#Approved  Audit failed
        btn.place (x=607, y=0, width=100, height=50)
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
        self.Text13 = Label (otherFrame, text='全局检查：', font=('微软雅黑', '20'))
        Text14 = Label (otherFrame, text='', fg='red')
        Text1.place (y=25), Text2.place (y=45), Text3.place (y=65), Text4.place (y=85)
        Text5.place (y=105), Text6.place (x=300, y=105), Text7.place (y=125), Text8.place (x=300, y=125)
        Text9.place (y=145), Text10.place (x=300, y=145), Text11.place (y=165), Text12.place (y=185)
        self.Text13.place (x=200, y=265), Text14.place (x=500)

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
                        self.Text13['text'] = '全局检查：检查有错误发生'
                        self.Text13['fg'] = 'red'
                    elif pass_Confirm:
                        self.Text13['text'] = '全局检查：标签待确认'
                    else:
                        self.Text13['text'] = '全局检查：全部正常'
                    self.check_Frame(self.url_txt.get ())
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
        from logo import img
        from base64 import b64decode
        self.photo = tk.PhotoImage (data=b64decode(img))
        theLabel = tk.Label (self.root,
                             image=self.photo,  # 加入图片
                             compound='bottom')
        theLabel.pack ()


    # ----------------------------------------------------------------------
    def check_Cookie(self):
        lbl = Label (self.root, text="Cookie:")
        lbl.place (x=0, y=160)
        txt = scrolledtext.ScrolledText (self.root, width=82, height=5)
        txt.place (x=60, y=140)
        checkrequest = Label (self.root, text="点击添加Cookie", font=('微软雅黑', '13'))
        if os.path.exists ('cookie.txt'):
            if len (open ('cookie.txt').read ()) > 10:
                checkrequest.configure (text="已保存cookie，请测试")
                self.start_check_btn.place(x=559,y=238)
        checkrequest.place (x=60, y=240)
        click_ = Button (self.root, text="Click Me", width=20, command=lambda: self.clicked (checkrequest, txt))
        click_.place (x=60,y=270)

    # ----------------------------------------------------------------------
    def clicked(self, checkrequest, txt):
        if os.path.exists ('cookie.txt'):
            test_cookie = cookie_test (open ('cookie.txt').read ())
            if test_cookie is True:
                checkrequest.configure (text="状态正常")
                self.start_check_btn.place(x=559,y=238)
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
                self.start_check_btn.place(x=559,y=238)
                return True
            else:
                checkrequest.configure (text="状态异常,请测试cookie")
                return False


if __name__ == '__main__':
    root = tk.Tk ()
    app = MyApp (root)
    root.mainloop ()
