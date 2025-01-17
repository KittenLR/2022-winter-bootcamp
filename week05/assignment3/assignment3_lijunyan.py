# 注意 - Copy this file and rename as assignment3_{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as assignment3_{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as assignment3_{first_name}.py then complete code with a PR.

# Q1.
"""
请实现 2个python list 的 ‘cross product’ function.
要求按照Numpy 中cross product的效果: https://numpy.org/doc/stable/reference/generated/numpy.cross.html
只实现 1-d list 的情况即可.

x = [1, 2, 0]
y = [4, 5, 6]
cross(x, y)
> [12, -6, -3]
"""
import numpy as np
import pandas as pd


# 只考虑三维叉积
def cro_product(x, y):
    list = []
    for i in range(0, len(x)):
        if i < len(x) - 1:
            a = x[i:i + 2]
            b = y[i:i + 2][::-1]
            c = np.multiply(a, b)
            print(c)
            list.append(c[0] - c[1])
        elif i == len(x) - 1:
            a = np.array(x)[[0, i]]
            b = np.array(y)[[0, i]][::-1]
            c = np.multiply(a, b)
            list.append(c[1] - c[0])
    b=list.pop(0)
    list.append(b)
    return list

cro_product([1, 2, 0], [4, 5, 6])


cro_product([1, 2, 0], [4, 5, 6])

# Q2.
"""
交易传输指令经常需要验证完整性，比如以下的例子
{ 
    request : 
    { 
        order# : 1, 
        Execution_details: ['a', 'b', 'c'],
        request_time: "2020-10-10T10:00EDT"
    },
    checksum:1440,
    ...
}
可以通过很多种方式验证完整性，假设我们通过判断整个文本中的括号 比如 '{}', '[]', '()' 来判断下单是否为有效的。
比如 {{[],[]}}是有效的，然而 []{[}](是无效的。 
写一个python 程序来进行验证。
 def checkOrders(orders: [str]) -> [bool]:
 return a list of True or False.
checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"] return [True, False, True, True, False]
"""


def checkOrders(orders: [str]) -> [bool]:
    check_list = []
    left_dict = {'{': '}', '[': ']', '(': ')'}
    for item in orders:
        if len(item) % 2 != 0 or len(item) == 1:
            check_list.append(False)
            continue

        for char in left_dict.keys():
            r = 1
            list = []
            if item.count(char) == 0:
                continue
            a = item.count(char)
            start = 0
            end = len(item)
            for i in range(0, a):
                list.append(item.index(char, start, end))
                list.append(item.rindex(left_dict[char], start, end))
                start = item.index(char, start, end)
                end = item.rindex(left_dict[char], start, end)
            for j in range(0, a):
                if (list[j] + list[j + a]) % 2 == 0:
                    r = 0
                    break
        check_list.append(r == 1)

    return check_list


checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"])


# Q3
"""
我们在进行交易的时候通常会选择一家broker公司而不是直接与交易所交易。
假设我们有20家broker公司可以选择 (broker id is [0, 19])，通过一段时间的下单表现(完成交易的时间)，我们希望找到最慢的broker公司并且考虑与其解除合约。
我们用简单的数据结构表达broker公司和下单时间: [[broker id, 此时秒数]]
[[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
解读: 
Broker 0 使用了2s - 0s = 2s
Broker 1 使用了5 - 2 = 3s
Broker 2 使用了7 - 5 = 2s
Broker 0 使用了16-7 = 9s
Broker 3 使用了19-16=3s
Broker 4 使用了25-19=6s
Broker 2 使用了35-25=10s
综合表现，是broker2出现了最慢的交易表现。

Def slowest(orders: [[int]]) -> int:

slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) return 2
"""


def slowest(orders: [[int]]) -> int:
    brokers = pd.DataFrame(orders)
    columns = ['broker', 'time']
    brokers.columns = columns
    first_lag = brokers.loc[0, 'time']
    time_lag = brokers.diff().fillna(first_lag)
    brokers['time_lag'] = time_lag['time']
    return brokers.groupby('broker')['time_lag'].sum().idxmax()


# Q4
"""
判断机器人是否能返回原点

一个机器人从平面(0,0)的位置出发，他可以U(向上), L(向左), R(向右), 或者D(向下)移动一个格子。
给定一个行走顺序，问是否可以回到原点。

例子
1. moves = "UD", return True.
2. moves = "LL", return False.
3. moves = "RRDD", return False.
4. moves = "LDRRLRUULR", return False.

def judgeRobotMove(moves: str) -> bool:

"""


def judgeRobotMove(moves: str) -> bool:
    list = ['U', 'D', 'L', 'R']
    dict = { key :0 for key in list}
    for i in str:
        if i in list:
            dict[i] += 1
    return dict['U'] == dict['D'] and dict['L'] == dict['R']


# Q5
"""
假设我们获得了一只股票的每日价格, 在这一天可以执行T+1买或卖的操作, 只能做多不能做空，每次只能持仓一股。
对于给定的价格序列，只能执行最多两次交易，写一个算法计算最高获利可以是多少。

Input: prices = [2,2,6,1,2,4,2,7]
Output: 10
解释: 6 - 2 + 7 - 1 = 10

Input: prices = [5, 3, 0]
Output: 0
解释: 没有交易。

Input: prices = [1,2,3,4,5,6,7]
Output: 6
解释: 7 - 1 = 6 因为只能持仓一股，不能再没有卖出1时购买。
"""
def max_profit(prices):
    profits=0
    prices = pd.DataFrame(prices)
    prices.columns = ['price']
    for i in range(0,2):
        if prices['price'].idxmax() > prices['price'].idxmin():
            profits += prices['price'].max() - prices['price'].min()
            prices.drop([prices['price'].idxmax(), prices['price'].idxmin()] , inplace=True)
        else:
            break
    return profits
max_profit([1,2,3,4,5,6,7])


