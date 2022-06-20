import pandas as pd
dict_from_csv = pd.read_csv(
    'ASX 300 Data.csv', header=None, index_col=0, squeeze=True).to_dict()
print(dict_from_csv)

for item in dict_from_csv:
    print("INSERT INTO *tablename (stock_code, company_name) VALUES ({},{});".format(item, dict_from_csv[item]))


