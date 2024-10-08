from errors.base_error import BaseError


class FetchHtmlTimeoutError(BaseError):
    # 頁面加載失敗

    def __init__(self):
        self.message = f"頁面加載失敗"
        super().__init__(self.message)
