import unittest
from zenode import ast
from zenode.lexer import Lexer, TokenStream
from zenode.parser import Parser


class ParserTest(unittest.TestCase):

    def _parse(self, s):
        return Parser().parse(TokenStream(Lexer().tokenize(s))).body

    def _assertNodesEq(self, s, nodes):
        return self.assertEqual(self._parse(s), nodes)

    def test_simple(self):
        self._assertNodesEq(
            '1',
            [ast.Number(1)]
        )
