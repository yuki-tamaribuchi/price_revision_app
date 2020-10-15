import PySimpleGUI as sg
from PriceRevision import PriceRevision

pr=PriceRevision()
makers=[]

sg.theme('DarkAmber')
layout=[
    [sg.Text('価格改定抽出アプリ')],
    [sg.In(),sg.FileBrowse('マスタのCSVを選択'),sg.Submit('読込')],
    [sg.DropDown(makers)],
    [sg.Text('作業先フォルダを選択してください．'),sg.FolderBrowse()],
    [sg.Button('作業用エクセルファイルを作成')],
]

window = sg.Window('価格改定抽出アプリ',layout)

while True:
    event,values=window.read()

    if event == sg.WIN_CLOSED:
        break
    if event=='読込':
        filepath=values[0]
        pr.load_master(filepath)
        pr.create_maker_list()
        makers=pr.makers

    if event=='作業用エクセルファイルを作成':
        pr.create_revision_excel()
window.close()