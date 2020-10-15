import PySimpleGUI as sg
from PriceRevision import PriceRevision

pr=PriceRevision()
makers=[]

sg.theme('DarkBrown4')
layout=[
    [sg.Text('価格改定抽出アプリ')],
    [sg.In(),sg.FileBrowse('マスタのCSVを選択'),sg.Submit('読込')],
    [sg.DropDown(makers,default_value='メーカーを選択',key='-MAKERS-',size=(40,10))],
    [sg.Text('作業先フォルダを選択してください．'),sg.FolderBrowse(key='-WORK_DIR-')],
    [sg.Button('作業用エクセルファイルを作成')],
    [sg.Button('実行')]
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

    if event=='作業用エクセルファイルを作成':
        dir=values['-WORK_DIR-']
        pr.create_revision_excel(dir=dir)

    if event=='実行':
        selected_maker=values['-MAKERS-']
        pr.query_by_maker(maker=selected_maker)
        pr.create_revision_data_frame(dir=dir)
        pr.execute_search()
        pr.export_matched_data(dir=dir)
        

window.close()