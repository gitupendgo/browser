import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def init_driver():
    try:
        # Verify chromedriver exists
        if not os.path.exists("./chromedriver"):
            st.error("Chromedriver not found in the expected location.")
            return None

        # Ensure executable permissions
        os.chmod("./chromedriver", 0o755)

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Initialize WebDriver
        service = Service("./chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        st.error(f"Error initializing WebDriver: {e}")
        return None

st.title("Selenium in Streamlit: Improved Test")

if st.button("Run Browser Test"):
    try:
        st.write("Checking chromedriver setup...")
        st.write(f"Current directory: {os.getcwd()}")
        st.write(f"Chromedriver path exists: {os.path.exists('./chromedriver')}")

        driver = init_driver()

        if not driver:
            st.error("Driver initialization failed. Check the logs above for details.")
        else:
            st.write("Driver initialized successfully.")
            driver.get("https://www.google.com")
            st.success(f"Page title: {driver.title}")
            driver.quit()
    except Exception as e:
        st.error(f"An error occurred during browser interaction: {e}")
