# Generated by Django 4.0.6 on 2022-07-30 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_box', '0004_alter_question_description_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answered_question',
            new_name='question',
        ),
    ]
