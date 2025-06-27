# Assignment 1: Forum Threads Scraper (Reddit)
# �� Target Subreddit: https://www.reddit.com/r/Python/
# �� Objective:
# Scrape the top 100 posts from a given subreddit.
# Extract:
#  Post Title
#  Author
#  Upvotes
#  Number of Comments
#  Post URL
#  Post Time
# �� Instructions:
#  Use Playwright or Selenium.
#  Scroll to load at least 50 posts.
#  Output in JSON or CSV format.
#  Skip ads or promoted content.



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

options = Options()


driver = webdriver.Chrome(options=options)

url = "https://www.reddit.com/r/Python/"
driver.get(url)
time.sleep(3)

results = []
seen_titles = set()

scrolls = 10
for _ in range(scrolls):
    print(_)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    posts = driver.find_elements(By.XPATH, "//shreddit-post")
    time.sleep(2)
    for post in posts:

        post_title = post.get_attribute("post-title")
        if not post_title or post_title in seen_titles:
            continue

        author = post.get_attribute("author")
        upvotes = post.get_attribute("score")
        comments = post.get_attribute("comment-count")
        post_url = post.get_attribute("content-href")
        post_time = post.get_attribute("created-timestamp")

        post_data = {
            "Post Title": post_title,
            "Author": author,
            "Upvotes": upvotes,
            "Number of Comments": comments,
            "Post URL": post_url,
            "Post Time": post_time
        }
        results.append(post_data)
        seen_titles.add(post_title)
        if len(results) >= 100:
            break
    if len(results) >= 100:
        break


with open(r"C:\Users\Lenovo\Desktop\Assignment\reddit_rpython_top_posts.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
print('json saved : C:\Users\Lenovo\Desktop\Assignment\reddit_rpython_top_posts.json')
driver.quit()

