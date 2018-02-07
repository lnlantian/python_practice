
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1 = l1[::-1]
    l2 = l2[::-1]
    l1 = [str(i) for i in l1]
    l2 = [str(i) for i in l2]
    str1 = "".join(l1)
    str2 = "".join(l2)
    l_sum = int(str1) + int(str2)
    l_list = []
    for i in str(l_sum):
        l_list.append(i)
    l_list = l_list[::-1]
    l_list = [int(i) for i in l_list]
    l_list.reverse()
    return l_list


l1 = [2,4,3]
l2 = [5,6,4]
print addTwoNumbers(l1,l2)
