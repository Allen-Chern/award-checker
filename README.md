#### 使用套件請查看 requirements.txt

若要安裝請使用

```
pip install -r requirements.txt
```

#### 簡單測試方法

修改 `src/main.py`，main 函數中的 user_inputs 參數，

並執行

```
python src/main.py
```

參數說明

- lottery_type: 彩券種類
  - 大樂透 `LotteryType.BIG_LOTTO`
  - 威力彩 `LotteryType.POWER_LOTTO`
  - 今彩 539 `LotteryType.DAILY_LOTTO`
- draw_date: 開獎日期，格式為 `YYYY-MM-DD`
- chosen_winning_numbers: 選擇獎號
  - 威力彩範例 `[[1, 2, 3, 4, 5, 6], [1]]` (index 0 為選號，index 1 為特別號)
  - 其他玩法範例 `[[1, 2, 3, 4, 5, 6]]`
