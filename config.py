# =========================
# 中华历法 ICS 生成器配置
# =========================

# 📅 时间范围
START_YEAR = 2026
END_YEAR = 2035   # 先用10年测试，后面再改30年/50年

# 📌 功能开关
SHOW_WEEK = True          # 星期
SHOW_ZODIAC = True        # 星座
SHOW_LUNAR = True         # 农历（后面实现）
SHOW_SOLAR_TERM = True    # 节气（后面实现）
SHOW_FESTIVAL = True      # 节日（后面实现）
SHOW_COUNTDOWN = True     # 倒计时（后面实现）

# 📁 输出路径
OUTPUT_FILE = "output/china_calendar.ics"

# 🕒 时区（先不用，后面扩展）
TIMEZONE = "Asia/Shanghai"