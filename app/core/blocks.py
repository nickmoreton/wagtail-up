from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(StructBlock):
    heading_text = CharBlock(required=True, help_text="Heading text")
    heading_level = ChoiceBlock(
        choices=[
            ("h1", "Heading 1"),
            ("h2", "Heading 2"),
            ("h3", "Heading 3"),
            ("h4", "Heading 4"),
            ("h5", "Heading 5"),
            ("h6", "Heading 6"),
        ],
        required=True,
        help_text="Heading level",
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        text_classes = [
            "text-xxl",
            "text-xl",
            "text-lg",
            "text-md",
            "text-sm",
            "text-xs",
        ]
        context["text_class"] = text_classes[int(value["heading_level"][1]) - 1]
        return context


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class GalleryBlock(StructBlock):
    title = CharBlock(required=False)
    images = StreamBlock(
        [
            ("image", ImageBlock()),
        ],
    )

    class Meta:
        icon = "image"
        template = "blocks/gallery_block.html"


class CoreBlocks(StreamBlock):
    heading = HeadingBlock()
    text = RichTextBlock(icon="doc-full")
    image = ImageBlock()
    gallery = GalleryBlock()
