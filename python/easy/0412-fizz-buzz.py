class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        new_arr = []
    
        for i in range(1,n+1):
            if (i % 3 != 0 and i % 5 != 0):
                new_arr.append(str(i))
            elif i % 15 == 0:
                new_arr.append("FizzBuzz")
            elif i % 3 == 0:
                new_arr.append("Fizz")
            else:
                new_arr.append("Buzz")
        return new_arr