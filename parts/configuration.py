from tkinter import *
from tkinter import ttk
import os


# file存在確認
def is_exist(path, frame, r, name):
    path = str(path.get())
    rpath = str(repr(path)[1:-1])#raw文字列化
    if os.path.exists(rpath):
        ok = ttk.Label(frame, width=50, text="{} ok !".format(name))
        ok.grid(row=r)
    else:
        no = ttk.Label(frame, width=50, \
                        text="no {}... please check the path".format(name))
        no.grid(row=r)
    print(path)


def configuration():
    root = Tk()
    root.title("hello !")

    # メインフレーム(この中に諸々入れる)
    mainframe = ttk.Frame(root, padding=10)
    mainframe.grid()

    # 画像path入力
    label = ttk.Label(mainframe, text="image path :")
    label.grid(row=0)

    img_path = StringVar()
    entry_img_path = ttk.Entry(mainframe, width=50, textvariable=img_path)
    entry_img_path.grid(row=1)

    button_img_path = ttk.Button(mainframe, text="enter", \
                                command=lambda:is_exist(img_path, mainframe, 3, "image"))
    button_img_path.grid(row=2)

    # 終了
    button_fin = ttk.Button(mainframe, text="all ok", \
                                command=lambda:root.destroy())
    button_fin.grid(row=5)


    root.mainloop()

    img_path = str(img_path.get())
    r_img_path = str(repr(img_path)[1:-1])#raw文字列化

    return r_img_path