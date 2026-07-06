import numpy as np
import matplotlib.pyplot as plt

states = ["00", "01", "10", "11"]

whole = np.array([0.5, 0.0, 0.0, 0.5])
cut = np.array([0.25, 0.25, 0.25, 0.25])

mask = whole > 0
phi = np.sum(whole[mask] * np.log2(whole[mask] / cut[mask]))

x = np.arange(len(states))

plt.figure(figsize=(7, 4))
plt.bar(x - 0.2, whole, 0.4, label="Whole system")
plt.bar(x + 0.2, cut, 0.4, label="Cut system")

plt.xticks(x, states)
plt.ylim(0, 0.7)
plt.xlabel("Future state")
plt.ylabel("Probability")
plt.title(f"IIT Example: Two Dancers Moving Together\nPhi = {phi:.1f} bit")
plt.legend()
plt.tight_layout()

plt.savefig("iit_dancers_plot.png")
plt.show()


# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
