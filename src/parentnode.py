

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if not self.tag:
            raise ValueError("No tag in node")
        
        if not self.children:
            raise ValueError("Children missing from node")
        
        inner_str = ""
        for child in self.children:
            inner_str += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{inner_str}</{self.tag}>'