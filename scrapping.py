# Importing required libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

# Setup
chromedriver = "C:/chromedriver-win64/chromedriver.exe"
s = Service(chromedriver)

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver = webdriver.Chrome(service=s, options=options)

# Open the website
driver.get('https://www.m*s*ar*p*i*e.com/')
driver.maximize_window()

# Selecting Mobiles
mobiles = driver.find_element(by=By.XPATH, value='//*[@id="Banner"]/aside/div/div/a[1]/div[2]')
time.sleep(2)
mobiles.click()

# Selecting All Phones
time.sleep(5)
all_phones = driver.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div[2]/a')
time.sleep(2)
all_phones.click()

# Selecting price range because we want smartphones data and by default it also contains feature phones
time.sleep(5)
price_start = driver.find_element(by=By.XPATH, value='//*[@id="content-section-bottom"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/input')
time.sleep(2)
price_start.send_keys(Keys.BACK_SPACE)
price_start.send_keys('5000')  # On the basis of domain knowledge generally smartphones price is greater than 5000
price_start.send_keys(Keys.ENTER)

count = 1

while True:
    # current page source
    time.sleep(5)
    current_page_source = driver.page_source

    # Saving page source into HTML file
    with open("web_content.html", "a", encoding="utf-8") as file:
        file.write(current_page_source)
    print(f"Page {count} data saved.")

    try:
        # Waiting for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="pgntn__item js-pgntn__item" and contains(text(), "Next")]'))
        )

        # finding the "Next" button
        actions = ActionChains(driver)
        actions.move_to_element(next_button).perform()
        time.sleep(2)

        # Waiting for loading the page
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((By.CLASS_NAME, "js-fltr-ldng-mask"))
        )

        # Clicking the "Next" button
        next_button.click()
        count += 1

    except StaleElementReferenceException:
        print("Encountered StaleElementReferenceException. Retrying...")
        continue  

    except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Encountered an issue: {e}. No more pages to scrape or failed to find the Next button.")
        break

driver.quit()