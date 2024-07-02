import random
import time

def generate_sequence(length):
    return [random.randint(0, 9) for _ in range(length)]

def display_sequence(sequence):
    for number in sequence:
        print(number, end=' ', flush=True)
        time.sleep(1)
    print("\r" + " " * len(sequence) * 2, end='\r')  # Clear the line

def get_user_input(length):
    user_input = input(f"Enter the {length}-digit sequence: ")
    return [int(digit) for digit in user_input]

def main():
    sequence_length = 3
    sequence = generate_sequence(sequence_length)
    display_sequence(sequence)
    user_sequence = get_user_input(sequence_length)
    if user_sequence == sequence:
        print("Correct!")
    else:
        print(f"Wrong! The correct sequence was {sequence}")

if __name__ == "__main__":
    main()