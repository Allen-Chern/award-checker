from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from errors.fetch_html_timeout_error import FetchHtmlTimeoutError


def fetch_rendered_html(url: str, max_retries=3) -> str:
    # 設置 Chrome 瀏覽器
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # 啟動 Chrome 瀏覽器
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    retries = 0
    while retries < max_retries:
        try:
            # 訪問目標網址
            driver.get(url)

            # 等待頁面加載完成
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "result-area"))
            )

            # 獲取渲染後的頁面 HTML
            html = driver.page_source
            return html
        except TimeoutException:
            retries += 1
            print(f"頁面加載失敗, 重試中... ({retries}/{max_retries})")

    driver.quit()
    raise FetchHtmlTimeoutError()
