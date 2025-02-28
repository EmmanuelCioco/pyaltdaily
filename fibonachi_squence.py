user_start_number=int(input("input the first number in the sequence:  "))
user_second_number=int(input("input the second number in the sequence:  "))
length_of_sequence=int(input("input the length of the sequence:  "))
sequence_numbers=[user_start_number,user_start_number]
for i in range(length_of_sequence):
    next_number=sequence_numbers[-1]+sequence_numbers[-2]
    sequence_numbers=sequence_numbers.append(next_number)
print(sequence_numbers)