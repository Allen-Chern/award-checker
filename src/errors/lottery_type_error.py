from errors.base_error import BaseError


class LotteryTypeError(BaseError):
    # 不合法的彩券類型錯誤

    def __init__(self):
        self.message = f"請輸入合法的彩券類型"
        super().__init__(self.message)
