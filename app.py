import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def init_driver():
    # Ensure the ChromeDriver has correct permissions
    os.chmod("./chromedriver", 0o755)  # Set executable permissions

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service("./chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

st.title("Selenium in Streamlit: Permissions Fix Test")

if st.button("Run Browser Test"):
    try:
        driver = init_driver()
        st.write("Driver initialized successfully.")
        driver.get("https://www.google.com")
        st.success(f"Page title: {driver.title}")
        driver.quit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
