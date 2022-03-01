from django.forms.utils import ErrorList
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)
from wagtail.core.blocks.struct_block import StructBlockValidationError
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


class CallToActionBlock(StructBlock):
    title = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    button_text = CharBlock(required=False)
    button_link = URLBlock(required=False)
    page_link = PageChooserBlock(required=False)

    class Meta:
        icon = "plus"
        template = "blocks/call_to_action_block.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context["button_url"] = value["button_link"] or value["page_link"]
        context["button_title"] = value["button_text"] or value["page_link"].title
        return context

    def clean(self, value):
        errors = {}
        values = [value["button_link"], value["page_link"]]

        # Check if at least button_link or page_link are set but not both
        if sum(value is not None and value != "" for value in values) != 1:
            message = "You must specify either a page or a link"
            errors["page_link"] = ErrorList([message])
            errors["button_link"] = ErrorList([message])

        # Check if button_link is set a title is inclued
        if value["button_link"] and not value["button_text"]:
            message = "You must specify the button text"
            errors["button_text"] = ErrorList([message])

        # If errors are found, raise a ValidationError
        if errors:
            raise StructBlockValidationError(errors)

        return super().clean(value)


class CoreBlocks(StreamBlock):
    heading = HeadingBlock()
    text = RichTextBlock(icon="doc-full")
    image = ImageBlock()
    gallery = GalleryBlock()
    call_to_action = CallToActionBlock()
