import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

## check if argv is passed
if len(sys.argv) < 2:
    print("Usage: python main.py <url>")
    sys.exit(1)

# Configuration for Chrome Driver
chrome_options = Options()
chrome_options.add_argument("--user-agent=" + "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('--disable-gpu')
binary_location_candidates = ['/usr/bin/chromium', '/usr/bin/google-chrome', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
driver_location_candidates = ['/usr/bin/chromedriver', '/usr/local/bin/chromedriver', '/opt/homebrew/bin/chromedriver']
binary_location = None
driver_location = None
for binary in binary_location_candidates:
    if os.path.exists(binary):
        binary_location = binary
        break
for driver in driver_location_candidates:
    if os.path.exists(driver):
        driver_location = driver
        break
driver = uc.Chrome(options=chrome_options, browser_executable_path=binary_location, driver_executable_path=driver_location)
# Login page of credit card web site
target_url = sys.argv[1] # https://x.com/username/status/1234567890
tweet_id = target_url.split("/")[-1]
# Find <div data-testid="tweetText"> element
xpath_tweettext = '//*[@data-testid="tweetText"]/span'
# xpath_username = '//*[@data-testid="User-Name"]/div/div/div/a/div/span'
# xpath_tweet = '//*[@data-testid="tweet"]'

try:
    driver.get(target_url)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_tweettext)))
    result = driver.find_elements(by=By.XPATH, value=xpath_tweettext)
    for element in result:
        # save text to file text_<tweet_id>.txt
        with open(f'text_{tweet_id}.txt', 'w') as f:
            f.write(element.text)
    # take screenshot
    driver.set_window_size(800, 800)
    driver.save_screenshot(f'screenshot_{tweet_id}.png')
finally:
    # Close the browser
    driver.quit()
