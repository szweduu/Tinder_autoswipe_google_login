from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()
sleep(2)
cookies=driver.find_element(By.CLASS_NAME, value='lxn9zzn')
cookies.click()
sleep(3)
def error():
    try:
        cookies1=driver.find_element(By.XPATH, value='//*[@id="s608155990"]/div/div[1]/div[1]/button')
        cookies1.click()
    except NoSuchElementException:
        print("x")
error()

click_login = driver.find_element(By.XPATH, value='//*[@id="s-1958430230"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
click_login.click()
sleep(2)

original_window = driver.current_window_handle

login=driver.find_element(By.XPATH, value='//*[@id="s-876596071"]/div')

login.click()

google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(driver.title)

email=driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
email.send_keys("szmichal224@gmail.com")

continue1=driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button')
continue1.click()
sleep(3)

password=driver.find_element(By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(GOOGLE_PASSWORD)

continue2=driver.find_element(By.XPATH, value='//*[@id="passwordNext"]/div/button')
continue2.click()

# sleep(2)
# continue3=driver.find_element(By.XPATH, value='//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button')
# continue3.click()

driver.switch_to.window(original_window)
print(driver.title)
#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="s608155990"]/div/div[1]/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="s608155990"]/div/div[1]/div/div/div[3]/button[2]')
notifications_button.click()

cookies1 = driver.find_element(By.XPATH, '//*[@id="s-1958430230"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies1.click()

sleep(7)
# for n in range(100):
#
#     #Add a 1 second delay between likes.
#     sleep(1)
#
#     print("called")
#     like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div/div/div/main/div/div/div/div/button')
#     like_button.click()

actions = ActionChains(driver)
for n in range(100):
    sleep(3)
    try:
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()



    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
    try:
        skip_button = driver.find_element(By.XPATH,
                                          value='//*[@id="s608155990"]/div/div/div[2]/button[2]')
        skip_button.click()
    except NoSuchElementException:
        sleep(2)
    try:
        close_button = driver.find_element(By.XPATH, value='// *[ @ id = "s608155990"] / div / div / div[1] / button')
        close_button.click()
    except NoSuchElementException:
        sleep(2)








