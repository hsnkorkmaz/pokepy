from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

page = webdriver.Chrome(os.path.expanduser("~/Desktop/chromedriver"))
page.get("https://www.delugerpg.com/login")

def pageControl():
    try:
        if "Unlock Session" in page.title:
            try:
                os.system('afplay /System/Library/Sounds/Glass.aiff')
            except:
                pass

        if "Login" in page.title:
            username = page.find_element_by_name("username")
            username.send_keys("USER")
            password = page.find_element_by_name("password")
            password.send_keys("PASSWORD")
            loginbutton = page.find_element_by_id("btn-login")
            loginbutton.click()

        if "Home" in page.title:
            page.get("https://www.delugerpg.com/battle/user/username/S-Fire")

        if "User Battle" in page.title:
            

            try:
                #print("ilk buton")
                battleButton = page.find_element_by_name("Start Battle")
                battleButton.click()
            except:
                pass
            try:
                #print("ikinci buton")
                if "Skip Pokemon Selection" in page.page_source:
                    try:
                        battle1 = page.find_elements_by_class_name("btn-battle-action")
                        battle1[1].click()
                    except:
                        pass
                else:
                    try:
                        battle2 = page.find_element_by_class_name("btn-battle-action")
                        battle2.click()
                    except:
                        pass
            except:
                pass
            try:
                if page.find_element_by_class_name("notify_done").is_displayed():
                    page.get("https://www.delugerpg.com/battle/user/username/S-Fire") 
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
