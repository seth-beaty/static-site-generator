from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    print(old_nodes)
    
    for node in old_nodes:
        print(node)
        # Check to make sure input is valid
        segments = node.text.split(delimiter)

        if len(segments) % 2 == 0:
            raise ValueError("Invalid Markdown: Uneven delimiters in text.")
        
        if all(segment.strip() == "" for segment in segments):
            raise ValueError("Invalid Markdown: No content between delimiters")

        # Skip non-text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            start_pos = node.text.find(delimiter)
            if start_pos != -1:  # if we found a delimiter
                end_pos = check_delimiters(node.text, delimiter, start_pos + len(delimiter))
                
                # Get the three parts
                before_text = node.text[:start_pos]
                delimited_text = node.text[start_pos + len(delimiter):end_pos]
                after_text = node.text[end_pos + len(delimiter):]

                # Create and add the three nodes
                if before_text:
                    new_nodes.append(TextNode(before_text, TextType.TEXT))
                new_nodes.append(TextNode(delimited_text, text_type))
                if after_text:
                    new_nodes.append(TextNode(after_text, TextType.TEXT))

            else:
                new_nodes.append(node)

    return new_nodes
            
            
def check_delimiters(text, delimiter, start_pos):
    closing_pos = text.find(delimiter, start_pos)
    if closing_pos == -1:
        raise Exception(f"Missing closing delimiter '{delimiter}' starting from position {start_pos}")
    return closing_pos