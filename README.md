# pranbot



#### Dependencies

- Twitter API

- Google Cloud Functions

- Google Cloud Scheduler

- gspread API



### How it works

pranbot completely runs on the cloud. It uses a google sheets file as it's database to store entries that it will tweet every 6 hours. This file is accessed by the Google Cloud Functions when called by the Google Cloud Scheduler and randomly chooses a cell in row 1 that it sends a POST request to the Twitter API to send a new tweet as @impranbot. 
