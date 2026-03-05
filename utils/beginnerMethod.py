import time

from playwright.sync_api import Page



def click_by_Xpath(page: Page, xpath: str, border_color: str, circle_color: str):
    element_handle = page.query_selector(xpath)

    """Elementi çerçeve içine alır ve merkezine bir daire çizer."""
    element_handle.evaluate(f"""(el) => {{
            // Kenarlık (Highlight) ekle
            el.style.border = '3px solid {border_color}';

            // Merkez daireyi oluştur
            const circle = document.createElement('div');
            circle.style.position = 'absolute';
            circle.style.width = '20px';
            circle.style.height = '20px';
            circle.style.borderRadius = '50%';
            circle.style.backgroundColor = '{circle_color}';
            circle.style.zIndex = '10000';
            circle.style.pointerEvents = 'none';

            // Elementin merkez koordinatlarını hesapla
            const rect = el.getBoundingClientRect();
            circle.style.left = (rect.left + rect.width / 2 - 10 + window.scrollX) + 'px';
            circle.style.top = (rect.top + rect.height / 2 - 10 + window.scrollY) + 'px';

            document.body.appendChild(circle);
        }}""")

    element_handle.click()




def sendKey_by_Xpath(page: Page, xpath: str, text: str, border_color: str, circle_color: str):
    element_handle = page.query_selector(xpath)
    """Elementi çerçeve içine alır ve merkezine bir daire çizer."""
    element_handle.evaluate(f"""(el) => {{
                // Kenarlık (Highlight) ekle
                el.style.border = '3px solid {border_color}';

                // Merkez daireyi oluştur
                const circle = document.createElement('div');
                circle.style.position = 'absolute';
                circle.style.width = '20px';
                circle.style.height = '20px';
                circle.style.borderRadius = '50%';
                circle.style.backgroundColor = '{circle_color}';
                circle.style.zIndex = '10000';
                circle.style.pointerEvents = 'none';

                // Elementin merkez koordinatlarını hesapla
                const rect = el.getBoundingClientRect();
                circle.style.left = (rect.left + rect.width / 2 - 10 + window.scrollX) + 'px';
                circle.style.top = (rect.top + rect.height / 2 - 10 + window.scrollY) + 'px';

                document.body.appendChild(circle);
            }}""")
    element_handle.fill(text)

def sendKeys_by_Xpath(page: Page, xpath: str, text: str, border_color: str, circle_color: str):
    element_handle = page.query_selector(xpath)
    """Elementi çerçeve içine alır ve merkezine bir daire çizer."""
    element_handle.evaluate(f"""(el) => {{
                // Kenarlık (Highlight) ekle
                el.style.border = '3px solid {border_color}';

                // Merkez daireyi oluştur
                const circle = document.createElement('div');
                circle.style.position = 'absolute';
                circle.style.width = '20px';
                circle.style.height = '20px';
                circle.style.borderRadius = '50%';
                circle.style.backgroundColor = '{circle_color}';
                circle.style.zIndex = '10000';
                circle.style.pointerEvents = 'none';

                // Elementin merkez koordinatlarını hesapla
                const rect = el.getBoundingClientRect();
                circle.style.left = (rect.left + rect.width / 2 - 10 + window.scrollX) + 'px';
                circle.style.top = (rect.top + rect.height / 2 - 10 + window.scrollY) + 'px';

                document.body.appendChild(circle);
            }}""")
    element_handle.fill(text)



def test_element_handle(page: Page):
    page.goto("https://practicesoftwaretesting.com/")
    click_by_Xpath(page, '(//*[@class="nav-link"])[2]', "Cyan", "Magenta")
    time.sleep(5)
    sendKey_by_Xpath(page,'//input[@data-test="email"]',"lazKorsan1767391364330@gmail.com","Cyan", "Magenta")
    time.sleep(5)

