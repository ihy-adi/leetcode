#roman to integer || 2 ways of solving this
class Solution(object):
    def intToRoman(self, num):

#  first way of solving
        def ones(num):
            if num < 1:
                return ""
            elif num < 4:
                return "I" * num
            elif num == 4:
                return "IV"
            elif num < 9:
                return "V" + "I" * (num - 5)
            else:
                return "IX"

        def tens(num):
            if num < 10:
                return ""
            elif num < 40:
                return "X" * (num // 10)
            elif num < 50:
                return "XL"
            elif num < 90:
                return "L" + "X" * ((num - 50) // 10)
            else:
                return "XC"

        def huns(num):
            if num < 100:
                return ""
            elif num < 400:
                return "C" * (num // 100)
            elif num < 500:
                return "CD"
            elif num < 900:
                return "D" + "C" * ((num - 500) // 100)
            else:
                return "CM"

        def thos(num):
            if num < 1000:
                return ""
            else:
                return "M" * (num // 1000)


        one = ones(num % 10)
        ten = tens(num % 100)
        hun = huns(num % 1000)
        tho = thos(num % 10000)
            
        return tho + hun + ten + one
        
#another way of solving
    #     roman_numeral = ''
    
    # # Iterate through the dictionary keys in descending order
    #     for value in sorted(vals.keys(), reverse=True):
    #         while num >= value:
    #             roman_numeral += vals[value]
    #             num -= value
        
    #     return roman_numeral


