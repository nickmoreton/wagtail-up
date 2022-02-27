from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from app.core.blocks import CoreBlocks


class StandardPage(Page):
    body = StreamField(CoreBlocks(), blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]


@register_setting
class NavigationSettings(BaseSetting):
    menu_items = StreamField(
        [
            ("menu_item", PageChooserBlock()),
        ],
        blank=True,
        verbose_name="Menu items",
        help_text="Add menu items to the navigation menu",
    )
