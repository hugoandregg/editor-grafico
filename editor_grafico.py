# !/usr/bin/python


class EditorGrafico():
    def __init__(self):
        self.matriz = []

    def criar(self, linhas, colunas):
        linhas, colunas = int(linhas), int(colunas)
        self.matriz = [["O" for x in range(colunas)] for y in range(linhas)]

    def colorir(self, x, y, cor):
        x, y, cor = int(x)-1, int(y)-1, str(cor)
        if x < 0 or y < 0:
            raise IndexError
        self.matriz[x][y] = cor

    def colorir_verticalmente(self, x, y1, y2, cor):
        x, y1, y2, cor = int(x)-1, int(y1), int(y2), str(cor)
        if x < 0 or y1 <= 0 or y2 <= 0:
            raise IndexError
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1-1, y2):
            self.matriz[y][x] = cor

    def colorir_horizontalmente(self, x1, x2, y, cor):
        x1, x2, y, cor = int(x1), int(x2), int(y)-1, str(cor)
        if x1 <= 0 or x2 <= 0 or y < 0:
            raise IndexError
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1-1, x2):
            self.matriz[y][x] = cor

    def colorir_retangulo(self, x1, y1, x2, y2, cor):
        x1, y1, x2, y2, cor = int(x1), int(y1), int(x2), int(y2), str(cor)
        if y2 <= 0:
            raise IndexError
        for y in range(y1, y2+1):
            self.colorir_horizontalmente(x1, x2, y, cor)


def main():
    pass

if __name__ == '__main__':
    editor = EditorGrafico()
    main()
