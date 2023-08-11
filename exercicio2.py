x=float(input('qual medida do lado x do triangulo?'))
y=float(input('Qual a medida do lado y do triangulo?'))
z=float(input('Qual a medida do lado z do triangulo ?'))
if(x<=0) or (y<=0) or (z<=0):
    print('nao existe triangulo com numero 0')
elif(x==y) and (y==z):
    print('seu triangulo é EQUILÁTERO')
elif(x==y) or (x==z) or (y==z):
    print('triangulo é isoceles')
else:
    print('triangulo escaleno')

