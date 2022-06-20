import pandas as pd
from hackathon.models import Companies


dict_from_csv = pd.read_csv(
    'ASX 300 Data.csv', header=None, index_col=0, squeeze=True).to_dict()
# print(dict_from_csv)

for code, name in dict_from_csv.items():
    entry = Companies(stock_code = code, name = name)
    entry.save()
