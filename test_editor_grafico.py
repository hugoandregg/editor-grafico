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


if __name__ == '__main__':
    unittest.main()
