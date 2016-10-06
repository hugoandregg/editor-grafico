# !/usr/bin/python
# -*- coding: utf8 -*-
import unittest
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
            self.editor.colorir_verticalmente(-1, 2, 3, "R")

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


if __name__ == '__main__':
    unittest.main()
