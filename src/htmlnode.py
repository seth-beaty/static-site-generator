class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag, self.value, self.children, self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        final_str = ""

        if self.props is not None:
            for prop, value in self.props.items():
                final_str += f' {prop}="{value}"'
        return final_str