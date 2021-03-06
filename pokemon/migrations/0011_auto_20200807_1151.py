# Generated by Django 3.0.3 on 2020-08-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0010_auto_20200806_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='sprite_url',
            field=models.URLField(default='', help_text='the url of the sprite of the required type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='type',
            name='double_damage_from',
            field=models.ManyToManyField(blank=True, related_name='double_damage_from_set', to='pokemon.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='double_damage_to',
            field=models.ManyToManyField(blank=True, related_name='double_damage_to_set', to='pokemon.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='half_damage_from',
            field=models.ManyToManyField(blank=True, related_name='half_damage_from_set', to='pokemon.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='half_damage_to',
            field=models.ManyToManyField(blank=True, related_name='half_damage_to_set', to='pokemon.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='no_damage_from',
            field=models.ManyToManyField(blank=True, related_name='no_damage_from_set', to='pokemon.Type'),
        ),
        migrations.AlterField(
            model_name='type',
            name='no_damage_to',
            field=models.ManyToManyField(blank=True, related_name='no_damage_to_set', to='pokemon.Type'),
        ),
    ]
