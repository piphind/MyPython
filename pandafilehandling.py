import pandas
import pandas as pd

pd.set_option("display.max_columns", 10)
pd.set_option("display.width", 320)

df1 = pandas.read_csv("Test Files/datafile1.csv")

print("----------------  df1  -------------------------------")
print(df1)

df2 = pandas.read_json("Test Files/datafile1.json")

print("-----------------  df2  ------------------------------")
print(df2)
df2subset = df2
df2subset = df2.set_index("Address")
print("-----------------  df2subset(1)  ------------------------------")
print(df2subset)
print("-----------------  df2subset(2)  ------------------------------")
df2subset = df2subset.loc["735 Dolores St":"332 Hill St", "Country":"Name"]
print(df2subset)
df2subset2 = df2.iloc[3, 2:4]
print("-----------------  df2subset2  ------------------------------")
print(df2subset2)

df3 = pandas.read_excel("Test Files/datafile1.xlsx", sheet_name=0)
print("--------------------  df3 (1)  ---------------------------")
print(df3)

# Adding Columns
# df3["Continent"] = ["North America", "North America", "North America", "North America", "North America", "North America"]
df3["Continent"] = df3.shape[0]*["North America"]
print("--------------------  df3 (2)  ---------------------------")
print(df3)
# Updating Columns
df3["Continent"] = df3.shape[0]*["North USA"]
print("--------------------  df3 (3)  ---------------------------")
print(df3)
# Adding Rows - Transpose the rows to columns and use the syntax above..,
df3v2 = df3.T
df3v2[6] = [7, "New Address", "New City", "New State", "New Country", "New Name", 0, "North America"]
df3 = df3v2.T
print("--------------------  df3 (4)  ---------------------------")
print(df3)


df4 = pandas.read_csv("Test Files/datafile1_semi-colons.txt", sep=";")
print("----------------------  df4  ------------------------")
print(df4)

df5 = pandas.read_csv("Test Files/datafile1-NH.txt", header=None)
df5.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employess"]
print("---------------------  df5  --------------------------")
print(df5)

df6 = df5.set_index("ID")
print("-----------------  df6  -----------------------------")
print(df6)

# Dropping Rows and Columns
# Drop Column - use argument '1'
df6subset1 = df5.drop("Name", 1)
print("-----------------  df6subset1  -----------------------------")
print(df6subset1)
# Drop Row - use argument '0'
df6subset2 = df5
df6subset2 = df5.set_index("Address")
print(df6subset2)
print(df6subset2.index)
df6subset2 = df6subset2.drop(" 1056 Sanchez St", 0)
print("-----------------  df6subset2  -----------------------------")
print(df6subset2)


