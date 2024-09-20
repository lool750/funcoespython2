from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n ----  MENU ----\n\n' +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair' +
              '\n1.Somar' +
              '\n2.Subtrair' +
              '\n3.Dividir' +
              '\n4.Multiplicar' +
              '\n5.Potência' +
              '\n6.Raiz' +
              '\n7.Tabuada'+
              '\n8.exercicio 1'+
              '\n9.exercicio 2'+
              '\n10.exercicio 3'+
              '\n11.Múltiplos de 5 a 50 são'+
              '\n12.Verificar se número é par ou impar'+
              '\n13.Verificar se número é positivo, negativo ou zero'+
              '\n14.Mostrar tabuada do numero escrito'+
              '\n15.Mostrar números do 1 até o número escrito'+
              '\n16.Mostrar a soma dos números de 1 até este número'+
              '\n17.Números primos de 1 a 20'+
              '\n18.Verificar se número é primo'+
              '\n19.Mostrar fatorial de um número'+
              '\n20.Sequência de fibonacci até o décimo termo'+
              '\n21.Mostrar se número é de fibonacci'+
              '\n22.Soma dos digitos do número digitado'+
              '\n23.Números pares e impares de 1 até o número digitado'+
              '\n24.Números primos de 1 até o número digitado'+
              '\n25.Sequência de Collatz até o número digitado'+
              '\n26.Soma dos números pares e impares de 1 até o número digitado'+
              '\n27.Verificar se número é perfeito'+
              '\n28.lista 2 exercicio 1'+
              '\n29.lista 2 exercicio 2'+
              '\n30.lista 2 exercicio 3'+
              '\n31.lista 2 exercicio 4'+
              '\n32.lista 2 exercicio 5'+
              '\n33.lista 2 exercicio 6'+
              '\n34.lista 2 exercicio 7'+
              '\n35.lista 2 exercicio 8'+
              '\n36.lista 2 exercicio 9'+
              '\n37.lista 2 exercicio 10'+
              '\n38.lista 2 exercicio 11'+
              '\n39.lista 2 exercicio 12'+
              '\n40.lista 2 exercicio 13'+
              '\n41.lista 2 exercicio 14'+
              '\n42.lista 2 exercicio 15'+
              '\n43.lista 2 exercicio 16'+
              '\n44.lista 2 exercicio 17'+
              '\n45.lista 2 exercicio 18'+
              '\n46.lista 2 exercicio 19'+
              '\n47.lista 2 exercicio 20')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 0:
                print('Obrigado!')
            if self.opcao == 1:
                self.coletar()#chamando o input por meio do coletar
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números é: {self.exer.multiplicar(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'\nO resultado da potência é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz de {self.num1} é: {self.exer.raiz(self.num1)}')
                print(f'\nA raiz de {self.num2} é: {self.exer.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.exer.tabuada(self.num2)}')
            elif self.opcao == 8:
                print(self.exer.exercicio1())
            elif self.opcao == 9:
                print(self.exer.exercicio2())
            elif self.opcao == 10:
                print(self.exer.exercicio3())
            elif self.opcao == 11:
                print(self.exer.exercicio4())
            elif self.opcao == 12:
                self.coletar()
                print(f'\nEste primeiro número é: {self.exer.exercicio5(self.num1)}')
                print(f'\nEste segundo número é: {self.exer.exercicio5(self.num2)}')
            elif self.opcao == 13:
                self.coletar()
                print(f'\nEste número é:{self.exer.exercicio6(self.num1)}')
                print(f'\nEste número é:{self.exer.exercicio6(self.num2)}')
            elif self.opcao == 14:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.exer.tabuada(self.num2)}')
            elif self.opcao == 15:
                self.num1 = int(input('Informe o número: '))#metodo coletar par 1 numero
                print(f'\nOs números de 1 a {self.num1} são: {self.exer.exercicio8(self.num1)}')
            elif self.opcao == 16:
                self.num1 = int(input('Informe o número: '))
                print(f'\nA soma dos números de 1 a {self.num1} é: {self.exer.exercicio9(self.num1)}')
            elif self.opcao == 17:
                print(self.exer.exercicio10())
            elif self.opcao == 18:
                self.num1 = int(input('Informe o número: '))
                print(self.exer.exercicio11(self.num1))
            elif self.opcao == 19:
                self.num1 = int(input('Informe o número: '))
                print(f'\nO fatorial de {self.num1} é: {self.exer.exercicio12(self.num1)}')
            elif self.opcao == 20:
                self.num1 = int(input('Informe o número: '))
                print(f'\nA sequência de fibonnacci até o {self.num1} é: {self.exer.exercicio13(self.num1)}')
            elif self.opcao == 21:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio14(self.num1)}')
            elif self.opcao == 23:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio16(self.num1)}')
            elif self.opcao == 24:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio17(self.num1)}')
            elif self.opcao == 26:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio19(self.num1)}')
            elif self.opcao == 27:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio20(self.num1)}')
            elif self.opcao == 28:
                print(self.exer.exercicio21())
            elif self.opcao == 29:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio22(self.num1)}')
            elif self.opcao == 30:
                self.num1 = int(input('Informe a base: '))
                self.num2 = int(input('Informe a altura: '))
                print(f'{self.exer.exercicio23(self.num1, self.num2)}')
            elif self.opcao == 31:
                self.num1 = int(input('Informe o número: '))
                print(f'{self.exer.exercicio24(self.num1)}')
            elif self.opcao == 32:
                self.num4 = int(input('Informe o número total de votos: '))
                self.num1 = int(input('Informe o número total de votos brancos: '))
                self.num2 = int(input('Informe o número total de votos nulos: '))
                self.num3 = int(input('Informe o número total de votos válidos: '))
                print(f'{self.exer.exercicio25(self.num4, self.num1, self.num2, self.num3)}')
            elif self.opcao == 33:
                self.num1 = int(input('Informe o salário dos funcionário: '))
                self.num2 = int(input('Informe o reajuste do salário do funcionário: '))
                print(f'{self.exer.exercicio26(self.num1, self.num2)}')
            elif self.opcao == 34:
                self.num1 = int(input('Informe o valor de fábrica: '))
                print(f'{self.exer.exercicio27(self.num1)}')
            elif self.opcao == 35:
                self.num1 = int(input('Informe a primeira nota: '))
                self.num2 = int(input('Informe a segunda nota:  '))
                self.num3 = int(input('Informe a terceira nota:  '))
                print(f'{self.exer.exercicio28(self.num1, self.num2, self.num3)}')
            elif self.opcao == 36:
                self.num1 = int(input('Informe a quantidade de maças compradas: '))
                print(f'{self.exer.exercicio29(self.num1)}')
            elif self.opcao == 37:
                self.num1 = int(input('Informe o primeiro número: '))
                self.num2 = int(input('Informe o segundo número: '))
                self.num3 = int(input('Informe o terceiro número: '))
                print(f'{self.exer.exercicio30(self.num1, self.num2, self.num3)}')
            elif self.opcao == 38:
                self.num1 = int(input('Informe o salário fixo: '))
                self.num2 = int(input('Informe o valor de vendas: '))
                print(f'{self.exer.exercicio31(self.num1, self.num2)}')
            elif self.opcao == 39:
                self.num1 = int(input('Informe o saldo: '))
                self.num2 = int(input('Informe o débito: '))
                self.num3 = int(input('Informe o crédito: '))
                print(f'{self.exer.exercicio32(self.num1, self.num2, self.num3)}')
            elif self.opcao == 40:
                self.num1 = int(input('Informe um número de 0 a 10: '))
                print(f'{self.exer.exercicio33(self.num1)}')
            elif self.opcao == 41:
                self.num1 = int(input('Informe um núemro positivo: '))
                print(f'{self.exer.exercicio34(self.num1)}')
            elif self.opcao == 42:
                print(self.exer.exercicio35(self.num1))
            elif self.opcao == 43:
                print(self.exer.exercicio36(self.num1))
            elif self.opcao == 44:
                print(self.exer.exercicio37())
            elif self.opcao == 45:
                print(self.exer.exercicio38(self.num1))






















        











