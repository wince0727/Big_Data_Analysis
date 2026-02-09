import dask.dataframe as dd

df = dd.read_csv("data.csv")

print("Total Rows:", df.shape[0].compute())
print(df.head())

