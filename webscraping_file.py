from selenium import webdriver
import time
import os
from datetime import datetime,timedelta

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://username:mdp@neo.inetpsa.com/qualite/init-vehicles-search.do')


start = datetime.now() - timedelta(minutes=16)
start = start.strftime('%d/%m/%Y %H:%M')
end = datetime.now() + timedelta(hours=2)
end = end.strftime('%d/%m/%Y %H:%M')
print(start,end)

pqgappintable=driver.find_element("id","idInputFieldRequete")
time.sleep(3) 
pqgappintable.send_keys("APPPQG")
starttime=driver.find_element("id","tagsQuaCommonFilter.quaPeriodsSelectFilter.dateRange.start")
starttime.clear()
starttime.send_keys(start)
endtime=driver.find_element("id","tagsQuaCommonFilter.quaPeriodsSelectFilter.dateRange.end")
endtime.clear()
endtime.send_keys(end)


exportfnction="validateFormExcelExport('vehiclesSearchQUAForm');"
driver.execute_script(exportfnction)
time.sleep(3) 
lowertimefct="components.dateRange.schemaSelected('vehiclesSearchQUAForm','tagsQuaCommonFilter.quaPeriodsSelectFilter.dateRange',true,'22/08/2023 06:00','29/08/2023 09:00', '');"
driver.execute_script(lowertimefct)
