sentence = input()
sentence_number = 0
even_alphabet, odd_alphabet = set(sentence), set()
while sentence:
    if sentence_number % 2 == 0:
        even_alphabet.update(sentence)
    else:
        odd_alphabet.update(sentence)
    sentence = input()
    sentence_number += 1

inter = even_alphabet.intersection(odd_alphabet)
if len(even_alphabet.difference(inter)) > \
   len(odd_alphabet.difference(inter)):
    print('Mumbo')
else:
    print('Jumbo')
