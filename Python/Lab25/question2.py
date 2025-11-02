# (2) Read the file ODI-Batting Cricket Analytics.json in pandas using
# pandas.read_json(<filename>) syntax. Then do the following:
# (a) Display the column names
import pandas as pd
df=pd.read_json("ODI-Batting_Cricket_Analytics.json")
print(f' Columns in the file : {df.columns.tolist()}')

# (b) Sort the dataframe by their ScoreRate and print the top 5 players with the highest ScoreRate
top=df.sort_values(by="ScoreRate",ascending=False).head(5)
print("Top 5 players:")
print(top[["Player","ScoreRate"]])

# (c) Print all the players who have got the min runs
min = df["Runs"].min()
print(f"The players who got minimum  : {min}")
print(" Players with minimum runs :")
min_players = df[df["Runs"] == min]
print(min_players)

# (d) How many players have got the min runs?
all_min=df[df["Runs"]==min]
number_all_min_players=len(all_min)
print(f"Players with minimum runs: {number_all_min_players}")



# (e) Print all the players from India who have runs above average
average=df["Runs"].mean()
print("The average of all the runs:",average)
names_ind_abvavg=df[(df["Country"]=="India") & (df["Runs"]>average)]
print(names_ind_abvavg[["Player","Runs"]])
number_ind_abvavg=len(names_ind_abvavg)
print("The number of Indian players who have scored above average are:",number_ind_abvavg)