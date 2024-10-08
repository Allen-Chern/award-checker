from datetime import datetime
from typing import List

from bs4 import BeautifulSoup

from errors.draw_date_error import DrawDateError
from errors.winning_number_range_error import WinningNumberRangeError
from errors.winning_numbers_length_error import WinningNumbersLengthError
from modules.lottery import Lottery, PrizeResult
from utils.date import convert_to_roc_date_str
from utils.html import fetch_rendered_html
from utils.str import format_currency


# 實作類別
class ThirtyNineLotto(Lottery):
    url = "https://www.taiwanlottery.com/lotto/result/39_m5"

    def validate_winning_numbers(self, chosen_winning_numbers: List[List[int]]) -> bool:
        # 檢查是否有長度問題, 39樂合彩可以選 2~4 個號碼
        numbers_length = len(chosen_winning_numbers[0])
        if numbers_length < 2 or numbers_length > 4:
            error_numbers = [chosen_winning_numbers[0]]
            raise WinningNumbersLengthError(length_error_numbers=error_numbers)

        # 檢查每個號碼是否在 1~39 之間
        out_of_range_numbers = []
        for number in chosen_winning_numbers[0]:
            if number < 1 or number > 39:
                out_of_range_numbers.append(number)
        if out_of_range_numbers:
            error_numbers = [out_of_range_numbers]
            raise WinningNumberRangeError(range_error_numbers=error_numbers)

        return True

    def check_prize_eligibility(
        self, draw_date: datetime, chosen_winning_numbers: List[List[int]]
    ) -> PrizeResult:
        # 39樂合彩只會用第一區號碼判斷
        chosen_numbers = chosen_winning_numbers[0]
        roc_date_str = convert_to_roc_date_str(draw_date)

        # 取得 html
        html = fetch_rendered_html(self.url)
        soup = BeautifulSoup(html, "html.parser")

        # 遍歷 result-item
        result_items = soup.find_all("div", class_="result-item")
        for item in result_items:
            # 取得 period-date
            period_date_div = item.find("div", class_="period-date")
            if period_date_div and roc_date_str in period_date_div.text:
                # 找到對應的 result-item，拿到獎號
                ball_numbers = []
                balls = item.find_all("div", class_="ball")
                for ball in balls:
                    ball_number_str = ball.text.strip()
                    if ball_number_str != "":
                        ball_number = int(ball_number_str)
                        ball_numbers.append(ball_number)

                # 檢查 chosen_numbers 是否全部都在 ball_numbers 裡面
                if all(
                    chosen_number in ball_numbers for chosen_number in chosen_numbers
                ):
                    prize_infos = item.find_all("div", class_="tab")
                    match len(chosen_numbers):
                        case 2:
                            amount = self.get_amount(prize_infos[2])
                            return PrizeResult(title="二合", amount=amount)
                        case 3:
                            amount = self.get_amount(prize_infos[1])
                            return PrizeResult(title="三合", amount=amount)
                        case 4:
                            amount = self.get_amount(prize_infos[0])
                            return PrizeResult(title="四合", amount=amount)
                else:
                    return PrizeResult(title="未中獎", amount=0)

        # 如果沒有找到對應的 result-item，則拋出 DrawDateError
        raise DrawDateError(draw_date=draw_date)

    def get_amount(self, prize_info_div) -> int:
        amount_str = prize_info_div.find_all("div", class_="tab-body-row-data")[1].text
        return format_currency(amount_str)
