from datetime import date
from modules.solar_terms import get_all_solar_terms


# =========================
# 节日
# =========================
IMPORTANT_EVENTS = {
    "01-01": "元旦",
    "02-14": "情人节",
    "05-01": "劳动节",
    "06-01": "儿童节",
    "10-01": "国庆节",
}


# =========================
# 节气事件
# =========================
def build_solar_term_events():
    return get_all_solar_terms()


# =========================
# 通用计算函数
# =========================
def _calc_next(current, events):
    closest_name = None
    min_days = 999999

    for md, name in events.items():

        m, d = map(int, md.split("-"))
        event_date = date(current.year, m, d)

        if event_date < current:
            event_date = date(current.year + 1, m, d)

        diff = (event_date - current).days

        if diff < min_days:
            min_days = diff
            closest_name = name

    return closest_name, min_days


# =========================
# 对外接口：节日倒计时
# =========================
def get_next_festival(current):
    return _calc_next(current, IMPORTANT_EVENTS)


# =========================
# 对外接口：节气倒计时
# =========================
def get_next_solar_term(current):
    return _calc_next(current, build_solar_term_events())