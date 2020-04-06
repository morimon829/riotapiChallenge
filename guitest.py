#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yoshi
#
# Created:     31/03/2020
# Copyright:   (c) yoshi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from riotwatcher import RiotWatcher

def button_click():
    watcher  = LolWatcher('RGAPI-b3bcf5be-23b0-4356-8a9a-d48279559780')
    region = "jp1" #サーバーの選択　日本鯖はjp1
    name = "morimon829" #サモナーネームの入力
    summoner = watcher.summoner.by_name(region,name) #プレイヤーデータの取得
    print(summoner)

    root = Tk()
    root.title('Entry Test')
    root.resizable(False, False)
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    label1 = ttk.Label(frame1, text='APIキー', padding=(5,2))
    label1.grid(row=0,column=0,sticky=E)

if __name__ == '__main__':

    """
    # ================================================
    watcher  = RiotWatcher('RGAPI-b3bcf5be-23b0-4356-8a9a-d48279559780')

    region = "jp1" #サーバーの選択　日本鯖はjp1
    name = "morimon829" #サモナーネームの入力
    summoner = watcher.summoner.by_name(region,name) #プレイヤーデータの取得
    print(summoner)
    # ================================================
    """

    root = Tk()
    root.title('Entry Test')
    root.resizable(False, False)
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    label1 = ttk.Label(frame1, text='APIキー', padding=(5,2))
    label1.grid(row=0,column=0,sticky=E)

    label2 = ttk.Label(frame1, text='サモナーネーム', padding=(5,2))
    label2.grid(row=1,column=0,sticky=E)

    # Username Entry
    username = StringVar()
    username_entry = ttk.Entry(
        frame1,
        textvariable=username,
        width=30 )
    username_entry.grid(row=0,column=1)

    # Email Entry
    email = StringVar()
    email_entry = ttk.Entry(
        frame1,
        textvariable=email,
        width=30 )
    email_entry.grid(row=1,column=1)

    frame2 = ttk.Frame(frame1, padding=(0,5))
    frame2.grid(row=3,column=1,sticky=W)

    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=3, column=1, padx=5, sticky=(E))

    button2 = ttk.Button(frame2, text='Cancel',command=quit)
    button2.pack(side=LEFT)


    root.mainloop()


