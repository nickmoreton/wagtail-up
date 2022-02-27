# Generated by Django 4.0.2 on 2022-02-27 17:36

import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="StandardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.StreamField(
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
                            (
                                "text",
                                wagtail.core.blocks.RichTextBlock(
                                    features=["bold", "italic", "link"], icon="doc-full"
                                ),
                            ),
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
                            ),
                            (
                                "gallery",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(
                                                required=False
                                            ),
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
                        ],
                        blank=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]