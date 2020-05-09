from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from multiprocessing.dummy import Pool as ThreadPool
import time
import random
options = Options()
options.headless = True
import os
def fun():
 count = 0
 lister = 0
 list = ["http://yamechanic.com/CTLT","http://yamechanic.com/He4f","http://velocicosm.com/3Xbm","http://kudoflow.com/6mBy","http://raboninco.com/OEbU","http://raboninco.com/Mtmy"]   
 while True:
  time.sleep(random.randint(0,5))
      
  driver = webdriver.Firefox(options=options)
  driver.get(list[lister])
  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'skip_bu2tton'))).click()
  driver.quit()
  os.system("sudo anonsurf change")
  count = count + 1
  if lister == 5:
    lister = 0
  else:  
    lister = lister + 1
  print('{}\r'.format(str(count)+" --> ID Changed dont use internet")) 

fun()
