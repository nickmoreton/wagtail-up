from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from app.core.blocks import CoreBlocks


class StandardPage(Page):
    body = StreamField(CoreBlocks(), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
