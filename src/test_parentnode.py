from unittest import TestCase
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(TestCase):
    def test_parent_node_validation(self):
        # Test missing children
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()
        
        # Test empty children list
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

        # Test missing tag
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "text")]).to_html()

    def test_parent_node_leaf_nodes(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],)
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected)

    def test_parent_node_with_other_parent_nodes(self):

        inner_parent = ParentNode(
            "div",
            [
                LeafNode("span", "Hello"),
                LeafNode("span", "World")
            ]
        )

        node = ParentNode(
                "p",
                [
                    inner_parent,
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],)
        
        expected = '<p><div><span>Hello</span><span>World</span></div>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected)

    def test_nested_nodes_with_props(self):
        inner_parent = ParentNode(
            "div",
            [
                LeafNode("span", "Hello"),
                LeafNode("span", "World")
            ],
            {"class": "inner", "id": "inner-div"}
        )

        node = ParentNode(
            "p",
            [
                inner_parent,
                LeafNode("b", "Bold", {"class": "bold-text"}),
                LeafNode(None, "Normal text")
            ],
            {"class": "outer", "data-test": "test"}
        )
        
        expected = '<p class="outer" data-test="test"><div class="inner" id="inner-div"><span>Hello</span><span>World</span></div><b class="bold-text">Bold</b>Normal text</p>'
        self.assertEqual(node.to_html(), expected)
        