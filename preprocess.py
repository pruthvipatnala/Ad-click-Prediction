
import pandas as pd
import numpy as np
import random

train_df = pd.read_csv("train_set.csv")

print(train_df.head())

k = list(train_df['devid'])
devices = [i for i in list(set(k)) if type(i)==type('str')]
devices = [(i,k.count(i)) for i in devices]
#number of missing values=1274 in devid

x = []
for i in range(len(k)):
    if(type(train_df.iloc[i]['devid'])==type('str') ):
        x.append((train_df.iloc[i]['devid'],train_df.iloc[i]['click']))
    

#devices --> key = device name , value = [count,support(devid),conf(devid,click=0)]

devid = dict()
for i in devices:
    devid[i[0]] = []
    devid[i[0]].append(i[1])
    devid[i[0]].append(i[1]/len(k))
    conf_dev_cl0 = [j for j in x if(j[0]==i[0] and j[1]==0)]
    
    #if(i[0]=='Desktop'):
    #    print(conf_dev_cl0)
    #print(i[0],len(conf_dev_cl0))
    devid[i[0]].append(len(conf_dev_cl0)/i[1])

#from confidence we understand that desktop has least confidence for click=0
#from support ---- mobile is the most used device

#Browser stats

m = list(train_df['browserid'])
browser = [i for i in list(set(m)) if type(i)==type('str')]



gc = ['Google Chrome','Chrome']
op = ['Opera']
mf = ['Firefox','Mozilla Firefox','Mozilla']
ie = ['InternetExplorer','Internet Explorer','IE']
ed = ['Edge']
sa = ['Safari']

m1 = []

for i in m:
    if(i in gc):
        m1.append('Google Chrome')
    elif(i in op):
        m1.append('Opera')
    elif(i in mf):
        m1.append('Mozilla Firefox')
    elif(i in ie):
        m1.append('Internet Explorer')
    elif(i in ed):
        m1.append('Edge')
    elif(i in sa):
        m1.append('Safari')
    else:
        m1.append(i)

train_df['browserid'] = m1
k = list(train_df['browserid'])
browser = [i for i in list(set(k)) if type(i)==type('str')]


x = []
for i in range(len(k)):
    if(type(train_df.iloc[i]['devid'])==type('str') and type(train_df.iloc[i]['browserid'])==type('str')):
        x.append((train_df.iloc[i]['devid'],train_df.iloc[i]['browserid'],train_df.iloc[i]['click']))
        

#browser_dict --> key = browserid , value = [count,support(browserid),lift(device,browser)*3,conf()]    

browser_dict = dict()

for i in browser:
    browser_dict[i] = []
    browser_dict[i].append(k.count(i))
    browser_dict[i].append(k.count(i)/len(k))
    for j in devices:
        c = [a for a in x if(a[0]==j[0] and a[1]==i)]
        browser_dict[i].append([j[0],(len(c)/devid[j[0]][0])])
        #/(k.count(i)/len(k)
'''
Conclusions - 
Popularity of browsers - Mozilla Firefox,Edge,Internet Explorer,Google Chrome,Safari,Opera

As per confidence ---
Device used    most used browser
Tablet       -     Edge
Mobile       -     Mozilla
Desktop      -     Mozilla
'''

#site ---
k = list(train_df['siteid'])
l = list(train_df['siteid'].dropna())
print(len(k),len(l))
#missing values in site


#offerid ---
k = list(train_df['offerid'])
l = list(train_df['offerid'].dropna())
print(len(k),len(l))
# no missing values in offerid


#category
k = list(train_df['category'])
l = list(train_df['category'].dropna())
print(len(k),len(l))
#no missing values category

#merchant
k = list(train_df['merchant'])
l = list(train_df['merchant'].dropna())
print(len(k),len(l))
#no missing values for merchant


#country code
k = list(train_df['countrycode'])
l = list(train_df['countrycode'].dropna())
print(len(k),len(l))
#no missing values for country code


dev_names = [i[0] for i in devices]
browser_names = browser

br_dev_combs = []
for i in dev_names:
    for j in browser_names:
        br_dev_combs.append((i,j))


k = list(train_df['browserid'])
browser = [i for i in list(set(k)) if type(i)==type('str')]


x = []
for i in range(len(k)):
    if(type(train_df.iloc[i]['devid'])==type('str') and type(train_df.iloc[i]['browserid'])==type('str')):
        x.append((train_df.iloc[i]['devid'],train_df.iloc[i]['browserid'],train_df.iloc[i]['click']))
        

y = []
for i in range(len(train_df['siteid'])):
    y.append((train_df.iloc[i]['devid'],train_df.iloc[i]['browserid']))

#confidence for click=0
for i in br_dev_combs:
    l = [j for j in x if(j[0]==i[0] and j[1]==i[1] and j[2]==0)]
    m = [j for j in y if(j[0]==i[0] and j[1]==i[1])]
    try:
        print(i[0],i[1],len(l)/len(m))
    except:
        print(i[0],i[1],0)

#for calculating the support of click=1
v = len([i for i in list(train_df['click']) if i==1])

print("****")

#lift for click=1
for i in br_dev_combs:
    l = [j for j in x if(j[0]==i[0] and j[1]==i[1] and j[2]==1)]
    m = [j for j in y if(j[0]==i[0] and j[1]==i[1])]
    try:
        print(i[0],i[1],len(l)/(len(m)*(v/len(y))))
    except:
        print(i[0],i[1],0)



'''
dealing with missing values
'''


site_click = []
for i in range(len(train_df['siteid'])):
    if(not(np.isnan(train_df.iloc[i]['siteid']))):
        site_click.append((train_df.iloc[i]['siteid'],train_df.iloc[i]['click']))

