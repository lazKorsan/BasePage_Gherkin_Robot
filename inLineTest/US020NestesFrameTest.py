from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriver'ı başlat
driver = webdriver.Chrome()  # veya kullandığınız tarayıcı için uygun WebDriver'ı belirtin

try:
    # Sayfayı aç
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Üst çerçeveye geçiş (frame-top)
    driver.switch_to.frame("frame-top")

    # Sol çerçeveye geçiş (frame-left)
    driver.switch_to.frame("frame-left")
    # LEFT metnini bul ve yazdır
    left_element = driver.find_element(By.XPATH, "//body")
    print("LEFT:", left_element.text)

    # Kapsayıcıdan çık
    driver.switch_to.parent_frame()

    # Orta çerçeveye geçiş (frame-middle)
    driver.switch_to.frame("frame-middle")
    # MIDDLE metnini bul ve yazdır
    middle_element = driver.find_element(By.XPATH, "//div[@id='content']")
    print("MIDDLE:", middle_element.text)

    # Kapsayıcıdan çık
    driver.switch_to.parent_frame()

    # Sağ çerçeveye geçiş (frame-right)
    driver.switch_to.frame("frame-right")
    # RIGHT metnini bul ve yazdır
    right_element = driver.find_element(By.XPATH, "//body")
    print("RIGHT:", right_element.text)

    # Asıl çerçeveye geri dön
    driver.switch_to.default_content()

    # Alt çerçeveye geçiş (frame-bottom)
    driver.switch_to.frame("frame-bottom")

    # BOTTOM metnini bul ve yazdır
    bottom_element = driver.find_element(By.XPATH, "//body")
    print("BOTTOM:", bottom_element.text)

finally:
    # Tarayıcıyı kapat
    driver.quit()
