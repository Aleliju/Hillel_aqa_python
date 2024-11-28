from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


driver = Chrome()
driver.get("http://localhost:8000/dz.html")
driver.switch_to.frame(driver.find_element(By.ID, 'frame1'))
frame1_input = driver.find_element(By.CSS_SELECTOR, 'input[id="input1"]')
frame1_input.send_keys("Frame1_Secret")
frame1_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="verifyInput(\'input1\')"]')
frame1_button.click()
alert1 = driver.switch_to.alert
alert_text1 = alert1.text
assert alert_text1 == 'Верифікація пройшла успішно!'
logger.info("First assert Done")
alert1.accept()

driver.switch_to.default_content()

WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'frame2')))
driver.switch_to.frame(driver.find_element(By.ID, 'frame2'))
frame2_input = driver.find_element(By.CSS_SELECTOR, 'input[id="input2"]')
frame2_input.send_keys("Frame2_Secret")
frame2_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="verifyInput(\'input2\')"]')
frame2_button.click()
alert2 = driver.switch_to.alert
alert_text2 = alert2.text
assert alert_text2 == 'Верифікація пройшла успішно!'
logger.info("Second assert Done")
alert2.accept()
driver.quit()