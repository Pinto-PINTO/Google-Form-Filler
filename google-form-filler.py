from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Doesnt open the Window at each execution
chrome_options = Options()
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(options=chrome_options)

# Use only this if you want to see the Window (Comment Line 9,10,12)
#driver = webdriver.Chrome()

# Form Link
driver.get('https://forms.gle/a8zHA9tBaXgPkofEA')


# --------------------------------------------------------------------
# ----------------------------- Select 1 -----------------------------
# --------------------------------------------------------------------
try:
    iframe1 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe1)
except:
    pass  

# Find and click the "No" radio button
radio_button_xpath = '//span[contains(text(), "No")]'
wait = WebDriverWait(driver, 10)
radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
radio_button.click()
# --------------------------------------------------------------------
# ----------------------------- Select 1 -----------------------------
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# ----------------------------- Select 2 -----------------------------
# --------------------------------------------------------------------
try:
    iframe2 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe2)
except:
    pass  

# Find and click the "The product ratings are inaccurate" checkbox
checkbox_xpath = '//span[contains(text(), "The product ratings are inaccurate.")]'
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
checkbox.click()
# --------------------------------------------------------------------
# ----------------------------- Select 2 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 3 -----------------------------
# --------------------------------------------------------------------
try:
    iframe3 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe3)
except:
    pass  

# Find and click the "Often" radio button
radio_button_xpath = '//span[contains(text(), "Often")]'
wait = WebDriverWait(driver, 10)
radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
radio_button.click()
# --------------------------------------------------------------------
# ----------------------------- Select 3 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 4 -----------------------------
# --------------------------------------------------------------------
try:
    iframe4 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe4)
except:
    pass  

# Find and click the "Read customer reviews" checkbox
checkbox_xpath = '//span[contains(text(), "Read customer reviews")]'
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
checkbox.click()
# --------------------------------------------------------------------
# ----------------------------- Select 4 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 5 -----------------------------
# --------------------------------------------------------------------
try:
    iframe6 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe6)
except:
    pass  

# Find and click the "4" radio button
radio_button_xpath = '//span[contains(text(), "To what extent do you consider customer reviews")]/following::div[text()="4"]'
wait = WebDriverWait(driver, 10)
radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
radio_button.click()
# --------------------------------------------------------------------
# ----------------------------- Select 5 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 6 -----------------------------
# --------------------------------------------------------------------
try:
    iframe6 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe6)
except:
    pass  

# Find and click the "4" radio button
radio_button_xpath = '//span[contains(text(), "To what extent will an accurate rating for a smartphone")]/following::div[text()="5"]'
wait = WebDriverWait(driver, 10)
radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
radio_button.click()
# --------------------------------------------------------------------
# ----------------------------- Select 6 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 7 -----------------------------
# --------------------------------------------------------------------
# try:
#     iframe9 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
#     driver.switch_to.frame(iframe9)
# except:
#     pass  # If there is no iframe, continue without switching

# # Locate the "Yes" radio button and click it
# try:
#     yes_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Yes"]/ancestor::div[@role="radio"]')))
#     yes_button.click()
# except:
#     print("Could not find or click the 'Yes' option.")

# driver.switch_to.default_content()
# --------------------------------------------------------------------
# ----------------------------- Select 7 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 8 -----------------------------
# --------------------------------------------------------------------
input_field = driver.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')  
input_field.send_keys("Ebay")
# --------------------------------------------------------------------
# ----------------------------- Select 8 -----------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------------------------- Select 9 -----------------------------
# --------------------------------------------------------------------
# input_field = driver.find_element(By.CLASS_NAME, 'whsOnd.zHQkBf')

# # Type "I really like it" into the input field
# input_field.send_keys("I really like it")
# --------------------------------------------------------------------
# ----------------------------- Select 9 -----------------------------
# --------------------------------------------------------------------

submit_button = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']"))
)
submit_button.click()


driver.quit()