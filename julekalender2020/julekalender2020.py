def openluke(number):
    """
    Open a juleluke
    Args:
        number (int): number of juleluke (1-24)
    Returns:
        solution (int): the luke solution
    """

    solution = 0
    print(f"Opening luke number: {number}.")

    if (number == 0):
      solution = -1

    print(f"Solution is: {solution}.")

    return solution

# A optimized school method based 
# Python3 program to check 
# if a number is prime 
 
def isPrime(n): 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True