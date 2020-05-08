'''
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
主要是 大数溢出问题 py。。
'''
from typing import List
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]

'''
    大数情况下：利用字符数组表示。
'''
def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return

    number = ['0'] * n
    while not Increment(number):
        PrintNumber(number)

def Increment(number):
    isOverflow = False
    nTakeOver = 0
    nLength = len(number)
    for i in range(nLength-1, -1, -1):
        nSum = int(number[i]) + nTakeOver
        if i == nLength - 1:
            nSum += 1
        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = str(nSum)
        else:
            number[i] = str(nSum)
            break

    return isOverflow

def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print('%c' % number[i], end='')
    print('')

Print1ToMaxOfNDigits(3)