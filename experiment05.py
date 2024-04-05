def get_user_numbers():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return numbers


def write_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + '\n')
            
def sort_and_write(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    
    sorted_numbers = sorted(numbers)

    with open(output_filename, 'w') as file:
        for num in sorted_numbers:
            file.write(str(num) + '\n')


user_numbers = get_user_numbers()
write_to_file('T1.txt', user_numbers)

print("Contents of T1.txt:")
with open('T1.txt', 'r') as file:
    print(file.read())

sort_and_write('T1.txt', 'T2.txt')

print("\nContents of T2.txt (sorted):")
with open('T2.txt', 'r') as file:
    print(file.read())
