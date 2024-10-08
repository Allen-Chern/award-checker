### 使用套件請查看 requirements.txt

若要安裝請使用

```
pip install -r requirements.txt
```

### 簡單測試方法

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

### 專案結構說明

```
├── README.md # 說明文件
├── requirements.txt # 定義使用套件及版本
├── src
│   ├── errors # 錯誤類別
│   │   ├── base_error.py # 基礎錯誤類別
│   │   ├── draw_date_error.py # 開獎日期錯誤類別
│   │   ├── fetch_html_timeout_error.py # 頁面加載失敗錯誤類別
│   │   ├── lottery_type_error.py # 彩券類型錯誤類別
│   │   ├── winning_numbers_length_error.py # 選號數量錯誤類別
│   │   ├── winning_number_range_error.py # 選號範圍錯誤類別
│   ├── modules # 彩券類別
│   │   ├── lottery.py # 彩券抽象類別
│   │   ├── lottery_type.py # 彩券種類列舉類別
│   │   ├── lottery_names.py # 彩券種類名稱對應函數
│   │   ├── lottery_factory.py # 彩券工廠函數
│   │   ├── big_lotto.py # 大樂透實作類別
│   │   ├── daily_lotto.py # 今彩實作類別
│   │   ├── power_lotto.py # 威力彩實作類別
│   │   ├── thirty_nine_lotto.py # 39 樂合彩實作類別
│   ├── utils # 工具類別
│   │   ├── date.py # 西元日期轉換民國日期函數
│   │   ├── html.py # 取得渲染後的網頁 HTML 函數
│   │   ├── str.py # 金額字串格式化函數
│   ├── main.py # 主程式 (流程控制)
```
