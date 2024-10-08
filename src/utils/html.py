from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def fetch_rendered_html(url: str):
    # 設置 Chrome 瀏覽器
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # 啟動 Chrome 瀏覽器
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    try:
        # 訪問目標網址
        driver.get(url)

        # 等待頁面加載完成
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

        # 獲取渲染後的頁面 HTML
        html = driver.page_source
        return html
    finally:
        # 關閉瀏覽器
        driver.quit()
