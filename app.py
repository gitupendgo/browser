import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Initialize Selenium WebDriver
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Path to ChromeDriver
    service = Service("./chromedriver")  # Ensure this matches the file name in your repo
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Streamlit App
st.title("Selenium in Streamlit: Simple Test")

if st.button("Run Browser Test"):
    try:
        # Initialize the WebDriver
        driver = init_driver()
        st.write("Driver initialized successfully.")

        # Perform a simple test: Open Google and fetch the page title
        driver.get("https://www.google.com")
        page_title = driver.title
        st.success(f"Page title: {page_title}")

        # Close the WebDriver
        driver.quit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
