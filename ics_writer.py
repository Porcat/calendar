from datetime import date, timedelta
from config import START_YEAR, END_YEAR, OUTPUT_FILE

from modules.zodiac import get_zodiac
from modules.solar_terms import get_solar_term_by_date
from modules.festivals import get_solar_festival, get_lunar_festival
from modules.countdown import get_next_festival, get_next_solar_term
from lunar_python import Solar


# =========================
# 星期系统
# =========================
WEEK_MAP = {
    0: "周一",
    1: "周二",
    2: "周三",
    3: "周四",
    4: "周五",
    5: "周六",
    6: "周日",
}


# =========================
# 农历系统
# =========================
def get_lunar_info(current):

    solar = Solar.fromYmd(current.year, current.month, current.day)
    lunar = solar.getLunar()

    lunar_month = int(lunar.getMonth())
    lunar_day = int(lunar.getDay())

    lunar_text = f"{lunar.getYearInGanZhi()}年 {lunar.getMonthInChinese()}月{lunar.getDayInChinese()}"

    return lunar_text, lunar_month, lunar_day


# =========================
# 主生成器
# =========================
def generate_ics():

    start_date = date(START_YEAR, 1, 1)
    end_date = date(END_YEAR, 12, 31)

    current = start_date

    ics_lines = []

    ics_lines.append("BEGIN:VCALENDAR")
    ics_lines.append("VERSION:2.0")
    ics_lines.append("PRODID:-//China Calendar//CN")

    count = 0

    while current <= end_date:

        # ===== 基础信息 =====
        zodiac = get_zodiac(current.month, current.day)
        weekday = WEEK_MAP[current.weekday()]

        # ===== 节气（专业版）=====
        solar_term = get_solar_term_by_date(current)

        # ===== 农历 =====
        lunar_text, lunar_month, lunar_day = get_lunar_info(current)

        # ===== 节日 =====
        solar_festival = get_solar_festival(current.month, current.day)
        lunar_festival = get_lunar_festival(lunar_month, lunar_day)

        festivals = []
        if solar_festival:
            festivals.append(solar_festival)
        if lunar_festival:
            festivals.append(lunar_festival)

        festival_text = "、".join(festivals)

        # ===== 双轨倒计时 =====
        festival_name, festival_days = get_next_festival(current)
        solar_name, solar_days = get_next_solar_term(current)

        # =========================
        # SUMMARY（精简显示）
        # =========================
        if solar_term:
            summary = f"{zodiac}｜{solar_term}"
        else:
            summary = f"{zodiac}"

        # =========================
        # DESCRIPTION（完整信息）
        # =========================
        description = (
            f"日期:{current}\n"
            f"星期:{weekday}\n"
            f"农历:{lunar_text}\n"
            f"节日:{festival_text}\n"
            f"节气:{solar_term}\n"
            f"距离节日：{festival_name}还有{festival_days}天\n"
            f"距离节气：{solar_name}还有{solar_days}天"
        )

        # ===== 写入 ICS =====
        ics_lines.append("BEGIN:VEVENT")
        ics_lines.append(f"DTSTART;VALUE=DATE:{current.strftime('%Y%m%d')}")
        ics_lines.append(f"DTEND;VALUE=DATE:{(current + timedelta(days=1)).strftime('%Y%m%d')}")
        ics_lines.append(f"SUMMARY:{summary}")
        ics_lines.append(f"DESCRIPTION:{description}")
        ics_lines.append("END:VEVENT")

        current += timedelta(days=1)
        count += 1

    ics_lines.append("END:VCALENDAR")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(ics_lines))

    print("生成完成！")
    print("总天数：", count)
    print("输出文件：", OUTPUT_FILE)