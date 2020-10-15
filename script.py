from PriceRevision import PriceRevision

pr=PriceRevision()
pr.read_master_csv('shop_datas/master.csv')
pr.read_revision_sheet()
pr.execute_search()