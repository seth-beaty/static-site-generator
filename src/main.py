from nodedelimiter import split_nodes_delimiter
from textnode import TextNode, TextType


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


if __name__ =="__main__":
    main()