#created a pyramid and user will provide the number of rows to form that

row = int(input('Enter no of row: '))
for x in range(1,(row * 2),2):
    print(('*'*x).center(row*3),'\n')

#fixed range of triangle
#right justify

##for x in range(1,30,2):
##    print(('*'*x).rjust(40),'\n')

#left justify
##for x in range(1,30,2):
##    print(('*'*x).ljust(40),'\n')

#reverse pyramid
##for x in range(27,0,-2):
##    print(('*'*x).center(40))
