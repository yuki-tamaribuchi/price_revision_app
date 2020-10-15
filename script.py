from PriceRevision import PriceRevision

pr=PriceRevision()
pr.load_master('shop_datas/master.csv')
#pr.create_revision_csv()
pr.create_maker_list()
pr.query_by_maker('菅公工業')
pr.create_revision_data_frame('revision.xlsx')
pr.execute_search()