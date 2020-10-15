from PriceRevision import PriceRevision

pr=PriceRevision()
pr.load_master('shop_datas/master.csv')
pr.create_maker_list()
pr.query_by_maker('マルアイ')