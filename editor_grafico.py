# !/usr/bin/python
# -*- coding: utf8 -*-


class EditorGrafico():
    def __init__(self):
        self.matriz = []

    def criar(self, linhas, colunas):
        linhas, colunas = int(linhas), int(colunas)
        self.matriz = [["O" for x in range(linhas)] for y in range(colunas)]

    def colorir(self, x, y, cor):
        x, y, cor = int(x)-1, int(y)-1, str(cor)
        if x < 0 or y < 0:
            raise IndexError
        self.matriz[y][x] = cor

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

    def colorir_regiao(self, x, y, cor):
        x, y, cor = int(x)-1, int(y)-1, str(cor)
        if x < 0 or y < 0:
            raise IndexError
        cor_aux = self.matriz[y][x]
        self.matriz[y][x] = cor
        if x+1 < (len(self.matriz[0])):
            if self.matriz[y][x+1] == cor_aux:
                self.colorir_regiao(x+2, y+1, cor)
        if x-1 >= 0:
            if self.matriz[y][x-1] == cor_aux:
                self.colorir_regiao(x, y+1, cor)
        if y+1 < (len(self.matriz)):
            if self.matriz[y+1][x] == cor_aux:
                self.colorir_regiao(x+1, y+2, cor)
        if y-1 >= 0:
            if self.matriz[y-1][x] == cor_aux:
                self.colorir_regiao(x+1, y, cor)

    def limpar(self):
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[0])):
                self.matriz[x][y] = "O"

    def imprimir(self):
        matriz_str = []
        for x in range(len(self.matriz)):
            matriz_str.append(''.join(self.matriz[x]))
        return '\n'.join(matriz_str)

    def salvar(self, nome="matriz.bmp"):
        with open(nome, 'w') as f:
            f.write(self.imprimir())


def main():
    comandos = '''
    Comandos:
    I M N
    Cria uma nova matriz MxN. Todos os pixels são brancos (O).

    C
    Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos
    (O).

    L X Y C
    Colore um pixel de coordenadas (X,Y) na cor C.

    V X Y1 Y2 C
    Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
    inclusivo) na cor C.

    H X1 X2 Y C
    Desenha um segmento horizontal na linha Y nas colunas de X1 a X2
    (intervalo inclusivo) na cor C.

    K X1 Y1 X2 Y2 C
    Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e
    (X2,Y2) o canto inferior direito.

    F X Y C
    Preenche a região com a cor C. A região R é definida da seguinte forma:
    O pixel (X,Y) pertence à região. Outro pixel pertence à região, se e
    somente se, ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um
    lado em comum com um pixel pertencente à região.

    S Name
    Escreve a imagem em um arquivo de nome Name.

    X
    Encerra o programa.
    '''
    print(comandos)
    editor = EditorGrafico()
    while True:
        entrada = raw_input()
        if entrada == 'X':
            break
        entrada = entrada.split(' ')
        try:
            if entrada[0] == 'I':
                editor.criar(entrada[1], entrada[2])
            elif entrada[0] == 'C':
                editor.limpar()
            elif entrada[0] == 'L':
                editor.colorir(entrada[1], entrada[2], entrada[3])
            elif entrada[0] == 'V':
                editor.colorir_verticalmente(entrada[1], entrada[2],
                                             entrada[3], entrada[4])
            elif entrada[0] == 'H':
                editor.colorir_horizontalmente(entrada[1], entrada[2],
                                               entrada[3], entrada[4])
            elif entrada[0] == 'K':
                editor.colorir_retangulo(entrada[1], entrada[2], entrada[3],
                                         entrada[4], entrada[5])
            elif entrada[0] == 'F':
                editor.colorir_regiao(entrada[1], entrada[2], entrada[3])
            elif entrada[0] == 'S':
                editor.salvar(entrada[1])
        except IndexError:
            print 'Digite corretamente o número de comandos da função desejada'

if __name__ == '__main__':
    main()
