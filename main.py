import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import argparse

parser = argparse.ArgumentParser(description='Get tweet text and screenshot')
parser.add_argument('url', type=str, help='URL of tweet')
parser.add_argument('--output-text', type=str, help='Output text file')
parser.add_argument('--output-screenshot', type=str, help='Output screenshot file')
args = parser.parse_args()

target_url = args.url
tweet_id = target_url.split("/")[-1]
if args.output_text:
    output_text = args.output_text
else:
    output_text = f'{tweet_id}_text.txt'
if args.output_screenshot:
    output_screenshot = args.output_screenshot
else:
    output_screenshot = f'{tweet_id}_screenshot.png'

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
xpath_tweettext = '//*[@data-testid="tweetText"]/span'

try:
    driver.get(target_url)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_tweettext)))
    result = driver.find_elements(by=By.XPATH, value=xpath_tweettext)
    for element in result:
        # save text to file text_<tweet_id>.txt
        with open(output_text, 'w') as f:
            f.write(element.text)
    # take screenshot
    driver.set_window_size(800, 800)
    driver.save_screenshot(output_screenshot)
finally:
    # Close the browser
    driver.quit()
