# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 14:08


from django.db import migrations, models
import tbx.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0020_auto_20160317_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='author_left',
            field=models.CharField(blank=True, help_text='author who has left Torchbox', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='streamfield',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', tbx.core.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())))), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_video_id',
            field=models.IntegerField(blank=True, help_text='Optional. The numeric ID of a Vimeo video to replace the background image.', null=True),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='servicespagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='servicespagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='streamfield',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', tbx.core.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())))), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')))),
        ),
        migrations.AlterField(
            model_name='standardpageclients',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpageclients',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link'),
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(help_text='Link title', max_length=255),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='streamfield',
            field=wagtail.core.fields.StreamField((('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', tbx.core.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))), label='Aligned image')), ('bustout', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())))), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())))), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')))),
        ),
    ]
