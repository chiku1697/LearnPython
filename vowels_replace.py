##Solution: Where simple translatory translate all the vowels into '_'
##inputStr = "This is a fruit name Orange. You could enjoy it!"
##def translate(phrase):
##    vowels = "AEIOUaeiou"
##    translated = ''
##    for chars in phrase:
##        if (chars in vowels):
##            translated = translated + '_'
##        else: 
##            translated = translated + chars
##    print(translated)
##
##inputString = input('Enter the string to translate all vowels in underscore:- ')
##print(translate(inputString))

var = input('Enter a string: ')
vowels = "AEIOUaeiou"
for x in var:
    if x in vowels:
        print('_',end='')
    else:
        print(x,end='')

