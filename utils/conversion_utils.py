
from src.leafnode import LeafNode
from src.textnode import TextNode, TextType


HANDLERS = {
    TextType.LINK: lambda node: link_helper(node),  # Complex case handed off to a helper function
    TextType.TEXT: lambda node: LeafNode(tag=None, value=node.text),  # Simple inline logic
    TextType.BOLD: lambda node: LeafNode(tag="b", value=node.text),
    TextType.ITALIC: lambda node: LeafNode(tag="i", value=node.text),
    TextType.CODE: lambda node: LeafNode(tag="code", value=node.text),
    TextType.IMAGE: lambda node: img_helper(node),
}


def text_node_to_html_node(text_node):

    handler = HANDLERS.get(text_node.text_type)
    if not handler:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")
    return handler(text_node)


def link_helper(text_node):
    if not text_node.url:
        raise ValueError("LINK must have a valid url.")
    
    href = text_node.url
    anchor_text = text_node.text
    return LeafNode(tag="a", value=anchor_text, props= {"href": href})

def img_helper(text_node):
    if 'src' not in text_node.props or 'alt' not in text_node.props:
        raise ValueError("IMG must have 'img' and 'src' and 'alt' in its props.")
    
    src_text = text_node.props['src']
    alt_text = text_node.props['alt']
    return LeafNode(tag="img", value="", props={"src": src_text, "alt": alt_text})


    