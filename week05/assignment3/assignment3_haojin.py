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


def cross_product(a, b):
    c = []
    for i in range(len(a)):
        if i == 0:
            c.append(a[1] * b[2] - b[1] * a[2])
        elif i == 1:
            c.append(b[0] * a[2] - a[0] * b[2])
        else:
            c.append(a[0] * b[1] - b[0] * a[1])
    return c


print(cross_product([1, 2, 3], [4, 5, 6]))


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
    open_parenthesis = "{[("
    close_parenthesis = "}])"
    result = []
    for i in orders:
        x = []
        for j in i:
            x.append(j)
            s = []
            for k in x:
                if k in open_parenthesis:
                    s.append(k)
                elif k in close_parenthesis:
                    pos = close_parenthesis.index(k)
                    if len(s) > 0 and open_parenthesis[pos] == s[-1]:
                        s.pop()
                else:
                    result.append(False)
        if len(s) == 0:
            result.append(True)
        else:
            result.append(False)
    return result


print(checkOrders(["()", "(", "{}[]", "[][][]", "[{]{]"]))



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
    for i in range(len(orders)):
        if i == 0:
            orders[i].append(orders[i][1])
        else:
            orders[i].append(orders[i][1] - orders[i-1][1])
    orders.sort(key=lambda x: x[2])
    return orders[-1][0]


print(slowest([[0, 2], [1, 5], [2, 7], [0, 16], [3, 19], [4, 25], [2, 35]]))


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
    u = 0
    d = 0
    l = 0
    r = 0
    for i in moves:
        if i == 'U':
            u += 1
        elif i == 'D':
            d += 1
        elif i == 'L':
            l += 1
        else:
            r += 1
    if u == d and l == r:
        return True
    else:
        return False


print(judgeRobotMove('UUDD'))
print(judgeRobotMove('UUDDD'))
print(judgeRobotMove('ULLRURDD'))



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


def maxProfit(prices):
    price_copy = prices.copy()
    price_copy.sort()
    first_max_index = prices.index(price_copy[-1])
    second_max_index = prices.index(price_copy[-2])
    if (first_max_index > second_max_index) and (first_max_index - second_max_index == 1 or second_max_index - first_max_index == 1):
        profit = prices[first_max_index] - price_copy[0]
    elif first_max_index < second_max_index:
        prices_1 = prices[:first_max_index + 1]
        prices_2 = prices[first_max_index + 1:second_max_index + 1]
        prices_1.sort()
        prices_2.sort()
        profit = prices_1[-1] - prices_1[0] + prices_2[-1] - prices_2[0]
    else:
        prices_1 = prices[:second_max_index + 1]
        prices_2 = prices[second_max_index + 1:first_max_index + 1]
        prices_1.sort()
        prices_2.sort()
        profit = prices_1[-1] - prices_1[0] + prices_2[-1] - prices_2[0]
    return profit

print(maxProfit([2,2,6,1,2,4,2,7]))
print(maxProfit([5, 3, 0]))
print(maxProfit([1,2,3,4,5,6,7]))