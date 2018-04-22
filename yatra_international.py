from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
import sys
import os
import time

# The data Entry and Populate Section

origin_city="BOM"
destination_city="DXB"

origin_flight_code="G9402"
return_flight_code="G9401"

departure_date="05/05/2018"
return_date="08/05/2018"

id_code1="fare--BOMSHJG940220180505SHJBOMG940120180508_G9API" #Replace with the <p> id 
my_URL="https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=BOM&originCountry=IN&destination=DXB&destinationCountry=AE&flight_depart_date=05/05/2018&arrivalDate=08/05/2018&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1" #Replace with the search URL

TWILIO_ACCOUNT_SID = "<enter twilio account sid here"
TWILIO_AUTH_TOKEN  = "enter twilio auth token here"

from_number  = '' #set up a number at Twilio and enter it here
to_number = ''#Number to which it has to be sent (Should not be in DND registry, if you are sending to Indian numbers)


# End of Data Entry And Populate Section

      
#Start of Definitions Section


def find_by_xpath2(locator):
            wait = WebDriverWait(driver, 10)
            #element =wait.until(EC.presence_of_element_located((By.XPATH, locator)))
            element=driver.find_element_by_css_selector(locator)            
            return element
'''
def get_exact_price(price_data):
            price=0
            for item in price_data.split("\n"):
                  if "Rs" in item:
                        price= int(item.strip().strip("Rs.").replace(",",""))
                        break

            return price
 
'''

class FormPage(object):
           
            
            def retrieve_price(self,city1,city2,flight_code1,flight_code2,my_date1,my_date2):
                  #finding the date and month and year
                  the_date1=my_date1[:2]
                  the_month1=my_date1[3:5]
                  the_year1=my_date1[6:10]

                  the_date2=my_date2[:2]
                  the_month2=my_date2[3:5]
                  the_year2=my_date2[6:10]
                  
                  
                  #id_code="fare--"+city1+city2+flight_code1+the_year1+the_month1+the_date1+city2+city1+flight_code2+the_year2+the_month2+the_date2+"_AASAPIINT"
    
                  price=find_by_xpath2("p#"+id_code1).text
                  return price
                   

                                    

class myWait(object):
            def __init__(self, driver):
                  self.driver = driver

            def __enter__(self):
                  pass

            def __exit__(self, *_):
                  element = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.TAG_NAME, "html"))
                  )

#End of Definition Section


#Start of Action Section
                  
#Chrome driver to open Browser
#Download from https://sites.google.com/a/chromium.org/chromedriver/downloads
#Add correct path for ChromeDriver here
driver = webdriver.Chrome('/Users/kaustav/Downloads/chromedriver')
    
#URL of the website to Scrap
#my_URL="https://flight.yatra.com/air-search-ui/int2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=BOM&originCountry=IN&destination=DXB&destinationCountry=AE&flight_depart_date=05/05/2018&arrivalDate=08/05/2018&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&version=1.1"
driver.get(my_URL)


time.sleep(13) #Time to load the page

price_data = FormPage().retrieve_price(origin_city,destination_city,origin_flight_code,return_flight_code,departure_date,return_date)

print(price_data)

#Send SMS

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
msg = "Flight from "+origin_city+" to "+destination_city+" on "+departure_date+" and return date "+return_date+" costs "+str(price_data)
message=client.messages.create(
          to=to_number,
          from_=from_number,
          body=msg
      )

print("Message sent at " + time.strftime("%a, %d %b %Y %H:%M:%S") + " with SID " + message.sid)
   
driver.quit() # closes the webbrowser
    
