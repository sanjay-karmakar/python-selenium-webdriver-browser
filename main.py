# pip install selenium
from idlelib import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()  # Keeps the search input visible on Wikipedia's layout
# driver.get("https://www.amazon.in/ASUS-Processor-5050-8GB-Upgradeable-FA608UHI-TU238WS/dp/B0H9YWCNVG?ref=dlx_deals_dg_dcl_B0H9YWCNVG_dt_sl10_1a_pi&pf_rd_r=QT2H37MG9V2RCTYV5HJY&pf_rd_p=da3a0150-1c0d-49da-a217-66ad62b72c1a&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")
#
# price_holder = driver.find_element(By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div .a-price-whole").text
# print(price_holder)

# driver.get("https://www.python.org/")
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
#
# # for time in event_names:
# #     print(time.text)
#
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
# print(events)


# Wikipedia Challenge
driver.get("https://en.wikipedia.org/wiki/Main_Page")
active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount a span")
# print(f"Total number of active users: {active_editors.text}")


# Events like clicking anchor tag
link_element = driver.find_element(By.LINK_TEXT, value="Content portals")
# link_element.click()


# Find the "Search" <input> by name
search_inp = driver.find_element(By.NAME, value="search")
search_inp.send_keys("Python", Keys.ENTER)








driver.quit()