def format_currency(amount_str: str) -> int:
    # 移除货币符号和逗号
    cleaned_amount = amount_str.replace("$", "").replace(",", "").strip()

    # 转换为浮点数并返回
    return int(cleaned_amount)
