class Coordena:


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro_valor):
        x_dif = (self.x - otro_valor.x)**2 
        y_dif = (self.y - otro_valor.y)**2
        return (x_dif + y_dif)**0.5


if __name__ == '__main__':
    cordenada_1 = Coordena(3, 30)
    cordenada_2 = Coordena(4,8)
    # print(cordenada_1.distancia(cordenada_2))
    print(isinstance(1, Coordena))