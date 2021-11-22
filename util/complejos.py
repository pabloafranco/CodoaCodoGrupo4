class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def sumar(complejo1, complejo2):
        real =  complejo1.real + complejo2.real
        imaginario = complejo1.imaginario + complejo2.imaginario

        return (real, imaginario)

    def restar(complejo1, complejo2):
        real =  complejo1.real - complejo2.real
        imaginario = complejo1.imaginario - complejo2.imaginario

        return (real, imaginario)

    def multiplicar(complejo1, complejo2):
        """(a+bi)(c+di) = ac+adi+bci+bdi2  donde i2= -1
 
                                  = ac+(ad+bc)i -bd
                                 = ac-bd+(ad+bc)i
        """
        unoR = complejo1.real * complejo2.real
        dosI = complejo1.real * complejo2.imaginario
        tresI = complejo1.imaginario * complejo2.real
        cuatroR = complejo1.imaginario * complejo2.imaginario * -1
        real = unoR+cuatroR
        imaginario = dosI+tresI
        return (real, imaginario)