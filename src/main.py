from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

from errors.draw_date_error import DrawDateError
from errors.fetch_html_timeout_error import FetchHtmlTimeoutError
from errors.lottery_type_error import LotteryTypeError
from errors.winning_number_range_error import WinningNumberRangeError
from errors.winning_numbers_length_error import WinningNumbersLengthError
from modules.lottery_factory import lottery_factory
from modules.lottery_names import lottery_names
from modules.lottery_type import LotteryType


@dataclass
class UserInputs:
    lottery_type: LotteryType
    draw_date: datetime
    chosen_winning_numbers: List[List[int]]


def get_user_inputs() -> UserInputs:
    # 取得使用者輸入的彩券類型
    lottery_type = None
    is_valid = False
    while not is_valid:
        lottery_type_str = input("請輸入彩券類型: ")
        try:
            lottery_type = LotteryType.from_string(lottery_type_str)
            is_valid = True
        except LotteryTypeError as error:
            print(error)

    # 取得使用者輸入的開獎日期
    draw_date = None
    current_date = datetime.now()
    is_valid = False
    while not is_valid:
        draw_date_str = input("請輸入開獎日期: ")
        try:
            draw_date = datetime.strptime(draw_date_str, "%Y-%m-%d")
            if (
                draw_date.month == current_date.month
                and draw_date.year == current_date.year
            ):
                is_valid = True
            else:
                print("目前僅供查詢當月開獎日期")
        except ValueError as error:
            print("請輸入正確的日期格式")

    # 取得使用者輸入的號碼
    chosen_winning_numbers: List[List[int]] = []
    has_second_zone = lottery_type == LotteryType.POWER_LOTTO
    is_valid = False
    while not is_valid:
        zone_name = "第一區" if has_second_zone else ""
        chosen_zone_numbers_str = input(f"請以逗號分隔輸入{zone_name}獎號:")
        try:
            chosen_zone_numbers = [
                int(number) for number in chosen_zone_numbers_str.split(",")
            ]
            duplicate_numbers = get_duplicate_numbers(chosen_zone_numbers)
            if not duplicate_numbers:
                chosen_winning_numbers.append(chosen_zone_numbers)
                is_valid = True
            else:
                print(f"輸入的號碼重複: {duplicate_numbers}")
        except ValueError as error:
            print("請輸入正確的號碼格式")

    is_valid = False
    if has_second_zone:
        while not is_valid:
            chosen_zone_numbers_str = input("請輸入第二區獎號:")
            try:
                chosen_zone_numbers = [
                    int(number) for number in chosen_zone_numbers_str.split(",")
                ]
                chosen_winning_numbers.append(chosen_zone_numbers)
                is_valid = True
            except ValueError as error:
                print("請輸入正確的號碼格式")

    return UserInputs(
        lottery_type=lottery_type,
        draw_date=draw_date,
        chosen_winning_numbers=chosen_winning_numbers,
    )


def get_duplicate_numbers(chosen_winning_numbers: List[int]) -> List[int]:
    seen = set()
    duplicates = set()

    for number in chosen_winning_numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    print(
        f"歡迎來到台彩兌獎小幫手, 目前系統僅提供當月兌獎功能\n兌獎項目為 1.大樂透 2.威力彩 3.今彩539 4.39樂合彩 (請以代號輸入)\n開獎日期請依格式輸入, 例如 {today}\n"
    )
    user_inputs = get_user_inputs()
    # user_inputs = UserInputs(
    #     lottery_type=LotteryType.THIRTY_NINE_LOTTO,
    #     draw_date=datetime.strptime("2024-10-7", "%Y-%m-%d"),
    #     chosen_winning_numbers=[[2, 10]],
    # )
    lottery = lottery_factory(user_inputs.lottery_type)

    try:
        lottery.validate_winning_numbers(user_inputs.chosen_winning_numbers)
    except WinningNumbersLengthError as error:
        print(error)
        return
    except WinningNumberRangeError as error:
        print(error)
        return

    try:
        prize_result = lottery.check_prize_eligibility(
            user_inputs.draw_date, user_inputs.chosen_winning_numbers
        )

        lottery_name = lottery_names.get(user_inputs.lottery_type)
        draw_date_formatted = user_inputs.draw_date.strftime("%Y-%m-%d")
        print(f"\n{lottery_name}於 {draw_date_formatted} 的兌獎結果:")
        if prize_result.amount > 0:
            print(f"恭喜您中了 {prize_result.title}, 獎金為 {prize_result.amount} 元")
        else:
            print("很抱歉, 您未中獎")
    except DrawDateError as error:
        print(error)
        return
    except FetchHtmlTimeoutError as error:
        print(error)
        return


main()
