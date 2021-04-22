from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-features=EnableEphemeralFlashPermission")

chrome_prefs = {"profile.default_content_setting_values.plugins": 1,
                "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
                "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
                "PluginsAllowedForUrls": "BEST URL EVER"}

chrome_options.add_experimental_option("prefs",chrome_prefs)
page = webdriver.Chrome(os.path.expanduser("~/Desktop/chromedriver"), chrome_options=chrome_options, service_log_path='NUL')


page.get("https://pokemon-planet.com/")

def pageControl():
    try:
        if "Fullcreen" in page.current_url:
            input("Bekliyorum!")
            try:
                flash = page.find_element_by_tag_name("object")
                flash.click()
                flash.send_keys("wwww")
            except:
                pass


        if "Unlock Session" in page.title:
            try:
                os.system('afplay /System/Library/Sounds/Glass.aiff')
            except:
                pass
    except:
        pass
 
while True:
    pageControl()



#catch id= catch
#tustan sonraki sayfa title Wild Battle
#tus name= Start Battle
#<input class="btn-battle-action" type="submit" value="Throw Pokeball" name="useitem_TQ2MTN">
