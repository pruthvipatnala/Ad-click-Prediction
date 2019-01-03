import pandas as pd

df = pd.read_csv('train_balanced.csv')

print(df.head())

x = []

df.columns = ["ID","datetime","siteid","offerid","category","merchant","countrycode","browserid","devid","click","day","time"]

for i in range(len(df['click'])):
    x.append((df.iloc[i]['click'],df.iloc[i]['day'],df.iloc[i]['time']))

k = list(df['click'])
sup0 = k.count(0)/len(k)
sup1 = k.count(1)/len(k)

day_anal0_wd = [i for i in x if i[0]==0 and i[1]=='weekday']
day_anal0_we = [i for i in x if i[0]==0 and i[1]=='weekend']

day_anal1_wd = [i for i in x if i[0]==1 and i[1]=='weekday']
day_anal1_we = [i for i in x if i[0]==1 and i[1]=='weekend']

# support(weekday) , conf(weekday,click=0),conf(weekday,click=1)
sup_weekday = (len(day_anal0_wd)+len(day_anal1_wd))/len(df['click'])
conf_weekday_0 = len(day_anal0_wd)/(len(day_anal0_wd)+len(day_anal1_wd))
conf_weekday_1 = len(day_anal1_wd)/(len(day_anal0_wd)+len(day_anal1_wd))
weekday = [sup_weekday,conf_weekday_0,conf_weekday_1,conf_weekday_0/sup0,conf_weekday_1/sup1]

# support(weekend) , conf(weekend,click=0),conf(weekend,click=1)
sup_weekend = (len(day_anal0_we)+len(day_anal1_we))/len(df['click'])
conf_weekend_0 = len(day_anal0_we)/(len(day_anal0_we)+len(day_anal1_we))
conf_weekend_1 = len(day_anal1_we)/(len(day_anal0_we)+len(day_anal1_we))
weekend = [sup_weekend,conf_weekend_0,conf_weekend_1,conf_weekend_0/sup0,conf_weekend_1/sup1]

print("\n\n\n\n")
print(weekday)
print(weekend)

q1 = [i for i in x if i[-1]<361]
q2 = [i for i in x if i[-1]<721]
q3 = [i for i in x if i[-1]<1081]
q4 = [i for i in x if i[-1]<1440]


quarters = [q1,q2,q3,q4]
print("\n\nQuarter , conf(q,click=0) , conf(q,click=1)")
for i in range(len(quarters)):
    a0 = [j for j in quarters[i] if j[0]==0]
    a1 = [j for j in quarters[i] if j[0]==1]
    print(i+1,"\t",len(a0)/(len(a0)+len(a1)),"\t",len(a1)/(len(a0)+len(a1)))
    












