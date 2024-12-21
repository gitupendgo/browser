import streamlit as st
from playwright.sync_api import sync_playwright

st.title("Playwright Browser Test")

if st.button("Run Browser Test"):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.google.com")
            st.success(f"Page title: {page.title()}")
            browser.close()
    except Exception as e:
        st.error(f"An error occurred: {e}")
