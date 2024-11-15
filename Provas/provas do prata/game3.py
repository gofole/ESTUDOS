for numero in range (0,int(input('DIgite o Numero que deseja parar'))):
    if (numero%3 == 0) and (numero%5 == 0) :
        print("FizzBuzz")
    elif numero%3 == 0 :
        print ("Fizz")
    elif numero%5 == 0 :
        print("Buzz")
    else :
        print (numero)