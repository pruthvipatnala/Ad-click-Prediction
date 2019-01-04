# Ad-Click Prediction

### Problem Statement

Given certain attributes of an advertisement been put up, predict if a user clicks on the advertisement .

### Dataset

train_set.csv and test_set.csv -
Attributes :
1) ID - Unique ID for each ad .
2) datetime - Date and time when the status was checked.
3) siteid - ID of the website hosting the ads.
4) offerid - ID of the offer by the ad.
5) category - ID for the category of the advertisement.
6) merchant - ID of the merchant putting up the ad.
7) countrycode - Code to represent the country where the status was checked.
8) browserid - Type of browser used by the end user.
9) devid - Device used by the end user.
10) click - 0 implies ad was not clicked and 1 implies that the ad was clicked.

train_balanced.csv , test_update.csv and train_update.csv -
Additional columns -
1) day - weekday or weekend.
2) time - time of the day in minutes.

### Preprocessing and Feature Extraction

Columns with missing values - siteid, browserid, devid.
Dealing with missing values - refer to preprocess.py 

browserid - Repetitions were dealt with (refer to preprocess.py)
Ex - Google Chrome , Chrome , GC were replaced by Google Chrome

Association rules have been used to replace missing values for browserid,devid.
siteid being anonymous was replaced by -1

Feature Extraction - 
datetime attribute was used to to generate two new attributes namely day and time.

Association rules using day of the week and time of the day dealt in day_time_analyze.py

### Model

Logistic regression model was used to predict the click of an ad using combinations of attributes .

>Note - Extracted features improved accuracy of the model when included .

Feature Engineering - 
Combinations of numeric columns along with categorical and cross columns were tested and the results for each are in models_tried file .

### References 
- https://www.tensorflow.org/tutorials/estimators/linear

