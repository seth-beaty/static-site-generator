import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_not_equal(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertNotEqual(node.to_html(), 'This is a paragraph of text.</p>')

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_props_not_equal(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(node.to_html(), '< href="https://www.google.com">Click me!</a>')