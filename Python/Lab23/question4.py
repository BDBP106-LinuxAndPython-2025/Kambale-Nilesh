import re
pattern="^[a-z0-9\.\-\%\_]+@[a-z0-9\.\_]+\.[a-z]{2,}$"
csv="2025,india,ni12l@k2amba.ac.in,Male,23yrs"
gmail=False
words=csv.split(',')
print(words)
for i in range(len(words)):
    if i==2:
        print(words[i])
        gmail=bool(re.fullmatch(pattern,words[i]))
        print(gmail)
        if gmail==True:
            print("Third field has gmail id")
        else:
            print("Third field doesnt have mail id")
