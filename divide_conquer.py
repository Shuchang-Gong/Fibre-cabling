"""
Fibre cabling problem
solve by divide and conquer and only takes O(n*lg(n))
"""

import sys

def main():
    while True:
        line = sys.stdin.readline().strip().split()
        length = len(line)
        a_list = [0] * length
        if length == 1 and line[0] == "1":
            return
        else:
            for i in range(length):
                a_list[i] = int(line[i])
        max_num = max_profit(a_list, 0, length-1)
        print(max_num)

def max_profit(a_list, left, right):
    middle = (left + right) // 2
    if (left - right) == 0:
        if a_list[right] >= 0:            
            return a_list[right]
        else:
            return 0        

    num = 0
    left_num = 0
    for i in range(middle, left-1, -1):
        num = num + a_list[i]
        if num > left_num:
            left_num = num

    num = 0
    right_num = 0
    for i in range(middle+1,right+1):
        num = num + a_list[i]
        if num > right_num:
            right_num = num

    total = right_num + left_num
    return max(max_profit(a_list, left, middle), max_profit(a_list, middle + 1, right), total)

main()
