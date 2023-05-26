# Generated by Django 4.2 on 2023-04-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0021_cadastroaluno_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastroaluno',
            name='classe',
        ),
        migrations.AddField(
            model_name='cadastroaluno',
            name='classe_aluno',
            field=models.CharField(choices=[(1, 'Turma1'), (2, 'Turma2'), (3, 'Turma3'), (4, 'Turma4'), (5, 'Turma5'), (6, 'Turma6')], max_length=100, null=True),
        ),
    ]
