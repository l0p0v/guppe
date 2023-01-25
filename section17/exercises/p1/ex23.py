class Televisor:
    numero_canais: int = 100
    volume_maximo: int = 100

    def __init__(self, ligado: bool, canal: int, volume: int) -> None:
        self.__ligado = ligado
        self.canal = canal
        self.volume = volume

    def ligar(self) -> None:
        self.__ligado = True

    def desligar(self) -> None:
        self.__ligado = False

    def imprimir(self) -> None:
        print(f'Televisor está ligado? {self.__ligado}')
        print(f'Televisor está no canal: {self.canal}/{Televisor.numero_canais}')
        print(f'Televisor está no volume: {self.volume}/{Televisor.volume_maximo}')


if __name__ == '__main__':
    tv = Televisor(False, 157, 69)
    tv.imprimir()
    tv.ligar()
    tv.imprimir()
