def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        total_distance += distance
    return total_distance


def calculate_similarity_score(left_list, right_list):
    similarity_score = 0
    for num in left_list:
        count = right_list.count(num)
        similarity_score += num * count
    return similarity_score

def number_from_string(string):
    number = 0;
    for words in string:
        for i, char in enumerate(words):
            print(f"Index: {i}, Character: {char}")

    return number

# Read the input files
try:
    #reading 2 lists from file
    with open(r'Text/input.txt', 'r') as input_file:
        lines = [line.strip() for line in input_file]
        left_list = []
        right_list = []
        for line in lines:
            numbers = line.split()
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1]))

    #outputs
    similarity_score = calculate_similarity_score(left_list, right_list)
    total_distance = calculate_total_distance(left_list, right_list)
    numbers = number_from_string(left_list)
    print("Numbers:", numbers)
    print("Total Distance:", total_distance)
    print("Similarity Score:", similarity_score)

except FileNotFoundError as e:
    print(f"Error: File not found. {e}")