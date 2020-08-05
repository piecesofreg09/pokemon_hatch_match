# Generated by Django 3.0.7 on 2020-08-05 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('generation_number', models.IntegerField(help_text='the official generation number', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sprite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back_default', models.URLField(max_length=300, verbose_name='default back url')),
                ('front_default', models.URLField(max_length=300, verbose_name='default back url')),
                ('svg_sprite', models.URLField(max_length=300, verbose_name='default back url')),
                ('big_sprite', models.URLField(max_length=300, verbose_name='default back url')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp', models.IntegerField(help_text='Hit point (health point)')),
                ('attack', models.IntegerField(help_text='Attack point')),
                ('defense', models.IntegerField(help_text='Ability to defend, mapped to a ratio')),
                ('special_attack', models.IntegerField(help_text='Special attack point')),
                ('special_attack_acc_rounds', models.IntegerField(help_text='Rounds to trigger special attack')),
                ('special_defense', models.IntegerField(help_text='Special defense point')),
                ('speed', models.IntegerField(help_text='Speed')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_number', models.IntegerField(help_text='type number', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='the type of the selected pokemon', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('idd', models.IntegerField(help_text='Pokemon id in the official game', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the pokemon', max_length=30)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('generation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Generation')),
                ('sprites', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Sprite')),
                ('stat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Stat')),
                ('types', models.ManyToManyField(to='pokemon.Type')),
            ],
            options={
                'ordering': ['idd'],
            },
        ),
    ]
