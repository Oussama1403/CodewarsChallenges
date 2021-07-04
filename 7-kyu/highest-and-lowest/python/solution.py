def high_and_low(numbers):
    n = [int(x) for x in numbers.split()]
    string = str(max(n))+" "+str(min(n))
    return string