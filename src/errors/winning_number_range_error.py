from typing import List

from errors.base_error import BaseError


class WinningNumberRangeError(BaseError):
    # 獎號範圍錯誤

    def __init__(self, range_error_numbers: List[List[int]]):
        if len(range_error_numbers) == 1:
            self.message = f"傳入的獎號超出範圍: {range_error_numbers[0]}"
        else:
            zone_one = range_error_numbers[0] if range_error_numbers[0] else "無"
            zone_two = range_error_numbers[1] if range_error_numbers[1] else "無"
            self.message = f"傳入的獎號不合法:\n第一區: {zone_one}\n第二區: {zone_two}"
        super().__init__(self.message)
