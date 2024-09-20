import math
from lib2to3.fixer_util import find_binding


class Operacao:
    def __init__(self):#construtor
        self.num1 = 0 #self serve para falar que aquela variavel pertence a aquela classe
        self.num2 = 0

    def coletar(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self,num1, num2):#um número dentro de parênteses é chamado de parâmetro
        self.coletar(num1, num2)#utilizando o método coletar
        return self.num1 + self.num2

    def subtrair(self,num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self,num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self,num1, num2):
        self.coletar(self.num1, self.num2)
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self,num1):
        resultado= ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self,num):
        return math.sqrt(num)

    def exercicio1(self):
        num = ""
        for i in range (1,11,1):
            num += f'\n{i}'
        return num

    def exercicio2(self):
        num=""
        for i in range (1,21,1):
            if i % 2 == 0:
                num += f'\n{i}'
        return num

    def exercicio3(self):
        soma=0
        for i in range (1, 101):
            soma += i
        return soma

    def exercicio4(self):
        num=""
        for i in range(1,51,1):
            if i % 5 == 0:
                num += f'\n{i}'
        return num

    def exercicio5(self,num):
        if num % 2 == 0:
            return 'par'
        else:
            return 'ìmpar'

    def exercicio6(self,num):
        if num == 0:
            return 'O zero'
        elif num > 0:
            return 'Positivo'
        else:
            return 'Negativo'

    def exercicio7(self, num):
        resultado = ""
        for i in range (1,11,1):
            resutado = f'\n{num} * {i} = {num * i}'
        return resultado

    def exercicio8(self, num):
        resultado = ""
        for i in range (1,num,1):
            resultado += f'\n{i}'
        return resultado

    def exercicio9(self, num):
        soma = 0
        for i in range (1,num,1):
            soma += i
        return soma

    def exercicio10(self):
        primo ='\n1 \n2 \n3 \n5'
        for i in range(5,21,1):
            if i % 2 != 0 and  i % 3 != 0  and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num):
        if num == 2 or  num == 3 or  num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and  num % 3 != 0 and  num % 5 != 0:
            return f'O {num} é primo!'
        return f'O {num} não é primo'

    def exercicio12(self, num):
        soma = 1
        for i in range(1, num, 1):
            soma += soma * i
        return soma

    def exercicio13(self, num):
        fib = 0
        fib1 = 1
        fib2 = 0
        resultado = f'\n{fib}\n{fib1}'
        for i in range(1,num,1):
            fib2 = fib + fib1
            resultado += f'\n{fib2}'
            fib = fib1
            fib1 = fib2
        return resultado

    def exercicio14(self, num):
        fib = 0
        fib1 = 1
        fib2 = 0
        resposta = ""
        resultado = f'\n{fib}\n{fib1}'
        for i in range(1, num, 1):
            fib2 = fib + fib1
            resultado += f'\n{fib2}'
            fib = fib1
            fib1 = fib2
        if num == resultado:
             resultado = f'O {num} faz parte da sequência de fibonacci'
        else:
            resultado = f'O {num} não faz parte da sequência de fibonacci' # ta errado
        return resultado

    #def exercicio15(self):


    def exercicio16(self, num):
       resultado = ""
       for i in range(1,num,1):
           if i % 2 == 0:
               resultado += f'\n{i} par'
           else:
               resultado += f'\n{i} impar'
       return resultado

    def exercicio17(self, num):
        primo = ""
        for i in range(1, num, 1):
            if i == 2 or i == 3 or i == 5:
                 primo += f'\n{i}'
            elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    #def exercicio18(self):

    def exercicio19(self, num):
        somapar = 0
        somaimpar = 0
        for i in range (1,num + 1, 1):
            if i % 2 == 0:
                somapar += i
            else:
                somaimpar += i
        return f'a soma dos pares é {somapar} e a dos ímpares é {somaimpar}.'

    def exercicio20(self, num):
        soma = 0
        resultado = ""
        for i in range (1,num + 1,1):
            if num % i == 0:
                soma += i
            elif soma == num:
               resultado = f'O {num} é um número perfeito'
            else:
                resultado = f'O {num} não é um número perfeito'
        return resultado

    #lista de exercicios 2

    def exercicio21(self):
        a = 10
        b = 20

        a = b
        b = a
        return f'A-{a} B-{b - 10}'

    def exercicio22(self, num):
        resultado = ''

        resultado = num - 1

        return f' o atencessor de {num} é {resultado}'

    def exercicio23(self, num1, num2):
        base = num1
        altura = num2
        resultado = ''

        resultado = base * altura

        return f' A área do retângulo é: {resultado}'

    def exercicio24(self, num):
        idade = num

        meses = idade * 12
        dias = idade * 365

        return f'A sua idade expressa em anos é {idade} anos, expressa em meses é {meses} meses e expressa em dias é {dias} dias.'

    def exercicio25(self, num1, num2, num3, num4):
        votobranco = num1
        votonulo = num2
        votoval = num3
        totalvoto = num4

        res1 = (votobranco/totalvoto) * 100
        res2 = (votonulo/totalvoto) * 100
        res3 = (votoval/totalvoto) * 100

        return f'O total de votos é {num4} O percentual de votos brancos é {res1}%, o percentual de votos nulos é {res2}%  e o percentual de válidos é {res3}%'

    def exercicio26(self,num ,num2):
        sal = num
        reaj = num2
        res = sal * reaj / 100 + sal

        return f' O novo salário do funcionário é: {res}'

    def exercicio27(self,  num):
        valfab = num
        pd = valfab * 0.28
        i = valfab * 0.45
        vt = valfab + pd + i
        return f' O custo final ao consumidor é: {vt}'

    def exercicio28(self, num, num1, num2):
        media = (num + num1 +num2) / 3
        return f'A média do aluno é R${media}'

    def exercicio29(self, num):
        if num < 6:
            res = num * 1.30
        else:
            res = num * 1.00
        return f' O valor das maças é : {res}'

    def exercicio30(self, num, num1, num2):
        res =""
        if num > num1 and num > num2 and num1 > num2:
            res = f'{num} \n{num1}\n{num2}'
        elif num1 > num and num1 > num2 and num > num2:
            res = f'{num1}\n{num}\n{num2}'
        elif num2 > num and num2 > num1 and num1 > num:
            res = f'{num2}\n{num1}\n{num}'
        elif num2 > num and num2 > num1 and num > num1:
            res = f'{num2}\n{num}\n{num1}'
        elif num > num1 and num > num2 and num2 > num1:
            res = f'{num}\n{num2}\n{num1}'
        else:
            res = f'{num1}\n{num2}\n{num}'
        return f'{res}'

    def exercicio31(self,num,num2):
        sf = num
        vv = num2
        res = ''
        if vv == 1500:
            res = sf+1500  * 0.03/100
        elif vv > 1500:
            res = sf+1500 * 0.03/100
        else:
            res = sf
        return f'O salário do vendedor é {res}'

    def exercicio32(self, num, num2, num3):
        saldo = num - num2 + num3
        res =''
        if saldo >= 1:
            res = f'O saldo final de R${saldo} é positivo'
        else:
            res = f'O saldo final de R${saldo} é negativo'
        return f'{res}'

    def exercicio33(self,num):
        res = ''
        for i in range(1,11, 1):
            if num >= 1 and num <= 10:
                res += f'\n{num} * {i} = {num * i}'
            else:
                res = f'{num} escreva um número de 1 a 10'
                return f'{res}'
        return f'{res}'

    def exercicio34(self, num):
        res = ''
        for i in range(1,num + 1,1):
            if num >= 1:
                res += f'\n{i}'
            else:
                res = f'escreva um valor positivo'
                return f'{res}'
        return f'{res}'

    def exercicio35(self, num):
        negativo = 0
        for i in range(1, 11, 1):
            num = int(input("escreva um numero:"))
            if num <= 0:
                negativo += 1
        return f' a quantidade de números negativos é: {negativo}'

    def exercicio36(self, num):
        soma = 0
        for i in range (1, 11, 1):
            num =int(input('Escreva um número: '))
            if num < 40:
                soma += num
        return f'A soma dos números inferiores a 40 é: {soma}'

    def exercicio37(self):
        resultado = 0
        for i in range (15,101,1):
            resultado += i
        return f'{resultado/85}'

    #def exercicio38(self, num):
     #   media = 0
      #  maior = 0
       # res =''
        #for i in range(1,num, 1):
         #   num = int(input('informe o  número: '))
          #  quantidade = i
           # media += i
            #if num > num :
             #   maior = num
            #res = media/quantidade
        #return f'A quantidade de números é: {quantidade} O maior número é {maior} e a media desses números é{res}'

    # não fiz 14 , 15, 18 da lista 1 e 18, 19, 20 da lista 2.
































