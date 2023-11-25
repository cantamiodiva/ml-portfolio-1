import pandas as pd

# per ogni game_version_id
# region -> match_duration_seconds

# def print_full(x):
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.width', 2000)
#     pd.set_option('display.float_format', '{:20,.2f}'.format)
#     pd.set_option('display.max_colwidth', None)
#     print(x)
#     pd.reset_option('display.max_rows')
#     pd.reset_option('display.max_columns')
#     pd.reset_option('display.width')
#     pd.reset_option('display.float_format')
#     pd.reset_option('display.max_colwidth')

df = pd.read_parquet("dota2_matches.parquet")
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_seq_items', None)

print(df.dtypes)
# print(df.describe(include="all"))
# print(df.info())
print(df.game_version_id.nunique())
