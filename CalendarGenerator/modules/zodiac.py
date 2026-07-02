# =========================
# 十二星座计算模块
# =========================

def get_zodiac(month, day):
    """
    根据月日返回星座
    """

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "♒ 水瓶座"
    if (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "♓ 双鱼座"
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "♈ 白羊座"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "♉ 金牛座"
    if (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "♊ 双子座"
    if (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "♋ 巨蟹座"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "♌ 狮子座"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "♍ 处女座"
    if (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "♎ 天秤座"
    if (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "♏ 天蝎座"
    if (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "♐ 射手座"
    return "♑ 摩羯座"