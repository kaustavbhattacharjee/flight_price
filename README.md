# flight_price

## Monitor flight price fluctuations like a PRO!

This repo helps you in retrieving price on a regular basis for a certain known flight. If you know the flight details, you can set a script to send you SMS about the flight price.




### Usage
1. Download all the pre-requisites, if not done already.
2. Perform a search on Yatra.com with your search parameters(city, date, class etc)
3. Copy the search URL generated and paste it in the file in the myURL
4. Right click and perform Inspect Element on the price of the flight journey you want to monitor.
5. Select the id and paste it into the id_code1 .
6. Enter your Twilio Account SID and Auth Token in the TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN respectively.
7. You can change the city and date details if you want to customise the SMS accordingly.
8. Run it and Voilà! Your flight price will be sent to your phone.
9. You can set a script (cron/task scheduler) to run it at a certain interval.

### Pre-Requisites
1. Python 3
2. Selenium (pip3 install selenium)
3. Twilio (pip3 install twilio)
4. Twilio Account with a phone number (can be added in the FREE TRIAL)
5. The mobile number where the SMS needs to be sent (If an Indian number, make sure that is is not registered with DND)
6. [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


Feel free to raise an issue if you have any queries.
