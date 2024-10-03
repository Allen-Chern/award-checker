from typing import List

from errors.base_error import BaseError


class WinningNumbersLengthError(BaseError):
    # 獎號長度錯誤

    def __init__(self, length_error_numbers: List[List[int]]):
        if len(length_error_numbers) == 1:
            self.message = f"傳入的獎號長度不合法: {length_error_numbers[0]}"
        else:
            zone_one = length_error_numbers[0] if length_error_numbers[0] else "無"
            zone_two = length_error_numbers[1] if length_error_numbers[1] else "無"
            self.message = (
                f"傳入的獎號長度不合法:\n第一區: {zone_one}\n第二區: {zone_two}"
            )
        super().__init__(self.message)
