import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = float(sys.argv[4])
e = float(sys.argv[5])

inputs = [a, b, c, d, e]

if not all(isinstance(num, (int, float)) for num in inputs):
    print("Error: All inputs must be numeric.")
    sys.exit()
else:
    if any(num < 0 for num in inputs):
        print("Error: Negative numbers are not allowed.")
        sys.exit()
    
    average = sum(inputs) / len(inputs)
    print(f"Average: {average}")
    print(f"Average Greater Than 50: {'Yes' if average > 50 else 'No'}")

    positive_count = sum(1 for num in inputs if num > 0)
    print(f"Count of Positives: {'Even' if positive_count & 1 == 0 else 'Odd'}")

    filtered_list = sorted([num for num in inputs if num > 10])
    print(f"Original List: {', '.join(map(str, inputs))}")
    print(f"Filtered List (values > 10): {', '.join(map(str, filtered_list))}")
