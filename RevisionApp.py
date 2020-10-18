import PySimpleGUI as sg
from PriceRevision import PriceRevision
import time

pr=PriceRevision()
makers=[]

sg.theme('DarkBrown4')
layout=[
    [sg.Text('価格改定抽出アプリ')],
    [sg.In(),sg.FileBrowse('マスタのCSVを選択'),sg.Submit('読込')],
    [sg.DropDown(makers,default_value='メーカーを選択',key='-MAKERS-',size=(40,10))],
    [sg.Text('作業先フォルダを選択してください．'),sg.FolderBrowse(key='-WORK_DIR-')],
    [sg.Button('作業用エクセルファイルを作成')],
    [sg.Button('実行',key='-EXECUTE-')],
]

window = sg.Window('価格改定抽出アプリ',layout,size=(600,400))

while True:
    event,values=window.read()

    if event == sg.WIN_CLOSED:
        break
    if event=='読込':
        filepath=values[0]
        pr.load_master(filepath)
        pr.create_maker_list()
        window['-MAKERS-'].update(values=pr.makers)
        print('読込完了')

    if event=='作業用エクセルファイルを作成':
        dir_path=values['-WORK_DIR-']
        pr.create_revision_excel(dir_path=dir_path)
        print('作成完了')

    if event=='-EXECUTE-':
        selected_maker=values['-MAKERS-']
        pr.query_by_maker(maker=selected_maker)
        pr.create_revision_data_frame(dir_path=dir_path)
        pr.execute_search()
        pr.export_matched_data(dir_path=dir_path)
        print('抽出完了')
        print('終了します')
        time.sleep(2)
        exit()

window.close()