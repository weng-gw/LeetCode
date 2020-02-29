class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = (digits[-1]+1)//10
        digits[-1] = (digits[-1]+1)%10
        
        n_digit = len(digits)
        for i in range(n_digit-2,-1,-1):
            if remain == 0:
                return digits
            remain = (digits[i]+1)//10
            digits[i] = (digits[i]+1)%10
        if remain==0:
            return digits
        return [remain]+digits
