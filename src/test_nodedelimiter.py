

from unittest import TestCase

from nodedelimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestNodeDelimiter(TestCase):

    def test_code_delimiter(self):
        node = TextNode("This is `code`.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("This is plain text.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]  # No split should occur
        self.assertEqual(result, expected)

    def test_missing_closing_delimiter(self):
        node = TextNode("This is `open.", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual( str(context.exception), "Missing closing delimiter for `")

    def test_only_delimiters(self):
        node = TextNode("****", TextType.TEXT)
        result = split_nodes_delimiter([node], '*', TextType.BOLD)
        expected = [node]
        self.assertEqual(result, expected)

    def test_mismatched_delimiters(self):
        input_node = TextNode("This is **bold*", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([input_node], '**', TextType.BOLD)
            print("Exception message:", str(context.exception))
            self.assertEqual(str(context.exception), 'Invalid Markdown: No content between delimiters')