# Recursive approach

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# Test case #1
print(fib_rec(6)) # 8

# # Test case #2
# print(fib_rec(100)) # Code hangs, control-c to stop


# Top-Down approach of DP

def fib_dp1(n):
    # Initialized memo as a list of length n, fill with None using to store the results of sub-problems
    memo = [None] * (n+1)

    def fib(n):
        if n < 2:
            memo[n] = n
        if memo[n] is None:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)

# Test case #3
print(fib_dp1(6)) # 8

# Test case #4
print(fib_dp1(100)) # 354224848179261915075



# Iterative approach O(1) space complexity
def fib_iterative(n):
    if n < 2:
        return n

    prev1, prev2 = 0, 1  # Base cases for F(0) and F(1)
    for _ in range(2, n + 1):
        current = prev1 + prev2  # Calculate the next Fibonacci number
        prev1, prev2 = prev2, current  # Shift the variables for the next iteration

    return prev2  # The nth Fibonacci number


print(fib_iterative(6))    # Output: 8
print(fib_iterative(100))  # Output: 354224848179261915075
