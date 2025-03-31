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
    
    def exercise_twelve(self, note_1, note_2, note_3):
        result = (note_1 + note_2 + note_3) / 3
        if result >= 7:
            self.result_string = "APROVADO"
        elif result >= 5 and result < 7:
            self.result_string = "RECUPERAÇÃO"
        else:
            self.result_string = "REPROVADO"
        
        self.result_number = result
        return self.result_number, self.result_string
    
    def exercise_thirteen(self, valor):
        if valor % 2 == 0:
            return "Par"
        else:
            return "Ímpar"
    
    def exercise_fourteen(self, number_1, number_2, number_3):
        if number_1 >= number_2 and number_1 >= number_3:
            self.result_number = number_1
        elif number_2 >= number_1 and number_2 >= number_3:
            self.result_number = number_2
        else:
            self.result_number = number_3
        
        return self.result_number

    def exercise_fifteen(self, idade):
        if idade >= 65:
            return "Idoso"
        elif idade >= 21:
            return "Adulto"
        elif idade >= 14:
            return "Juvenil"
        elif idade >= 9:
            return "Infantil"
        else:
            return "Mirim"
        
    def exercise_sixteen(self, number_1, number_2):
        soma = number_1 + number_2
        if soma > 20:
            result = soma + 8
        else:
            result = soma - 5
        self.result_number = result
        return self.result_number
    
    def exercise_seventeen(self, value_buy):

        if value_buy < 20.00:
            result = 0.45
        else:
            result = 0.30

        value_sale = value_buy * (1 + result)
        self.result_number = value_sale
        return self.result_number
    
    #Fim, não vai ter Bônus. 
    
teste = Exercicios()
print(teste.exercise_seventeen(100))
