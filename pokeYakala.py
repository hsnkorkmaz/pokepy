from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import random

page = webdriver.Chrome(os.path.expanduser("~/Desktop/chromedriver"))
page.get("https://www.delugerpg.com/login")
randomInt = [1,2]
keyList = ["move_north-west",
"move_north",
"move_north-east",
"move_west",
"move_east",
"move_south-west",
"move_south",
"move_south-east"]

mapList = ["https://www.delugerpg.com/map/overworld1",
"https://www.delugerpg.com/map/overworld2",
"https://www.delugerpg.com/map/overworld3",
"https://www.delugerpg.com/map/overworld4",
"https://www.delugerpg.com/map/overworld5",
"https://www.delugerpg.com/map/overworld6",
"https://www.delugerpg.com/map/overworld7",
"https://www.delugerpg.com/map/overworld8",
"https://www.delugerpg.com/map/overworld9",
"https://www.delugerpg.com/map/overworld10",
"https://www.delugerpg.com/map/overworld11",
"https://www.delugerpg.com/map/overworld12",
"https://www.delugerpg.com/map/overworld13",
"https://www.delugerpg.com/map/overworld14",
"https://www.delugerpg.com/map/overworld15",
"https://www.delugerpg.com/map/overworld16",
"https://www.delugerpg.com/map/overworld17",
"https://www.delugerpg.com/map/overworld18",
"https://www.delugerpg.com/map/overworld19",
"https://www.delugerpg.com/map/overworld20",
"https://www.delugerpg.com/map/overworld21",
"https://www.delugerpg.com/map/overworld22",
"https://www.delugerpg.com/map/overworld23",
"https://www.delugerpg.com/map/overworld24",
"https://www.delugerpg.com/map/overworld25",
"https://www.delugerpg.com/map/snowcave1",
"https://www.delugerpg.com/map/snowcave2",
"https://www.delugerpg.com/map/snowcave3",
"https://www.delugerpg.com/map/snowcave4",
"https://www.delugerpg.com/map/volcano1",
"https://www.delugerpg.com/map/volcano2",
"https://www.delugerpg.com/map/volcano3",
"https://www.delugerpg.com/map/volcano4",
"https://www.delugerpg.com/map/pkmntower1",
"https://www.delugerpg.com/map/pkmntower2",
"https://www.delugerpg.com/map/pkmntower3",
"https://www.delugerpg.com/map/unownruins1",
"https://www.delugerpg.com/map/unownruins2",
"https://www.delugerpg.com/map/powerplant1",
"https://www.delugerpg.com/map/powerplant2",
"https://www.delugerpg.com/map/powerplant3",
"https://www.delugerpg.com/map/pkmnmansion1",
"https://www.delugerpg.com/map/pkmnmansion2",
"https://www.delugerpg.com/map/pkmnmansion3",
"https://www.delugerpg.com/map/pkmnmansion4",
"https://www.delugerpg.com/map/rockcave1",
"https://www.delugerpg.com/map/rockcave2",
"https://www.delugerpg.com/map/rockcave3",
"https://www.delugerpg.com/map/rockcave4"]

def pageControl():
    if "Unlock Session" in page.title:
        try:
            os.system('afplay /System/Library/Sounds/Glass.aiff')
        except:
            pass

    if "Login" in page.title:
        username = page.find_element_by_name("username")
        username.send_keys("nicholaix")
        password = page.find_element_by_name("password")
        password.send_keys("05354366879")
        loginbutton = page.find_element_by_id("btn-login")
        loginbutton.click()
    
    if "Home" in page.title:
        page.get(random.choice(mapList))

    if "Try moving to another spot." in page.page_source:
        if random.choice(randomInt) == 1:
            map1 = page.find_element_by_id(random.choice(keyList))
            map1.click()
        else:
            page.get(random.choice(mapList))

    pokemonimg = None
    try:
        pokemonimg = page.find_element_by_id("pokemonimgwrap").is_displayed()
    except:
        pass
    
    if pokemonimg == True:
        try:
            catchButton = page.find_element_by_class_name("btn-catch-action")
            catchButton.click()
        except:
            pass

    if "Wild Battle" in page.title:
        print("wild battle")

        if "Try moving to another spot." in page.page_source:
            if random.choice(randomInt) == 1:
                map1 = page.find_element_by_id(random.choice(keyList))
                map1.click()
            else:
                page.get(random.choice(mapList))

        if "Return to Map" in page.page_source:
            page.get(random.choice(mapList))

        teamleft = None
        try:
            teamleft = page.find_element_by_id("teamleft").is_displayed()
        except:
            pass

        if teamleft == True:
            try:
                catchButton2 = page.find_element_by_class_name("btn-battle-action")
                catchButton2.click()
            except:
                pass
        attack = None
        try:
            attack = page.find_element_by_id("attack").is_displayed()
        except:
            pass

        if attack == True:
            try:
                print("listelendi")
                throwButton = page.find_elements_by_class_name("btn-battle-action")
                print(throwButton)
                throwButton[1].click()
            except:
                pass

while True:
    pageControl()