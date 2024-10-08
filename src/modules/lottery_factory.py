from modules.big_lotto import BigLotto
from modules.daily_lotto import DailyLotto
from modules.lottery import Lottery
from modules.lottery_type import LotteryType
from modules.power_lotto import PowerLotto
from modules.thirty_nine_lotto import ThirtyNineLotto


def lottery_factory(lottery_type: LotteryType) -> Lottery:
    if lottery_type == LotteryType.BIG_LOTTO:
        return BigLotto()
    elif lottery_type == LotteryType.POWER_LOTTO:
        return PowerLotto()
    elif lottery_type == LotteryType.DAILY_LOTTO:
        return DailyLotto()
    elif lottery_type == LotteryType.THIRTY_NINE_LOTTO:
        return ThirtyNineLotto()
