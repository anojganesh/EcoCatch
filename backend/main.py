from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_waterbody_info(waterbody):
    fishONLineURL = "https://www.lioapplications.lrc.gov.on.ca/fishonline/Index.html?viewer=FishONLine.FishONLine&locale=en-CA" 

    if waterbody and len(waterbody) > 3:
        # create a new Firefox session
        driver = webdriver.Firefox()
        driver.get(fishONLineURL)
        driver.implicitly_wait(5)
        # Get button and click it
        #python_button = driver.find_element(By.ID, 'DisclaimerAcceptButton')
        #driver.execute_script("arguments[0].scrollIntoView(true);", python_button)
        #python_button.click()

        element = driver.find_element(By.CLASS_NAME, 'modal')
        driver.execute_script("arguments[0].remove();", element)
        python_button2 = driver.find_element(By.ID, 'btnLakeName')
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.CLASS_NAME, 'splash-overlay')))
        python_button2.click() #click search waterbody button
        #enter text
        text_field = driver.find_element(By.ID, 'txtWbSearchName')
        text_field.send_keys(waterbody)
        driver.implicitly_wait(1)
        text_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        #get water body
        waterbodylist = driver.find_element(By.CLASS_NAME, 'folResultsContent') 
        if waterbodylist:
            ul_element = waterbodylist.find_element(By.TAG_NAME, 'ul')
            first_child = ul_element.find_element(By.TAG_NAME, 'li')
            wbBtn = ul_element.find_element(By.TAG_NAME, 'button')
            first_child3 = ul_element.find_element(By.TAG_NAME, 'div')
            wbName1 = ul_element.find_element(By.TAG_NAME, 'span')
            
            wbBtn.click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'folWaterbodyTab')))
            child_divs = driver.find_elements(By.CLASS_NAME, 'folWaterbodyIdentifyRow')
            zone = ""
            city = ""
            town = ""
            district = ""
            for child in child_divs:
                childText = child.find_element(By.TAG_NAME, 'strong').text
                
                if childText == 'Fisheries Management Zone:':
                    zone = child.find_element(By.TAG_NAME, 'span').text
                elif childText == 'Municipality:':
                    city = child.find_element(By.TAG_NAME, 'span').text
                elif childText == 'Geographic Township:':
                    town = child.find_element(By.TAG_NAME, 'span').text
                elif childText == 'MNRF District:':
                    district = child.find_element(By.TAG_NAME, 'span').text

            cords = driver.find_element(By.CLASS_NAME, "folCoordinates")
            cordsText = cords.find_element(By.TAG_NAME, "span").text
            #break down cordinate string into float
            long = float(cordsText[0:6])
            lat = float(cordsText[11:17])
            print(cordsText[9])
            print(cordsText[19])
            if cordsText[8] == "S":
                long = long*-1
            if cordsText[19] == "W":
                lat = lat*-1
            #div4 = driver.find_element(By.CSS_SELECTOR, '.folWaterbodyIdentifyRow:nth-child(4)')
            #zone = div4.find_element(By.TAG_NAME, 'span')
            #div3 = driver.find_element(By.CSS_SELECTOR, '.folWaterbodyIdentifyRow:nth-child(6)')
            #city = div3.find_element(By.TAG_NAME, 'span')
            #div2 = driver.find_element(By.CSS_SELECTOR, '.folWaterbodyIdentifyRow:nth-child(7)')
            #town = div2.find_element(By.TAG_NAME, 'span')
            #div1 = driver.find_element(By.CSS_SELECTOR, '.folWaterbodyIdentifyRow:nth-child(8)')
            #district = div1.find_element(By.TAG_NAME, 'span')
            
            
            
            print("Loading results for", waterbody, ":\n")
            print("Fishing Zone: ", zone)
            print("Municipality: ", city)
            print("Township: ", town)
            print("MNRF District: ", district)
            print("Coordinates: ", str(long) + ", " + str(lat))
        
    else:
        print("Error, Invalid prompt")
        
    driver.quit()
    return [zone, long, lat, city, town, district]