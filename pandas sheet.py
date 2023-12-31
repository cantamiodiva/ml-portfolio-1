import pandas as pd

df = pd.read_parquet("dota_matches.parquet")
print(df.head())
print(df.info())

# select column
df.column1
df[["column1","column2"]]

# select row
df.iloc[2]

# filter rows
df[df.age > 30]
df[(df.month == "March") | (df.age == 23)]
df[df.month.isin(['January','February','March'])]
df.reset_index(inplace=True, drop=True)

# add column
df['Sold in Bulk?'] = ['Yes','Yes','No','No']
df['Is taxed?'] = 'Yes'
df['Margin'] = df.Price-df.Cost_to_Manufacture
df['Lowercase Name'] = df.Name.apply(str.lower)
get_last_name = lambda fullname: fullname.split()[-1]
df['last_name'] = df.name.apply(get_last_name)
total_earned = lambda row: row['hourly_wage']*row['hours_worked'] if row['hours_worked'] < 40 else 40*row['hourly_wage'] + (row['hours_worked']-40)*1.5*row['hourly_wage']
df['total_earned'] = df.apply(total_earned, axis=1)

# renaming columns
df.columns = ['ID','Title','Category','Year Released','Rating']
df.rename(columns={
  'name': 'movie_title'
},inplace=True)

# aggregates
pd.age.median()
pd.state.nunique()
pd.color.unique()
# mean, std, median, max, min, count, nunique, unique
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda row: np.percentile(row,25)).reset_index()
shoe_counts = orders.groupby(['shoe_type','shoe_color']).id.count().reset_index()
shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color',index='shoe_type',values='id').reset_index()

# dataframe merge
# inner merge (merge on columns with same name, only keep values that are matching between tables)
sales_vs_targets= pd.merge(sales,targets)
all_data = sales.merge(targets).merge(men_women)
orders_products = orders.merge(products.rename(columns={'id':'product_id'}))
orders_products = pd.merge(orders,products,left_on='product_id',right_on='id', suffixes=['_orders','_products'])
#outer merge (merge on columns with same name, keep every value and fill with NaN or none for missing values)
store_a_b_outer = pd.merge(store_a,store_b,how="outer")
# left/right merge (merge on columns with same name, keep every value from left/right table and add values from right/left table or none/NaN)
store_a_b_left = pd.merge(store_a,store_b,how="left")

#concatenate frame
menu = pd.concat([bakery,ice_cream])