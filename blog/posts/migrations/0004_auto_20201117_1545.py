# Generated by Django 3.1.3 on 2020-11-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20201116_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['title'], 'verbose_name': 'Hashtag', 'verbose_name_plural': 'Hashtags'},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('p', 'published'), ('u', 'unpublished')], default='p', max_length=190, verbose_name='Статус'),
        ),
    ]