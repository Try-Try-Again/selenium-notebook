# %% codecell
from selenium import webdriver
# %% start_browser
# START BROWSER
browser = webdriver.Chrome()
# %% codecell
browser.set_window_size(320, 480)
# %% codecell
browser.get('http://lakeviewdata.com') #travel to a website
# %% codecell
app_div = browser.find_element_by_id('app') #get div with id 'app'
# %% codecell
login_organism = browser.find_element_by_id('id_login_organism')
# %% codecell
login_organism.screenshot("screenshot.png") #take a screenshot of a div
# %% codecell
browser.current_url #returns url as string
# %% kill_browser
# KILL BROWSER
browser.quit()
