import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://boot.dev"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev"')

    def test_multiple_props(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://boot.dev", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')

    def test_no_props(self):
        simple_node = HTMLNode(tag="p")
        self.assertEqual(simple_node.props_to_html(), '')