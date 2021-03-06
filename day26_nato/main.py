import pandas
student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
word = input()
#Loop through rows of a data frame
phone_dict = { row.letter:row.code for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print([phone_dict[letter] for letter in word.upper()])
