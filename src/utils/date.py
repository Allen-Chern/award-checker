from datetime import datetime


def convert_to_roc_date_str(date: datetime) -> str:
    year = date.year - 1911

    return f"{year}/{date.month:02d}/{date.day:02d}"
