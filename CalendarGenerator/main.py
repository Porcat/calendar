from config import START_YEAR, END_YEAR
from ics_writer import generate_ics

print("=" * 40)
print("中华历法 ICS 生成器 v0.1")
print("=" * 40)

print(f"年份范围：{START_YEAR} - {END_YEAR}")
print("开始生成...")

# 先只测试ICS生成
generate_ics()

print("完成！")