import pandas as pd
df = pd.read_csv('viva2.csv')
new_df = df.sort_values(["color"],ascending=True)
mincol = new_df["color"].value_counts(ascending=True)
print("sorted by values:")
print(mincol)
min_index = mincol.sort_index(ascending=True)
print("sorted by index")
print(min_index)
df["min_col"]=df["carat"]*df["price"]
print(df)