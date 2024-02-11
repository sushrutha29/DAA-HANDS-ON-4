1. Implement the solutions and upload it to github
sol:  printfib(5) -> fib(5)
            -> fib(4) -> fib(3)
                       -> fib(2) -> fib(1) -> 1
                                  -> fib(0) -> 0
                       -> fib(1) -> 1
            -> fib(3) -> fib(2) -> fib(1) -> 1
                                  -> fib(0) -> 0
                       -> fib(1) -> 1


2. Prove the time complexity of the algorithms
sol: The basic recursive Fibonacci algorithm has an exponential time complexity, represented as O(2^n), where n is the Fibonacci function's input parameter. The structure of the procedure, which requires making two recursive calls, fib(n-1) and fib(n-2), for every value of n. As a result, the number of function calls and processing steps to increase exponentially. This means that the time required for this approach for calculating Fibonacci numbers increases exponentially with the amount of the input.


3. Comment on way's you could improve your implementation (you don't need to do it just discuss it)
sol:
Memoization: To save and reuse previously computed results, utilize memoization. This can improve the algorithm's performance and significantly reduce the number of unnecessary calculations, especially for bigger values of n.

Bottom-Up Dynamic Programming: Use bottom-up dynamic programming, often known as an iterative technique, to implement the Fibonacci sequence. This involves removing the recursion overhead by building the solution from the smallest subproblems upwards.

Matrix Exponentiation: Investigate complicated algorithms, such as matrix exponentiation, to calculate Fibonacci numbers in logarithmic time. For very large values of n, this may offer an improved approach. 

