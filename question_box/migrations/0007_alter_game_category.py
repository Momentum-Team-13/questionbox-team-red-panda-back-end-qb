# Generated by Django 4.0.6 on 2022-07-31 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0006_game_question_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('A', 'Action Game'), ('F', 'Fighting Game')], max_length=3),
        ),
    ]
