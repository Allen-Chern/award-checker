from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List


# 共用回應類別
@dataclass
class PrizeResult:
    title: str
    amount: int


# 抽象類別
class Lottery(ABC):
    @abstractmethod
    def validate_winning_numbers(self, chosen_winning_numbers: List[List[int]]) -> bool:
        # WinningNumbersLengthError
        """
        若傳入的長度有誤, 請 raise WinningNumbersLengthError

        威力彩範例: #二維陣列中, index 0 為第一區, index 1 為第二區, 若某一區沒有錯誤, 請回傳空陣列
        error_numbers = [[1, 2, 3, 4, 5, 6, 7], [1, 2]]
        raise WinningNumbersLengthError(length_error_numbers=error_numbers)

        其他玩法範例:
        error_numbers = [[1, 2, 3, 4, 5, 6, 7]]
        raise WinningNumbersLengthError(length_error_numbers=error_numbers)
        """

        # WinningNumberRangeError
        """
        若傳入的獎號超出範圍, 請找出並 raise WinningNumberRangeError

        威力彩範例: #二維陣列中, index 0 為第一區, index 1 為第二區, 若某一區沒有錯誤, 請回傳空陣列
        error_numbers = [[99, 100], [10]]
        raise WinningNumberRangeError(range_error_numbers=error_numbers)

        其他玩法範例:
        error_numbers = [[99, 100]]
        raise WinningNumberRangeError(range_error_numbers=error_numbers)
        """

        return True

    @abstractmethod
    def check_prize_eligibility(
        self, draw_date: datetime, chosen_winning_numbers: List[List[int]]
    ) -> PrizeResult:
        # DrawDateError
        """
        若找不到指定日期的開獎資訊, 請 raise DrawDateError, 以下為範例
        raise DrawDateError(draw_date=draw_date)
        """
        # 若符合開獎規則，請回傳 PrizeResult
        pass
