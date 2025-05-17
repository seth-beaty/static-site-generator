from unittest import TestCase

from src.leafnode import LeafNode
from src.textnode import TextNode, TextType
from src.utils.conversion_utils import text_node_to_html_node

class TestConversionUtils(TestCase):
    def test_simple_nodes(self):
        text_node = TextNode(text_type=TextType.TEXT, text="Hello world")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello world"

    def test_helper_functions(self):
        # Test a LINK node
        link_node = TextNode(
            text_type=TextType.LINK, 
            text="Click me", 
            url="https://example.com",
        )
        html_node = text_node_to_html_node(link_node)
        assert html_node.tag == "a"
        assert html_node.value == "Click me"
        assert html_node.props == {"href": "https://example.com"}

    def test_invalid_node(self):
        invalid_node = TextNode(text="Invalid node", text_type="UNSUPPORTED")
        try:
            text_node_to_html_node(invalid_node)
        except ValueError as e:
            assert str(e) == "Unsupported TextType: UNSUPPORTED"