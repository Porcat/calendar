# =========================
# 专业级二十四节气系统（统一接口版）
# =========================

import ephem
from datetime import date, timedelta

# =========================
# 节气名称（按黄经顺序）
# =========================
SOLAR_TERM_NAMES = [
    "春分", "清明", "谷雨",
    "立夏", "小满", "芒种",
    "夏至", "小暑", "大暑",
    "立秋", "处暑", "白露",
    "秋分", "寒露", "霜降",
    "立冬", "小雪", "大雪",
    "冬至", "小寒", "大寒",
    "立春", "雨水", "惊蛰"
]

SOLAR_TERM_ANGLES = [i * 15 for i in range(24)]


# =========================
# 太阳黄经计算
# =========================
def get_sun_longitude(dt):
    sun = ephem.Sun()
    observer = ephem.Observer()
    observer.date = dt

    sun.compute(observer)

    ecl = ephem.Ecliptic(sun)
    lon = float(ecl.lon) * 180 / 3.141592653589793

    return lon % 360


# =========================
# 判断某天是否为节气日
# =========================
def get_solar_term_by_date(dt):
    lon = get_sun_longitude(dt)

    tolerance = 0.3

    for i, angle in enumerate(SOLAR_TERM_ANGLES):
        if abs(lon - angle) < tolerance:
            return SOLAR_TERM_NAMES[i]

    return None


# =========================
# 返回全部节气（用于倒计时）
# =========================
def get_all_solar_terms():
    # 用固定映射（用于倒计时系统）
    return {
        "01-05": "小寒",
        "01-20": "大寒",
        "02-04": "立春",
        "02-19": "雨水",
        "03-06": "惊蛰",
        "03-21": "春分",
        "04-05": "清明",
        "04-20": "谷雨",
        "05-06": "立夏",
        "05-21": "小满",
        "06-06": "芒种",
        "06-21": "夏至",
        "07-07": "小暑",
        "07-23": "大暑",
        "08-07": "立秋",
        "08-23": "处暑",
        "09-07": "白露",
        "09-23": "秋分",
        "10-08": "寒露",
        "10-23": "霜降",
        "11-07": "立冬",
        "11-22": "小雪",
        "12-07": "大雪",
        "12-21": "冬至",
    }


# =========================
# ⭐ 兼容接口（关键修复）
# =========================
def get_solar_term(month, day):
    """
    兼容旧代码（不会再报 ImportError）
    """
    from datetime import date
    return get_solar_term_by_date(date(2026, month, day))