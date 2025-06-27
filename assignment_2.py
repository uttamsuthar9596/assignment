# Assignment 2: YouTube - Search Results Scraper
# �� URL:
# https://www.youtube.com/
# Search Keyword: Python Tutorial, AI, Agents
# �� Objective:
# Scrape metadata of first 50 videos from the search result.
# Extract:
#  Video Title
#  Channel Name
#  Views
#  Upload Date
#  Video URL




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

search_query = "Python Tutorial AI Agents"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com/results?search_query=" + search_query.replace(" ", "+"))
time.sleep(2)

for _ in range(15):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)

videos = driver.find_elements(By.XPATH, '//ytd-video-renderer')[:50]

results = []
for video in videos:
    title = video.find_element(By.ID, 'video-title').text
    url = video.find_element(By.ID, 'video-title').get_attribute('href')
    channel = video.find_element(By.CLASS_NAME, 'ytd-channel-name').text
    views = video.find_element(By.XPATH, './/span[contains(text(),"views")]').text
    date = video.find_element(By.XPATH, './/span[contains(text(),"ago")]').text

    results.append({
        'Video Title': title,
        'Channel Name': channel,
        'Views': views,
        'Upload Date': date,
        'Video URL': url
    })
        
with open(r"C:\Users\Lenovo\Desktop\youtube_results.json", 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
print('json file saved : C:\Users\Lenovo\Desktop\youtube_results.json')
driver.quit()
