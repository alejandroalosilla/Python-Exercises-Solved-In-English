#  Ex053 - Create a program that reads any sentence and says if it is a
# palindrome, disregarding the spaces.
#  Examples of palindromes: Murder for a jar of red rum
# Never odd or even.

sentence = str(input('Enter a sentence: ')).upper().strip().replace(' ', '')
reverse_sentence = ''

for c in range(len(sentence) - 1, -1, -1):
    reverse_sentence += sentence[c]
print(f'The inverse of {sentence} is {reverse_sentence}')

if sentence != reverse_sentence:
    print('The sentence you entered is not a palindrome.')
else:
    print('The sentence entered is a palindrome.')
