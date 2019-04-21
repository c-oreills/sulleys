# Generated by Django 2.1.8 on 2019-04-21 15:57

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('buildings', '0002_building_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
