from tkinter import *
import tkinter as tk
import os
from tkinter import scrolledtext
from test_cookie import cookie_test
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.geometry('350x300')
        self.root.resizable(0, 0)
        self.root.title("lemon审核工具")
        self.frame = tk.Frame(parent)
        self.insert_photo()
        self.check_Cookie()
        self.frame.place(x=208, y=240)
        btn = tk.Button(self.frame, text="开始审核", height=3,
                        width=19, fg='red', command=self.openFrame)
        btn.pack()


    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------


    def openFrame(self):
        """"""

        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.geometry("700x300")
        otherFrame.resizable(0, 0)
        otherFrame.title("lemon审核", )

        global txt2,url_txt
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        url_txt = tk.Entry(otherFrame, width=44)
        url_txt.place(x=35, y=0)
        Label(otherFrame, text="url:", font=('微软雅黑', '10')).place(x=0, y=0)
        check = tk.Button(otherFrame, text="check", width=12, height=5, command=lambda:btn_func())
        check.place(x=607,y=202)
        btn = tk.Button(otherFrame, text="back", command=handler)
        btn.place(x=620, y=152,width=80,height=50)
        Label(otherFrame,text='标题：').place(y=25)
        Label(otherFrame,text='副标题：').place(y=45)
        Label(otherFrame, text='类型：').place(y=65)
        Label(otherFrame, text='详细信息：').place(y=85)
        Label(otherFrame, text='媒介检查：').place(y=105)
        Label(otherFrame, text='编码检查：').place(y=125)
        Label(otherFrame, text='音频检查：').place(y=145)
        Label(otherFrame, text='地区检查：').place(y=165)
        Label(otherFrame, text='制作组检查：').place(y=185)
        Label(otherFrame, text='标签检查：').place(y=205)
        Label(otherFrame, text='链接检查：').place(y=225)
        Label(otherFrame, text='全局检查：',font=('微软雅黑', '20')).place(x=100,y=255)
    # ----------------------------------------------------------------------

        def btn_func():
            """按键的触发事件"""
            from start_check import start_process
            url_search = re.search('lemonhd.org', url_txt.get())
            if url_search:
                from start_check import start_process
                input_data=start_process(url_txt.get())
                Label(otherFrame, text='标题：'+input_data[0]).place(y=25)
                Label(otherFrame, text='副标题：'+input_data[1]).place(y=45)
                Label(otherFrame, text='类型：'+input_data[2]).place(y=65)
                Label(otherFrame, text='详细信息：'+str(input_data[3])).place(y=85)
                Label(otherFrame, text='媒介检查：'+input_data[4]).place(y=105)
                Label(otherFrame, text='编码检查：'+input_data[5]).place(y=125)
                Label(otherFrame, text='音频检查：'+input_data[6]).place(y=145)
                Label(otherFrame, text='分辨率检查：'+input_data[7]).place(y=165)
                Label(otherFrame, text='地区检查：'+input_data[8]).place(y=165)
                Label(otherFrame, text='制作组检查：'+input_data[9]).place(y=185)
                Label(otherFrame, text='标签检查：'+input_data[10]).place(y=205)
                Label(otherFrame, text='链接检查：'+input_data[11]).place(y=225)
                pass_false = re.search('错误', str(input_data))
                if pass_false:
                    Label(otherFrame, text='全局检查：检查有错误发生',font=('微软雅黑', '20'),fg='red').place(x=100,y=255)
                else:
                    Label(otherFrame, text='全局检查：全部正常', font=('微软雅黑', '20')).place(x=100, y=255)
            else:
                Label(otherFrame, text='请输入正确的url',fg='red').place(x=370)

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()



    # ----------------------------------------------------------------------
    def insert_photo(self):
        from logo import img_data
        from base64 import b64decode
        def get_pic(pic_code, pic_name):
            image = open(pic_name, 'wb')
            image.write(b64decode(pic_code))
            image.close()
        get_pic(img_data, 'logo.png')
        global photo
        photo = tk.PhotoImage(file='logo.png')
        theLabel = tk.Label(self.root,
                            image=photo,  # 加入图片
                            compound='bottom')
        theLabel.pack()
        os.remove('logo.png')

    # ----------------------------------------------------------------------
    def check_Cookie(self):
        lbl = Label(self.root, text="Cookie:")
        lbl.place(x=0, y=160)
        txt = scrolledtext.ScrolledText(self.root, width=40, height=9)
        txt.place(x=50, y=110)

        if os.path.exists('cookie.txt'):
            checkrequest = Label(self.root, text="已保存cookie，请测试")
        else:
            checkrequest = Label(self.root, text="点击添加Cookie", font=('微软雅黑', '13'))
        checkrequest.place(x=0, y=240)

        def clicked():
            if os.path.exists('cookie.txt'):
                if cookie_test(open('cookie.txt').read()) is True:
                    checkrequest.configure(text="状态正常")
                    return True
                else:
                    checkrequest.configure(text="状态异常,请测试cookie")
                    return False
            else:
                if cookie_test(txt.get(1.0, 'end').strip('\n')) is True:
                    checkrequest.configure(text="状态正常")
                    return True
                else:
                    checkrequest.configure(text="状态异常,请测试cookie")
                    return False

        click_=Button(self.root, text="Click Me", width=20, command=lambda :clicked())
        click_.place(y=270)
    # ----------------------------------------------------------------------


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

