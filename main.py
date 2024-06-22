from selenium import webdriver
from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint


def func():
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.dismiss()
        print("alert accepted")

        time.sleep(randint(80, 200) / 100)

        # driver.implicitly_wait(2)

        driver.find_elements(By.TAG_NAME, "BUTTON")[0].click()

        time.sleep(randint(80, 200) / 100)

        # driver.implicitly_wait(2)

        return True

    except NoAlertPresentException:
        print("no alert")
        return False


driver = webdriver.Firefox()
driver.get('https://huggingface.co/spaces/dalle-mini/dalle-mini')

driver.implicitly_wait(5)

frame2 = driver.find_element(By.XPATH, "//iframe[@id='iFrameResizer0']")
driver.switch_to.frame(frame2)

print(driver.find_element(By.TAG_NAME, "div").get_attribute('innerHTML'))

box = driver.find_elements(By.TAG_NAME, "INPUT")[0]

box.click()
box.send_keys("futuristic astronaut")

driver.find_elements(By.TAG_NAME, "BUTTON")[0].click()

x = 0
while func():
    x += 1
    print("test n° {}".format(x))

print("end")
# driver.quit()
