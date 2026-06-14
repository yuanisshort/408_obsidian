# -*- coding: utf-8 -*-
'''
@IDE : PyCharm
@version : 3.9
@Auth : 恍惚
@time : 2026/3/26 10:52
@Description: Null
'''


# 判断 i 是否是 t 的有效倍数
def OK(i, t, n):
    return (i % t == 0) and (i // t < n)

def count_num(t1, t2, t3, t4, n):
    maxt = max(t1, t2, t3, t4)
    count = 0

    # ======================
    # 错误版本：没有 +1
    # ======================
    print("===== 错误版本（不加 +1）=====")
    count_err = 0
    for i in range(1, maxt * (n-1)):  # ❌ 这里没 +1
        if OK(i, t1, n) or OK(i, t2, n) or OK(i, t3, n) or OK(i, t4, n):
            count_err += 1
    print(f"错误统计结果：{count_err}")

    # ======================
    # 正确版本：必须 +1
    # ======================
    print("\n===== 正确版本（加上 +1）=====")
    count_correct = 0
    for i in range(1, maxt * (n-1) + 1):  # ✅ 必须 +1
        if OK(i, t1, n) or OK(i, t2, n) or OK(i, t3, n) or OK(i, t4, n):
            count_correct += 1
            # print(i)  # 想看哪些数被选中，打开这句
    print(f"正确统计结果：{count_correct}")

    return count_correct

# ======================
# 测试一下
# ======================
t1, t2, t3, t4 = 7, 5, 6, 4
n = 10  # 每个数最多取 2 个倍数

count_num(t1, t2, t3, t4, n)