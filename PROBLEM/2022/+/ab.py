'''from abc import ABCMeta,abstractmethod
class Food(metaclass=ABCMeta):
    @abstractmethod
    def a(self):
        pass
class Pizaa(Food):
    def a(self):
        print("fs")

class Burger(Food):
    pass

'''
def maxNumber(nums1, nums2, k):
    def fn(arr, k):
        """Return largest sub-sequence of arr of size k."""
        ans = []
        for i, x in enumerate(arr):
            while ans and ans[-1] < x and len(ans) + len(arr) - i > k:
                ans.pop()
            if len(ans) < k:
                ans.append(x)
        return ans

    ans = [0] * k
    for i in range(k + 1):
        if k - len(nums2) <= i <= len(nums1):
            val1 = fn(nums1, i)
            val2 = fn(nums2, k - i)
            cand = []
            i1 = i2 = 0
            while i1 < len(val1) or i2 < len(val2):
                if val1[i1:] >= val2[i2:]:
                    cand.append(val1[i1])
                    i1 += 1
                else:
                    cand.append(val2[i2])
                    i2 += 1
            ans = max(ans, cand)
    return ans


ina1 = input().split(',')
ina2 = input().split(',')
innum = int(input())
inarr1 = []
inarr2 = []
for i in ina1:
    inarr1.append(int(i))
for i in ina2:
    inarr2.append(int(i))

a = inarrRe = maxNumber(inarr1, inarr2, innum)
for i in range(len(a)-1):
    print(a[i],end=',')
print(a[len(a)-1])
