class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l_list = []
        for i in str(x):
            l_list.append(i)
            
        if str(x).endswith("0"):
            l_list.pop()
        else:
            pass
        if str(x).startswith("-"):
            c = l_list.pop(0)
            l_list = l_list[::-1]
            l_list = [str(i) for i in l_list]
            str1 = "".join(l_list)
            str2 = c + str1
            num = int(str2)
            
        else:
            l_list = l_list[::-1]
            l_list = [str(i) for i in l_list]
            str1 = "".join(l_list)
            num = int(str1)
        return num

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
