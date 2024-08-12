import random
from collections import Counter

# 과거 당첨 번호 데이터 예시
past_winning_numbers = [
    [5, 10, 11, 17, 28, 34],
    [1, 5, 8, 16, 28, 33],
    [10, 15, 24, 30, 31, 37],
    [1, 2, 6, 14, 27, 38],
    [15, 19, 21, 25, 27, 28],
    [4, 5, 9, 11, 37, 40],
    [6, 14, 25, 33, 40, 44],
    [3, 8, 17, 30, 33, 34],
    [13, 19, 21, 24, 34, 35],
    [3, 6, 21, 30, 34, 35],
    [2, 19, 26, 31, 38, 41],
    [1, 9, 12, 13, 20, 45],
    [6, 7, 19, 28, 34, 41 ],
    # 추가적인 데이터...
]

def calculate_frequencies(past_numbers):
    flat_numbers = [num for sublist in past_numbers for num in sublist]
    return Counter(flat_numbers)

def weighted_random_choice(frequencies):
    total = sum(frequencies.values())
    rand = random.uniform(0, total)
    upto = 0
    for number, freq in frequencies.items():
        if upto + freq >= rand:
            return number
        upto += freq
    return list(frequencies.keys())[0]

def generate_weighted_lotto_numbers(frequencies, count=6):
    selected_numbers = set()
    while len(selected_numbers) < count:
        selected_numbers.add(weighted_random_choice(frequencies))
    return sorted(selected_numbers)

if __name__ == "__main__":
    print("Starting the program...")
    frequencies = calculate_frequencies(past_winning_numbers)
    print("Frequencies:", frequencies)

    num_sets = 5  # 생성할 세트의 개수
    sets = []
    for i in range(num_sets):
        weighted_numbers = generate_weighted_lotto_numbers(frequencies)
        sets.append(weighted_numbers)
        print(f"Generated Lotto Numbers (Weighted) - Set {i + 1}: {weighted_numbers}")

    print("Program finished.")

    # 결과를 파일에 저장
    with open("generated_lotto_sets.txt", "w") as file:
        for i, lotto_set in enumerate(sets):
            file.write(f"Set {i + 1}: {lotto_set}\n")
    print("Results saved to generated_lotto_sets.txt")
