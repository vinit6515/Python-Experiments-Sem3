"""def histogram(lst):
    
    count_dict = {}
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1
    pairs = [(num, count) for num, count in count_dict.items()]
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    return sorted_pairs


input_list = [4, 2, 8, 4, 6, 2, 8, 4, 1, 3, 6, 8, 8, 4]
result = histogram(input_list)
print(result)"""

def perfect(n):
    
    if not isinstance(n, int) or n <= 0:
        return False
    factors = [i for i in range(1, n) if n % i == 0]
    sum_of_factors = sum(factors)
    return sum_of_factors == n


number = 28
result = perfect(number)
print(f"{number} is a perfect number: {result}")

