def calculoVogais(texto):

 count_vowels = 0

 for letra in texto:
  if letra in ['a','e','i','o','u']:
      count_vowels += 1

 print('Number of vowels in text is: ' + str(calculoVogais))

pessoaEscreveu = input('Type here: ')
calculoVogais(pessoaEscreveu)
