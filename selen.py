from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
options = Options()
DRIVER_PATH = './chromedriver'
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
driver.get('https://www.nike.com/fr/t/chaussure-air-max-90-ltr-pour-6mdj2K/CZ5594-100?nikemt=true&cp=30566810280_search_%7c%7c10690195814%7c108495198474%7c%7cc%7cFR%7ccssproducts%7c453050557176_GEOZ&ds_rl=1252249&gclid=CjwKCAjwvuGJBhB1EiwACU1AicBH57SIX3lW3ACTcqbD-ELqbsJoKq234i2HsOy1o0c1dM2Tt2tCLRoCR60QAvD_BwE&gclsrc=aw.ds')



a=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div[3]/form/div[1]").is_enabled()
javaScript = "window.scrollBy(0,1000);"
driver.execute_script(javaScript)



