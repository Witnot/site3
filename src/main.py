# hello world

# main.py
from textnode import TextNode, TextType

def main():
    # Create a dummy TextNode object
    node = TextNode(
        text="Hello, world!",
        text_type=TextType.BOLD,
        url=None
    )
    
    # Print the object
    print(node)

# Call the main function
if __name__ == "__main__":
    main()
