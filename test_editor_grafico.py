# !/usr/bin/python
# -*- coding: utf8 -*-
import unittest
import os
from editor_grafico import *


class TestEditorGrafico(unittest.TestCase):
    def setUp(self):
        self.editor = EditorGrafico()

    '''
    I M N
    Cria uma nova matriz MxN. Todos os pixels são brancos (O).
    '''
    def test_criar(self):
        self.editor.criar(2, 2)
        self.assertEquals(self.editor.matriz, [["O", "O"], ["O", "O"]])

    def test_criar_com_index_diferentes(self):
        self.editor.criar(2, 3)
        self.assertEquals(self.editor.matriz,
                          [["O", "O", "O"], ["O", "O", "O"]])

    def test_criar_com_argumentos_invalidos(self):
        with self.assertRaises(ValueError):
            self.editor.criar("a", "b")

    def test_criar_matriz_index_negatixo(self):
        self.editor.criar(-1, -1)
        self.assertEquals(self.editor.matriz, [])

    def test_criar_matriz_index_negatixo(self):
        self.editor.criar(0, 0)
        self.assertEquals(self.editor.matriz, [])

    def test_criar_matriz_index_negativo_e_zero(self):
        self.editor.criar(0, -1)
        self.assertEquals(self.editor.matriz, [])

    '''
    L X Y C
    Colore um pixel de coordenadas (X,Y) na cor C.
    '''
    def teste_colorir(self):
        self.editor.criar(2, 2)
        self.editor.colorir(1, 2, "R")
        esperado = [
            ["O", "R"],
            ["O", "O"]
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_3x3(self):
        self.editor.criar(3, 3)
        self.editor.colorir(2, 3, "R")
        esperado = [
            ["O", "O", "O"],
            ["O", "O", "R"],
            ["O", "O", "O"]
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_com_numero(self):
        self.editor.criar(2, 2)
        self.editor.colorir(1, 2, 3)
        self.assertEquals(self.editor.matriz, [["O", "3"], ["O", "O"]])

    def teste_colorir_com_X_maior_que_matriz(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(3, 2, "R")

    def teste_colorir_com_Y_maior_que_matriz(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(1, 3, "R")

    def teste_colorir_com_X_igual_a_zero(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(0, 2, "R")

    def teste_colorir_com_X_menor_que_zero(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(-1, 2, "R")

    def teste_colorir_com_Y_igual_a_zero(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(2, 0, "R")

    def teste_colorir_com_Y_menor_que_matriz(self):
        self.editor.criar(2, 2)
        with self.assertRaises(IndexError):
            self.editor.colorir(1, -1, "R")

    '''
    V X Y1 Y2 C
    Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo
    inclusivo) na cor C.
    '''
    def teste_colorir_verticalmente(self):
        self.editor.criar(3, 3)
        self.editor.colorir_verticalmente(2, 1, 3, "R")
        esperado = [
            ['O', 'R', 'O'],
            ['O', 'R', 'O'],
            ['O', 'R', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_verticalmente_coluna_incompleta(self):
        self.editor.criar(3, 3)
        self.editor.colorir_verticalmente(2, 1, 2, "R")
        esperado = [
            ['O', 'R', 'O'],
            ['O', 'R', 'O'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_verticalmente_y1_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, 4, 3, "R")

    def teste_colorir_verticalmente_y1_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, -1, 3, "R")

    def teste_colorir_verticalmente_y2_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, 3, 4, "R")

    def teste_colorir_verticalmente_y2_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, 3, -1, "R")

    def teste_colorir_verticalmente_y2_menor_que_y1(self):
        self.editor.criar(3, 3)
        self.editor.colorir_verticalmente(2, 3, 1, "R")
        esperado = [
            ['O', 'R', 'O'],
            ['O', 'R', 'O'],
            ['O', 'R', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_verticalmente_y2_igual_a_y1(self):
        self.editor.criar(3, 3)
        self.editor.colorir_verticalmente(2, 3, 3, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'R', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_verticalmente_X_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(4, 2, 3, "R")

    def teste_colorir_verticalmente_X_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(-1, 4, 3, "R")

    def teste_colorir_verticalmente_y1_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, 0, 3, "R")

    def teste_colorir_verticalmente_y2_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(2, 3, 0, "R")

    def teste_colorir_verticalmente_X_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_verticalmente(0, 2, 3, "R")

    '''
    H X1 X2 Y C
    Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo
    inclusivo) na cor C.
    '''
    def teste_colorir_horizontalmente(self):
        self.editor.criar(3, 3)
        self.editor.colorir_horizontalmente(1, 3, 2, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['R', 'R', 'R'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_horizontalmente_coluna_incompleta(self):
        self.editor.criar(3, 3)
        self.editor.colorir_horizontalmente(1, 2, 2, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['R', 'R', 'O'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_horizontalmente_x1_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(4, 3, 2, "R")

    def teste_colorir_horizontalmente_x1_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(-1, 3, 2, "R")

    def teste_colorir_horizontalmente_x2_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(3, 4, 2, "R")

    def teste_colorir_horizontalmente_x2_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(3, -1, 2, "R")

    def teste_colorir_horizontalmente_x2_menor_que_y1(self):
        self.editor.criar(3, 3)
        self.editor.colorir_horizontalmente(3, 1, 2, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['R', 'R', 'R'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_horizontalmente_y2_igual_a_y1(self):
        self.editor.criar(3, 3)
        self.editor.colorir_horizontalmente(3, 3, 2, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['O', 'O', 'R'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_horizontalmente_Y_maior_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(2, 3, 4, "R")

    def teste_colorir_horizontalmente_Y_menor_que_matriz(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(3, 3, -1, "R")

    def teste_colorir_horizontalmente_x1_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(0, 3, 2, "R")

    def teste_colorir_horizontalmente_x2_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(3, 0, 2, "R")

    def teste_colorir_horizontalmente_Y_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_horizontalmente(2, 3, 0, "R")

    '''
    K X1 Y1 X2 Y2 C
    Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e
    (X2,Y2) o canto inferior direito.
    '''
    def teste_colorir_retangulo(self):
        self.editor.criar(3, 3)
        self.editor.colorir_retangulo(2, 2, 3, 3, "R")
        esperado = [
            ['O', 'O', 'O'],
            ['O', 'R', 'R'],
            ['O', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_retangulo_completo(self):
        self.editor.criar(3, 3)
        self.editor.colorir_retangulo(1, 1, 3, 3, "R")
        esperado = [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_retangulo_completo_5x5(self):
        self.editor.criar(5, 5)
        self.editor.colorir_retangulo(1, 1, 5, 5, "R")
        esperado = [
            ['R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_retangulo_Y_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_retangulo(1, 1, 3, 0, "R")

    def teste_colorir_retangulo_X_igual_a_zero(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_retangulo(1, 0, 3, 3, "R")

    def teste_colorir_retangulo_Y_negativo(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_retangulo(1, 1, 3, -2, "R")

    def teste_colorir_retangulo_X_negativo(self):
        self.editor.criar(3, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_retangulo(-2, 1, 3, 3, "R")

    '''
    F X Y C
    Preenche a região com a cor C. A região R é definida da seguinte forma:
    O pixel (X,Y) pertence à região. Outro pixel pertence à região, se e
    somente se, ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos
    um lado em comum com um pixel pertencente à região.
    '''
    def teste_colorir_regiao(self):
        self.editor.criar(3, 3)
        self.editor.colorir_regiao(3, 3, 'R')
        esperado = [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_regiao_com_linha_vertical(self):
        self.editor.criar(3, 3)
        self.editor.colorir_verticalmente(2, 1, 3, 'Q')
        self.editor.colorir_regiao(1, 1, 'R')
        esperado = [
            ['R', 'Q', 'O'],
            ['R', 'Q', 'O'],
            ['R', 'Q', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_regiao_com_linha_horizontal(self):
        self.editor.criar(3, 3)
        self.editor.colorir_horizontalmente(1, 3, 2, 'Q')
        self.editor.colorir_regiao(1, 1, 'R')
        esperado = [
            ['R', 'R', 'R'],
            ['Q', 'Q', 'Q'],
            ['O', 'O', 'O']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_regiao_com_linha_vertical_incompleta(self):
        self.editor.criar(3, 4)
        self.editor.colorir_verticalmente(3, 1, 2, 'Q')
        self.editor.colorir_regiao(1, 1, 'R')
        esperado = [
            ['R', 'R', 'Q', 'R'],
            ['R', 'R', 'Q', 'R'],
            ['R', 'R', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_regiao_com_linha_horizontal_incompleta(self):
        self.editor.criar(4, 3)
        self.editor.colorir_horizontalmente(2, 3, 3, 'Q')
        self.editor.colorir_regiao(1, 1, 'R')
        esperado = [
            ['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'Q', 'Q'],
            ['R', 'R', 'R']
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_colorir_regiao_com_X_invalido(self):
        self.editor.criar(4, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_regiao(0, 1, 'R')

    def teste_colorir_regiao_com_Y_invalido(self):
        self.editor.criar(4, 3)
        with self.assertRaises(IndexError):
            self.editor.colorir_regiao(1, -1, 'R')

    '''
    C
    Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam
    brancos (O).
    '''
    def teste_limpar(self):
        self.editor.criar(3, 3)
        self.editor.colorir(2, 3, 'R')
        self.editor.limpar()
        esperado = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        self.assertEquals(self.editor.matriz, esperado)

    def teste_limpar_sem_matriz_criada(self):
        self.editor.limpar()
        self.assertEquals(self.editor.matriz, [])

    '''
    S Name
    Escreve a imagem em um arquivo de nome Name.
    '''
    def teste_imprimir(self):
        self.editor.criar(2, 4)
        esperado = "O O O O\nO O O O"
        self.assertEquals(self.editor.imprimir(), esperado)

    def teste_imprimir_vazio(self):
        self.assertEquals(self.editor.imprimir(), "")

    def teste_salvar(self):
        self.editor.criar(2, 4)
        self.editor.salvar("one.bmp")
        esperado = "O O O O\nO O O O"
        resultado = open("one.bmp").read()
        try:
            self.assertEqual(resultado, esperado)
        finally:
            os.remove("one.bmp")

    def teste_salvar_sem_nome(self):
        self.editor.criar(1, 5)
        self.editor.salvar()
        esperado = "O O O O O"
        resultado = open("matriz.bmp").read()
        try:
            self.assertEqual(resultado, esperado)
        finally:
            os.remove("matriz.bmp")


if __name__ == '__main__':
    unittest.main()
