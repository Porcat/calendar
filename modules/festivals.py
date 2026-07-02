# =========================
# 中国 + 公历节日（基础版）
# =========================

FESTIVALS = {
    "01-01": "元旦",
    "02-14": "情人节",
    "03-08": "妇女节",
    "05-01": "劳动节",
    "06-01": "儿童节",
    "10-01": "国庆节",
    "12-25": "圣诞节",
}

LUNAR_FESTIVALS = {
    "01-01": "春节",
    "01-15": "元宵节",
    "05-05": "端午节",
    "07-07": "七夕节",
    "08-15": "中秋节",
    "09-09": "重阳节",
}


def get_solar_festival(month, day):
    return FESTIVALS.get(f"{month:02d}-{day:02d}")


def get_lunar_festival(lunar_month, lunar_day):
    return LUNAR_FESTIVALS.get(f"{lunar_month:02d}-{lunar_day:02d}")