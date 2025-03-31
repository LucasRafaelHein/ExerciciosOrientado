class Exercicios():

    def __init__(self):
        self.result_string = ""
        self.result_number = 0
        self.result_secundary_number = 0

    # Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas.
    def exercise_one(self, note_1, note_2, note_3):
        result = (note_1 + note_2 + note_3) / 3
        self.result_number = result
        return self.result_number
    
    #Faça um programa para converter um certo valor em dólar para reais (ver cotação do dia).
    def exercise_two(self, dolar):# Cotação do dolar: 5,74
        result = dolar * 5.74
        self.result_number = result
        return self.result_number
    
    # Faça um programa para converter um certo valor em reais para dólares (ver cotação do dia).
    def exercise_three(self, reais):
        result = reais * 0.17
        self.result_number = result
        return self.result_number

    # Faça um programa que leia um saldo e imprimir o saldo com reajuste de 1%.
    def exercise_four(self, saldo):
        result = saldo * 1.01
        self.result_number = result
        return self.result_number
    
    # Faça um programa que leia o valor de um produto e imprimir o valor corrigido com o reajuste de 33.33%.
    def exercise_five(self, valor):
        result = valor + (valor * 0.33)
        self.result_number = result
        return self.result_number
    
    # Faça programa que leia uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius e Kelvin.
    def exercise_six(self, fahrenheit):
        result = (5/9) * (fahrenheit - 32)
        result_two = (fahrenheit - 32) / 1.8 + 273.15
        self.result_number = result
        self.result_secundary_number = result_two
        return self.result_number, self.result_secundary_number
    
    # Faça programa que leia uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.
    def exercise_seven(self, celsius):
        result = celsius * 1.8 + 32
        result_two = celsius + 273.15
        self.result_number = result
        self.result_secundary_number = result_two
        return self.result_number, self.result_secundary_number
    
    def exercise_eight(self, kelvin):
        result = kelvin - 273.15
        result_two = (kelvin - 273.15) * 1.8 + 32
        self.result_number = result
        self.result_secundary_number = result_two
        return self.result_number, self.result_secundary_number
    
    def exercise_nine(self, salario, aumento):
        percentual = salario * aumento
        result = salario + percentual
        self.result_number = percentual
        self.result_secundary_number = result
        return self.result_number, self.result_secundary_number
    
    def exercise_ten(self, valor):
        return 'Você digitou um numero negativo' if valor < 0 else 'Você digitou um número positivo'
    
    def exercise_eleven(self, valor):
        if valor == 0:
            return "Você escreveu 0"
        elif valor > 1:
            return "Você escreveu um número positivo"
        else:
            return "Você escreveu um número negativo"
    
        

    


teste = Exercicios()
# 1
#print(teste.exercise_one(3, 4, 3))
# 2
#print(teste.exercise_two(1))
# 3
#print(teste.exercise_three(10))
# 4
#print(teste.exercise_four(100))
# 5
#print(teste.exercise_five(100))
# 6
#print(teste.exercise_six(15))
# 7
#print(teste.exercise_seven(15))
# 8
#print(teste.exercise_eight(15))
