#  Ex077 - Create a program that has a tuple with several words.
#  After that, you must show, for each word, which are its vowels.

words = ('Learn', 'Program', 'Language', 'Python', 'Course', 'Free', 'Study', 'Practice',
         'Work', 'Marketplace', 'Programmer', 'Future')

for word in range(0, len(words)):
    print(f'\nIn the word {words[word].upper()} we have: ', end='')
    for c in range(0, len(words[word])):
        if words[word][c] in 'aeiou':
            print(f'{words[word][c]}', end=' ')
