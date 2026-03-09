from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.description_utils import description_utils

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")

    # (By, value) tuple ile:
result = description_utils(
        driver,
        locator=(By.XPATH, '/html/frameset/frame[1]'),
        highlight_colour="#00BFFF",
        circle_colour="#FF6347",
)