pos_site_ids0 = [i[0] for i in site_click if(i[1]==0)]
pos_site_ids0 = list(set(pos_site_ids0))
pos_site_ids1 = [i[0] for i in site_click if(i[1]==1)]
pos_site_ids1 = list(set(pos_site_ids1))

site_ids = []
browser_ids = []
device_ids =[]

for i in range(len(train_df['siteid'])):
    row = [train_df.iloc[i]['siteid'],train_df.iloc[i]['browserid'],train_df.iloc[i]['devid']]
    if(np.isnan(row[0])==True):
        '''
        if(train_df.iloc[i]['click']==0):
            site_ids.append(random.choice(pos_site_ids0))
        else:
            site_ids.append(random.choice(pos_site_ids1))
        '''
        site_ids.append(-1)
    else:
        site_ids.append(row[0])
    
    #browser is missing
    if(type(row[1])!=type('str') and type(row[2])==type('str')):
        if(row[2]=='Mobile' or row[2]=='Desktop'):
            browser_ids.append('Mozilla Firefox')
            device_ids.append(row[2])
        elif(row[2]=='Tablet'):
            browser_ids.append('Edge')
            device_ids.append(row[2])
    
    #device is missing
    elif(type(row[1])==type('str') and type(row[2])!=type('str')):
        if(row[1]=='Mozilla Firefox'):
            browser_ids.append(row[1])
            device_ids.append(random.choice(['Mobile','Desktop']))
        elif(row[1]=='Edge'):
            browser_ids.append(row[1])
            device_ids.append('Tablet')
        elif(row[1]=='Internet Explorer'):
            browser_ids.append(row[1])
            device_ids.append("Desktop")
        elif(row[1]=='Google Chrome' or row[1]=='Opera' or row[1]=='Safari'):
            browser_ids.append(row[1])
            device_ids.append("Mobile")
    
    elif(type(row[1])!=type('str') and type(row[2])!=type('str')):
        if(train_df.iloc[i]['click']==0):
            a = random.choice([('Opera','Mobile'),('Mozilla Firefox','Mobile'),('Internet Explorer','Mobile'),('Google Chrome','Desktop'),('Mozilla Firefox','Desktop'),('Edge','Tablet'),('Internet Explorer','Tablet')])
            browser_ids.append(a[0])
            device_ids.append(a[1])
        elif(train_df.iloc[i]['click']==1):
            a = random.choice([('Google Chrome','Mobile'),('Internet Explorer','Desktop'),('Google Chrome','Desktop'),('Safari','Tablet'),('Internet Explorer','Tablet')])
            browser_ids.append(a[0])
            device_ids.append(a[1])
            
    else:
        browser_ids.append(row[1])
        device_ids.append(row[2])
            

site_ids = [np.int32(i) for i in site_ids]

ids = list(train_df['ID'])
datetime_ = list(train_df['datetime'])
offerid = list(train_df['offerid'])
category = list(train_df['category'])
merchant = list(train_df['merchant'])
countrycode = list(train_df['countrycode'])
click = list(train_df['click'])



df_new = pd.DataFrame(list(zip(ids,datetime_,site_ids,offerid,category,merchant,countrycode,browser_ids,device_ids,click)),\
    columns=["ID","datetime","siteid","offerid","category","merchant","countrycode","browserid","devid","click"])



#Dealing with imbalance in classes
df_new0 = df_new[df_new['click']==0]

df_new1 = df_new[df_new['click']==1]

#print(df_new0.head())

#print(df_new1.tail())

#df_new0 = df_new0.iloc[:400][:]

df_new0 = df_new0.sample(frac=0.2)

df_balance = pd.concat([df_new0, df_new1])

df_balance = df_balance.sample(frac=1)



#df_new.to_csv("train_update.csv", sep=',', encoding='utf-8')

'''
df = pd.read_csv("train_set.csv")

df_new0 = df[df['click']==0]
df_new1 = df[df['click']==1]

df_new0 = df_new0.iloc[:400][:]

df_balance = pd.concat([df_new0, df_new1])

df_balance = df_balance.sample(frac=1)

df_balance.to_csv("train_balanced1.csv", sep=',', encoding='utf-8')
'''

import datetime
def get_date_time(s):
    l = s.split(' ')
    l[0] = [int(i) for i in l[0].split('/')]
    l[0][-1] = 2000+l[0][-1]
    l[0].reverse()
    d = datetime.datetime(l[0][0],l[0][1],l[0][2]).weekday()
    l[1] = [int(i) for i in l[1].split(':')]
    minutes = l[1][0]*60+l[1][1]
    
    ans =[]
    if(d==5 or d==6):
        ans.append("weekend")
    else:
        ans.append("weekday")
    ans.append(minutes)
    return tuple(ans)

date_stat = []

for i in range(len(df_balance['datetime'])):
    date_stat.append(get_date_time(df_balance.iloc[i]['datetime']))
    
days = [i[0] for i in date_stat]
times = [i[1] for i in date_stat]


df_balance['day'] = days
df_balance['time'] = times

df_balance.to_csv("train_balanced.csv", sep=',', encoding='utf-8')

#Test set***************************************************************

df_test = pd.read_csv('test_set.csv')

date_stat = []

df_test.columns = ["ID","datetime","siteid","offerid","category","merchant","countrycode","browserid","devid","click"]

for i in range(len(df_test['datetime'])):
    date_stat.append(get_date_time(df_test.iloc[i]['datetime']))
    
days = [i[0] for i in date_stat]
times = [i[1] for i in date_stat]


df_test['day'] = days
df_test['time'] = times

df_balance.to_csv("test_update.csv", sep=',', encoding='utf-8')





















