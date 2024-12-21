import undetected_chromedriver as uc
import streamlit as st

# Initialize Selenium WebDriver
def init_driver():
    # Automatically handles ChromeDriver installation and configuration
    driver = uc.Chrome(headless=True)
    return driver

st.title("Selenium in Streamlit: Final Fix")

if st.button("Run Browser Test"):
    try:
        driver = init_driver()
        st.write("Driver initialized successfully.")
        driver.get("https://www.google.com")
        st.success(f"Page title: {driver.title}")
        driver.quit()
    except Exception as e:
        st.error(f"An error occurred: {e}")
