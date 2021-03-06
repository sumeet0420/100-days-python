import pandas
student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
word = input()
phone_dict = { row.letter:row.code for (index, row) in student_data_frame.iterrows()}
print([phone_dict[letter] for letter in word.upper()])