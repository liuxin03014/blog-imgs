import json
import os

# 定义一个函数来获取当前的版本号并递增 patch 部分
def get_new_version(jspack):
    # 如果 package.json 文件中没有 version 字段，则初始化为 1.0.0
    if 'version' not in jspack:
        jspack['version'] = '1.0.0'

    # 解析当前版本号
    major, minor, patch = map(int, jspack['version'].split('.'))

    # 递增 patch 部分（你也可以选择递增 minor 或 major）
    patch += 1

    # 返回新的版本号
    new_version = f"{major}.{minor}.{patch}"
    return new_version

# 读取 package.json 并更新版本号
try:
    with open("package.json", 'r', encoding='utf-8') as f:
        jspack = json.load(f)
except FileNotFoundError:
    print("Error: package.json 文件未找到!")
    exit(1)
except json.JSONDecodeError:
    print("Error: package.json 文件格式错误!")
    exit(1)

# 获取新的版本号
new_version = get_new_version(jspack)

# 更新 version 字段
jspack['version'] = new_version

# 将更新后的内容写回 package.json
try:
    with open("package.json", 'w', encoding='utf-8') as f:
        json.dump(jspack, f, ensure_ascii=False, indent=2)  # 格式化输出（indent=2）
    print(f"package.json 文件已更新，新的版本号为 {new_version}")
except IOError:
    print("Error: 无法写入 package.json 文件!")
    exit(1)
