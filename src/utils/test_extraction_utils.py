from unittest import TestCase

from src.utils.extraction_utils import *



class TestExtractionUtils(TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):

        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_links_equal(self):

        text = "This is text with a link [](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        # [("", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        matches = extract_markdown_links(text)
        self.assertListEqual([("", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)