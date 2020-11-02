from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
 
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver.get('https://www.asos.com/men/hoodies-sweatshirts/hoodies/cat/?cid=15427&ctaref=hp|mw|prime|feature|4|category|hoodies')
driver.maximize_window()
 
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)
 
 
path = './'
fileName = 'example'
data = {}
 
while True:
    try:
        for x in range(72):
            x += 1
            time.sleep(2)
            driver.find_element_by_xpath(f'/html/body/main/div/div/div/div[2]/div/div[1]/section/article[{str(x)}]/a/div[1]/img').click()
            time.sleep(2)
            try:
                name = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/h1').text
                price = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[1]/div[2]/div/span/span[4]/span[1]').text
                price = price.replace("£", "")
                color = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[2]/div[2]/div[3]/section/div/div/span').text
                images = []
                for d in range(10):
                    try:
                        img = driver.find_element_by_xpath('/html/body/main/div[1]/section[1]/div/div[1]/div/div[2]/div[1]/div[2]/div[' +str(d)+']/div/div/div/div[1]/div[1]/div[3]/div/div/img')
                        src = img.get_attribute('src')
                        images.append(src)
                    except:
                        pass
            except:
                pass
            data[name] = []
            data[name].append({
                'product-name': name,
                'price': price,
                'color': color,
                'image': images,
            })
            print(f"Product {str(x)} is done.")
            writeToJSONFile(path, fileName, data)
            driver.back()
    except Exception as err:
        print(err)