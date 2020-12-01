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