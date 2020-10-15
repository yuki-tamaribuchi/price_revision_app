from PriceRevision import PriceRevision

pr=PriceRevision()
pr.read_master_csv('shop_datas/master.csv')
pr.create_revision_sheet()