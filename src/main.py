from nodedelimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from utils.extraction_utils import extract_markdown_images, extract_markdown_links


def main():
    # node = TextNode("****", TextType.TEXT)
    # result = split_nodes_delimiter([node], '*', TextType.BOLD)
    # expected = [node]
    # print(result)

    node = TextNode("**bold at beginning**", TextType.TEXT)
    result = split_nodes_delimiter([node], '**', TextType.BOLD)
    print(result)

    try:
        input_node = TextNode("This is **bold*", TextType.TEXT)
        split_nodes_delimiter([input_node], '**', TextType.BOLD)
    except ValueError as e:
        print("Exception raised:", str(e))

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]



if __name__ =="__main__":
    main()