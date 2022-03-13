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


def cross_product(x: [int], y: [int]) -> [int]:
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


assert cross_product([1, 2, 0], [4, 5, 6]) == [12, -6, -3]

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


def check_orders(orders: [str]) -> [bool]:
    patterns = {")": "(", "}": "{", "]": "["}
    return [check_order(o, patterns) for o in orders]


def check_order(order: str, patterns: {str: str}) -> bool:
    stack = []  # append, pop
    for c in order:
        if c in patterns:  # right
            if len(stack) == 0 or stack.pop() != patterns[c]:
                return False
        else:  # left or non-parentheses
            stack.append(c)

    return len(stack) == 0


assert check_orders(["()", "(", ")", "{}[]", "[][][]", "[{]{]"]) == [True, False, False, True, True, False]

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


def slowest_broker(orders: [[int]]) -> int:
    brokers = [0 for i in range(20)]
    prev_time = 0
    for o in orders:
        b_id = o[0]
        time_spent = o[1] - prev_time
        prev_time = o[1]
        brokers[b_id] = max(brokers[b_id], time_spent)

    (_, idx) = max((v, idx) for idx, v in enumerate(brokers))
    return idx


assert slowest_broker([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) == 2

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


def judge_robot_move(moves: str) -> bool:
    pos = [0, 0]  # x, y
    move_pos = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for m in moves:
        if m in move_pos:
            pos[0] += move_pos[m][0]
            pos[1] += move_pos[m][1]
        else:
            return False
    return pos == [0, 0]


assert judge_robot_move("UD")
assert not judge_robot_move("LDRRLRUULR")

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

#              2,3,1,4,3    ---> 1 +3 =4
# price  0     2 3 1 4 3
# cost1  100   2 2 1 1 1   ====> min(cost1, price)
# profit1 0    0 1 1 3 3   ====> max(profit1, price - cost1)
# cost2  100   2 2 0 0 0   ====> min(cost2, price - profit1) !!
# profit2 0    0 1 1 4 4   ====> max(profit2, price - cost2)


def max_profit2(prices: [float]) -> float:
    cost1, cost2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0

    for p in prices:
        cost1 = min(cost1, p)
        profit1 = max(profit1, p - cost1)
        cost2 = min(cost2, p - profit1)
        profit2 = max(profit2, p - cost2)

    return profit2


assert max_profit2([2, 2, 6, 1, 2, 4, 2, 7]) == 10
