from datetime import datetime

from errors.base_error import BaseError


class DrawDateError(BaseError):
    # 不合法的開獎日期

    def __init__(self, draw_date: datetime):
        today = datetime.now().strftime("%Y-%m-%d")  # 獲取今天的日期
        draw_date_formatted = draw_date.strftime("%Y-%m-%d")
        if draw_date == today:
            self.message = f"尚無 {draw_date_formatted} 的開獎資訊"
        else:
            self.message = f"沒有 {draw_date_formatted} 的開獎資訊"
        super().__init__(self.message)
