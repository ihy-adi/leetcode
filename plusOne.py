class Solution(object):
    def plusOne(self, digits):
    
        n = len(digits)
        digits[-1] = digits[-1] + 1

        def check(digits, n):
            if digits[n-1]>9:
                digits[n-1] = 0
                if n-1 == 0:
                    digits.insert(0, 1)
                else:
                    digits[n-2] += 1
                    check(digits, n-1)
                    return
            else:
                return
            
        check(digits, n)
        return digits
        
