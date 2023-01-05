#  Ex026 - Make a program that reads a sentence from the keyboard and shows
#  how many times the letter "A" appears, in which position it
#  appears the first time and in which position it appears the last
#  time.

sentence = str(input('Enter a sentence: ')).strip().upper()

print(f'The letter "A" appears {sentence.count("A")} times in the sentence.')
print(f'The first letter A appeared at position {sentence.find("A") + 1}.')
print(f'The last letter A appeared in position {sentence.rfind("A") + 1}.')
