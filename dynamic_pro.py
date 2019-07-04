"""
Fibre cabling problem
solve by dynamic programming and only takes O(n)
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
        max_profit(a_list)
                    
def max_profit(a_list): 
	max_num = 0
	num = 0
	for i in range(len(a_list)): 
		num = num + a_list[i] 
		if max_num < num: 
			max_num = num 
		if num < 0: 
			num = 0
	print(max_num) 

main()
