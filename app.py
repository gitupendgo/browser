import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# Initialize Selenium WebDriver
def init_driver():
    # Setup Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Specify chromedriver location
    chromedriver_path = "./chromedriver"  # This file must be uploaded to GitHub
    service = Service(chromedriver_path)
    
    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Streamlit UI
st.title("Browser Testing Framework")

# Input field for a website URL
url = st.text_input("Enter the URL to visit", "https://www.google.com")

# Button to run the browser test
if st.button("Run Browser Test"):
    st.write("Initializing browser...")
    try:
        # Start browser
        driver = init_driver()
        driver.get(url)
        
        # Fetch and display the page title
        page_title = driver.title
        st.success(f"Page Title: {page_title}")
        
        # Close the browser
        driver.quit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
