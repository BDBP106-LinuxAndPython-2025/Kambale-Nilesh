#(8) Read in the file diabetes.csv, and after obtaining the pandas dataframe, do the following:
import pandas as pd
df = pd.read_csv('diabetes.csv')

# (i) Print all the column names
print("columns of csv :",df.columns)

# (ii) Print the first 10 rows
print("\nTop 10 rows\n", df.head(10))

# (iii) Print the mean of the BloodPressure column values
print("The mean of the Blood pressure column :", df["BloodPressure"].mean())

# (iv) Print the first 4 rows of columns 3,4,5
print("Print the first 4 rows of columns 3,4,5:\n",df.iloc[:4,3:6])

# (v) Addanothercolumn’NormalizedBP’ using (max-min) normalization to the dataframe
# as: BP[i]-min(BP) / (max(BP)- min(BP)).

df["NormalizedBP"]=(df["BloodPressure"] - df["BloodPressure"].min())/(df["BloodPressure"].max() - df["BloodPressure"].min())
print("NormalizedBP:\n",df[["BloodPressure","NormalizedBP"]].head(6))

# (vi) Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Se
# nior” based on the age brackets (1-18, 19-50, ¿50). Create a new column in the
# dataframe with this function called age category
def categorize_age(age):
    if age<=18:
        return "Youth"
    if 19 <=age <=50:
        return "Adult"
    else:
        return "Senior"

f=pd.read_csv("diabetes.csv")
f["Age Category"]=f["Age"].apply(categorize_age)
print(f[["Age","Age Category"]])
