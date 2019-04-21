# Generated by Django 2.1.8 on 2019-04-21 20:34

from django.db import migrations, models
import django.db.models.deletion
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_building_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='building',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='buildingimage',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_images', to='buildings.Building'),
        ),
    ]