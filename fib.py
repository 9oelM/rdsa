class Solution:
    def fib(self, N: 'int') -> 'int':
        sequence = [0,1,1]
        for i in range(3,N+1):
            print(i)
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[N]

sol = Solution()
print(sol.fib(5))