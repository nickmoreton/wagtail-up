# Generated by Django 4.0.2 on 2022-02-28 22:26

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_add_call_to_action_block"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standardpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "heading",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "heading_text",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Heading text", required=True
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("h1", "Heading 1"),
                                            ("h2", "Heading 2"),
                                            ("h3", "Heading 3"),
                                            ("h4", "Heading 4"),
                                            ("h5", "Heading 5"),
                                            ("h6", "Heading 6"),
                                        ],
                                        help_text="Heading level",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ("text", wagtail.core.blocks.RichTextBlock(icon="doc-full")),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "gallery",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "images",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "image",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                        (
                                                            "caption",
                                                            wagtail.core.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            )
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "call_to_action",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "button_text",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "button_link",
                                    wagtail.core.blocks.URLBlock(required=False),
                                ),
                                ("page_link", wagtail.core.blocks.PageChooserBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
