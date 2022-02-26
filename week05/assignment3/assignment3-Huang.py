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


def crossproduct(a, b):
    if len(a) == 2 and len(b) == 2:
        return a[0] * b[1] - a[1] * b[0]
    else:
        if len(a) == 2:
            a.append(0)
        if len(b) == 2:
            b.append(0)
        return [a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0]]


x = [1, 2]
y = [4, 5, 6]
a = [1, 2]
b = [4, 5]

assert crossproduct(x, y) == [12, -6, -3]
assert crossproduct(a, b) == -3
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
    orders_checked = []
    for item in orders:
        stack = []
        boolean = True
        for i in item:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    boolean = False
            elif i == "]":
                if not stack or stack.pop() != "[":
                    boolean = False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    boolean = False
        if stack:
            boolean = False
        orders_checked.append(boolean)
    return orders_checked


assert checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"]) == [True, False, True, True, False]
assert checkOrders(["({)", "())", "{[}]", "([])[]", "[[{]}]"]) == [False, False, False, True, False]
# Q3
"""
我们在进行交易的时候通常会选择一家broker公司而不是直接与交易所交易。
假设我们有20家broker公司可以选择 (broker id is 0...19)，通过一段时间的下单表现(完成交易的时间)，我们希望找到最慢的broker公司并且考虑与其解除合约。
我们用简单的数据结构表达broker公司和下单时间: [[broker id, 此时秒数]]
[[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]
解读: 
Broker 0 使用了0s - 2s = 2s
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
    broker_slowest = 0
    performance_slowest = 0
    time = 0
    for item in orders:
        if item[1] - time > performance_slowest:
            performance_slowest = item[1] - time
            broker_slowest = item[0]
        time = item[1]
    return broker_slowest


assert slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]) == 2
assert slowest([[0, 2], [1, 5], [2, 7], [11, 16], [3, 19], [4, 25], [8, 30]]) == 11

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
    position = [0, 0]
    for move in moves:
        if move == "L":
            position[1] = position[1] - 1
        elif move == "R":
            position[1] = position[1] + 1
        elif move == "U":
            position[0] = position[0] + 1
        elif move == "D":
            position[0] = position[0] - 1
    return position == [0, 0]


assert judgeRobotMove("UD") == True
assert judgeRobotMove("LL") == False
assert judgeRobotMove("RRDD") == False
assert judgeRobotMove("LDRRLRUULR") == False
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


def maxprofit(prices):
    first_sell, second_sell, first_buy, second_buy = 0, 0, 0, 0
    for i in range(0, len(prices)):
        if i == 0:
            first_sell = 0
            second_sell = 0
            first_buy = prices[i]
            second_buy = prices[i]
        else:
            first_sell = max(first_sell, prices[i] - first_buy)
            first_buy = min(first_buy, prices[i])
            second_sell = max(second_sell, prices[i] - second_buy)
            second_buy = min(second_buy, prices[i] - first_sell)
    return second_sell


prices = [2, 2, 6, 1, 2, 4, 2, 7]
# print(maxprofit(prices))
assert maxprofit(prices) == 10

prices = [5, 3, 0]
assert maxprofit(prices) == 0

prices = [1, 2, 3, 4, 5, 6, 7]
assert maxprofit(prices) == 6

# first_sell = max(first_sell, prices(i) - first_buy)
# first_buy = min(first_buy, prices(i))
# second_sell = max(second_sell, prices(i) - second_buy)     first_sell + max_prices(i) - min_prices(i)
# second_buy = min(second_buy, prices(i)- first_sell)        find min prices(i)
# reference: https://blog.csdn.net/qq_41231926/article/details/84451773
