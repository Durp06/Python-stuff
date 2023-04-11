def calculate_average(numbers):
        total = 0

        for num in numbers:
                total+=num
        average = total / len(numbers)
        
        return average

numbers = [3, 7, 4, 9, 9]

print("The average is:", calculate_average(numbers))