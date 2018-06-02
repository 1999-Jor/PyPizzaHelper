

class Calculadora:

    def __init__(self, valor_total):
        self.valor_total = valor_total

    def definir_numero_personas(self, numero_persona):
        self.numero_persona = numero_persona

    def calcular_valor_por_persona(self):
        self.valor_por_persona = self.valor_total / self.numero_persona

    #def salida(self, cuota):
    #    return ("Valor por cada persona: %.2f" % self.valor_por_persona)


if __name__ == '__main__':
    valor_total = float(input("Valor de pizza: "))
    calculadora = Calculadora(valor_total)
    numero_persona = int(input("Numero personas: "))
    calculadora.definir_numero_personas(numero_persona)

    calculadora.calcular_valor_por_persona()

    # cuota = calculadora
    # print(salida(cuota))
    import pyttsx
    import num2words
    cuota_txt = num2words.num2words(calculadora.valor_por_persona, lang='es')
    engine = pyttsx.init()
    lista_voluntarios = [
        'CHRISTIAN O.',
        'JONATHAN',
        'ESTEFANO',
        'JAIRO',
        'ROMMEL',
        'DAVID',
        'EDISON',
        'CRISTIAN'
    ]
    from random import randrange
    vol1 = randrange(0, 10)
    vol2 = randrange(0, 10)

    engine.say("La cuota es ")
    engine.say(cuota_txt)
    engine.say("Y los voluntarios son")
    engine.say(lista_voluntarios[vol1])
    engine.say(lista_voluntarios[vol2])
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 30)

    print(cuota_txt)

    engine.runAndWait()
