# Enum 與名稱對應
from modules.lottery_type import LotteryType

lottery_names = {
    LotteryType.BIG_LOTTO: "大樂透",
    LotteryType.POWER_LOTTO: "威力彩",
    LotteryType.DAILY_LOTTO: "今彩",
}


def get_lottery_name(lottery_type: LotteryType) -> str:
    return lottery_names.get(lottery_type, "未知玩法")
