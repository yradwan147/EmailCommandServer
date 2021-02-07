from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PICKUP = "Hadayek El Ahram Club"

def recommend(type, destination = "El Tahrir"):
    if type == 0:
        driver = webdriver.Firefox(executable_path=r'E:\Python Projects\Email Parser Server\Final 11-10-2020\geckodriver.exe')
        driver.get("https://www.uber.com/us/en/price-estimate/")
        time.sleep(10)
        element_pickup = driver.find_element_by_name("pickup")
        element_pickup.send_keys(PICKUP)
        time.sleep(5)
        element_pickup.send_keys(Keys.RETURN)
        element_destination = driver.find_element_by_name("destination")
        element_destination.send_keys(destination)
        time.sleep(5)
        element_destination.send_keys(Keys.RETURN)
        time.sleep(8)
        button = driver.find_element_by_xpath('//button[text()="View all options"]')
        button.click()
        try :
            price = driver.find_elements_by_css_selector("span.v6.f4.al.q8.pl")
            if not price:
                raise Exception("List is empty")
        except :
            try :
                price = driver.find_elements_by_css_selector("span.v7.f4.al.q8.pl")
                if not price:
                    raise Exception("List is empty")
            except :
                try :
                    price = driver.find_elements_by_css_selector("span.v8.f4.al.q8.pl")
                    if not price:
                        raise Exception("List is empty")
                except :
                    try :
                        price = driver.find_elements_by_css_selector("span.vt.f4.al.q8.pl")
                        if not price:
                            raise Exception("List is empty")
                    except :
                        price = driver.find_elements_by_css_selector("span.vv.f4.al.q8.pl")
                        if not price:
                            raise Exception("List is empty")
        uber = {"Scooter" : price[0].text, "Connect" : price[1].text, "Taxi" : price[2].text, "UberX" : price[3].text, 
                    "Comfort" : price[4].text, "Select" : price[5].text, "Black" : price[6].text}
        uber_string = "Finished Uber Report (" + str(time.time()) + "):\n"
        for i in uber:
            uber_string += i + " : " + uber[i] + "\n"
        return uber_string
        driver.close()
    elif type == 1:
        driver = webdriver.Firefox(executable_path=r'E:\Python Projects\Email Parser Server\Final 11-10-2020\geckodriver.exe')
        brands = ['samsung', 'xiaomi', 'oppo', 'lg']
        for i in brands:
            driver.get("https://www.techradar.com/news/best-" + i + "-phones")
            time.sleep(5)
            print("Parsing...\n")
            titles = driver.find_elements_by_class_name("title__text")
            titles_formatted = []
            specs_formatted = []
            specs_1 = []
            counter = -1
            for x in titles:
                print(x.text)
                print("iteration : " + str(x))
                titles_formatted.append(x.text)
            for u in titles_formatted:
                name = u.split(".")
                string_name = name[1]
                string_name = string_name[1:]
                string_name = string_name.lower()
                string_name = string_name.replace(" ", "-")
                try:
                    driver.get("https://www.kimovil.com/en/where-to-buy-" + string_name)
                    time.sleep(5)
                    antutu_scores = driver.find_elements_by_css_selector("span.spec.main")
                    antutu_score = antutu_scores[7]
                    specs1 = ("Antutu score: " + antutu_score.text + " | ")
                except:
                    specs1 = ("Antutu score: N/A | ")
                try:
                    driver.get("https://eg.pricena.com/en/product/" + string_name + "-price-in-egypt")
                    time.sleep(5)
                    price = driver.find_element_by_css_selector("span.lowPrice")
                    specs2 = "Price: " + price.text +  " | "
                except:
                    specs2 = "Price: N/A | "
                specs_1.append((specs1 + specs2))
            driver.get("https://www.techradar.com/news/best-" + i + "-phones")
            specs = driver.find_elements_by_class_name("specs__container")
            print(specs_1)
            for y in specs:
                counter += 1
                specs_all = specs_1[counter] + y.text
                specs_formatted.append(specs_all)
            result_string = "Results for " + i + "\n"
            for z in range(0, len(specs_formatted)):
                result_string += (titles_formatted[z] + "\n")
                result_string += (specs_formatted[z] + "\n")
            print(result_string)
        driver.close()

recommend(1)
        
