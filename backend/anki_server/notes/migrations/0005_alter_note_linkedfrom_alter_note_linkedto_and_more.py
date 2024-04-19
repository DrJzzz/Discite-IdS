# Generated by Django 5.0.3 on 2024-04-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_note_linkedfrom_alter_note_linkedto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='linkedFrom',
            field=models.ManyToManyField(blank=True, to='notes.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='linkedTo',
            field=models.ManyToManyField(blank=True, to='notes.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, to='notes.tag'),
        ),
    ]
