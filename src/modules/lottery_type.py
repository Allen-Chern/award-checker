from enum import Enum

from errors.lottery_type_error import LotteryTypeError


# 定義 Enum 類別
class LotteryType(Enum):
    BIG_LOTTO = 1
    POWER_LOTTO = 2
    DAILY_LOTTO = 3

    @staticmethod
    def from_string(lottery_type_str: str) -> "LotteryType":
        try:
            # 將傳入的字串轉為整數並找到對應的枚舉成員
            return LotteryType(int(lottery_type_str))
        except ValueError:
            raise LotteryTypeError()
        except KeyError:
            raise LotteryTypeError()
