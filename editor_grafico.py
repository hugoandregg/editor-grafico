# !/usr/bin/python


class EditorGrafico():
    def __init__(self):
        self.matriz = []

    def criar(self, linhas, colunas):
        linhas, colunas = int(linhas), int(colunas)
        self.matriz = [["O" for x in range(colunas)] for y in range(linhas)]


def main():
    pass

if __name__ == '__main__':
    editor = EditorGrafico()
    main()
