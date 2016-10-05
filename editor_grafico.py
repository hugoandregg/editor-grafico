# !/usr/bin/python


class EditorGrafico():
    def __init__(self):
        self.matriz = []

    def criar(self, linhas, colunas):
        linhas, colunas = int(linhas), int(colunas)
        self.matriz = [["O" for x in range(colunas)] for y in range(linhas)]

    def colorir(self, x, y, cor):
        x, y, cor = int(x)-1, int(y)-1, str(cor)
        if x >= 0 and y >= 0:
            self.matriz[x][y] = cor


def main():
    pass

if __name__ == '__main__':
    editor = EditorGrafico()
    main()
