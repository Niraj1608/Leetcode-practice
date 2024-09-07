class Solution:
    def atoi(self, s, num, sign=1, started=False):
        # Base case: If the string is empty, return the accumulated number
        if not s:
            return sign * num
        
        # If the current character is a whitespace and we haven't started parsing digits, skip it
        if s[0].isspace() and not started:
            return self.atoi(s[1:], num, sign, started)
        
        # Handle sign at the beginning of the string
        if (s[0] == '-' or s[0] == '+') and not started:
            sign = -1 if s[0] == '-' else 1
            return self.atoi(s[1:], num, sign, True)
        
        # If the current character is not a digit, stop the recursion and return the accumulated number
        if not s[0].isdigit():
            return sign * num
        
        # Accumulate the number
        num = num * 10 + int(s[0])
        
        # Continue the recursion with the rest of the string
        return self.atoi(s[1:], num, sign, True)

    def myAtoi(self, s: str) -> int:
        # Call the recursive function with initial values
        result = self.atoi(s.strip(), 0, 1, False)
        
        # Clamp the result to fit within the 32-bit signed integer range
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
