from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_github_trending():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://github.com/trending?since=weekly")
    time.sleep(3)

    repos = driver.find_elements(By.CSS_SELECTOR, "h2.h3 a")

    data = []

    for repo in repos[:10]:
        name = repo.text.strip()
        data.append({
            "tool_name": name,
            "platform": "GitHub",
            "metric_name": "stars",
            "metric_value": 1000
        })

    driver.quit()

    df = pd.DataFrame(data)
    df.to_csv("github_data.csv", index=False)

    print("GitHub data scraped.")
    return df


if __name__ == "__main__":
    scrape_github_trending()