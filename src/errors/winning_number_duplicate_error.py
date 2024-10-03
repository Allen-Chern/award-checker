from typing import List

from errors.base_error import BaseError


class WinningNumberDuplicateError(BaseError):
    # 獎號重複錯誤

    def __init__(self, duplicate_numbers: List[int]):
        self.message = f"傳入的獎號重複: {duplicate_numbers}"
        super().__init__(self.message)
