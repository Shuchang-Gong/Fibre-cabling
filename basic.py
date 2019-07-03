"""
Fibre cabling problem
take integers and find the maximum num by summing the nums
"""

import sys

def main():
    while True:
        line = sys.stdin.readline().strip().split()
        length = len(line)
        a_list = [0] * length
        if length == 1 and line[0] == "1":
            return      # if only input 1, halt
        else:
            for i in range(length):
                a_list[i] = int(line[i])
            max_profit(a_list)
            
def max_profit(a_list):
    max_num = 0
    for i in range(len(a_list)):
        n = 0
        for j in range(i,len(a_list)):
            n = n + a_list[j]
            if n > max_num:
                max_num = n
    print(max_num)

main()
