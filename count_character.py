##Write a .py script to get the occurances of a character (irrespective case sensitivity) from a sentence and get the index of that character as well.
##For example the sentence is = "Python is a preferred programming language in today world of informations" and we need to get it for "p". Input should be provided by a variable.

##There are two ways that i defined here, one to take the input from the user and second is of fixed character

#1

##count = 0
##string = 'Python is a preferred programming language in today world of informations'
##in_value =input('which character you want to count: ')
##for i in string.lower():
##    if i == in_value.lower():
##        count = count + 1
##print(count)


#2

##count = 0
##string = 'Python is a preferred programming language in today world of informations'
##for i in string.lower():
##    if i == 'p':
##        count = count + 1
##print(count)


#3
string = 'Python is a preferred programming language in today world of informations'
print(string.lower().count('p'))
