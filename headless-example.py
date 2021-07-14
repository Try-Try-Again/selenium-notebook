# %% codecell
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
# %% codecell
#  _   _ _____    _    ____  _     _____ ____ ____    __  __  ___  ____  _____
# | | | | ____|  / \  |  _ \| |   | ____/ ___/ ___|  |  \/  |/ _ \|  _ \| ____|
# | |_| |  _|   / _ \ | | | | |   |  _| \___ \___ \  | |\/| | | | | | | |  _|
# |  _  | |___ / ___ \| |_| | |___| |___ ___) |__) | | |  | | |_| | |_| | |___
# |_| |_|_____/_/   \_\____/|_____|_____|____/____/  |_|  |_|\___/|____/|_____|
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
# %% codecell
browser.set_window_size(320, 480) #resize to phone
browser.get('http://lakeviewdata.com') #travel to a website
# %% codecell
login_organism = browser.find_element_by_id('id_login_organism')
login_organism.screenshot("screenshot.png") #take a screenshot of a div
# %% codecell
browser.quit()
# %% codecell
