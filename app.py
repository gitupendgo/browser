from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import streamlit as st

# Initialize Selenium WebDriver
def init_driver():
    # Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Path to chromedriver (ensure it's in the same directory as app.py)
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Streamlit App
st.title("Selenium in Streamlit")
if st.button("Run Browser Test"):
    driver = init_driver()
    driver.get("https://www.google.com")
    st.write(f"Page title: {driver.title}")
    driver.quit()
