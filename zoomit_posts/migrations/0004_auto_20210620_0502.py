# Generated by Django 3.2.4 on 2021-06-20 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoomit_categories', '0003_rename_url_category_slug'),
        ('zoomit_tags', '0001_initial'),
        ('zoomit_posts', '0003_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='zoomit_categories.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='zoomit_tags.Tag'),
        ),
    ]