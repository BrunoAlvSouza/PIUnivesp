# Generated by Django 4.2 on 2023-04-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0022_remove_cadastroaluno_classe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroaluno',
            name='classe_aluno',
            field=models.CharField(choices=[(1, 'turma1'), (2, 'turma2'), (3, 'turma3'), (4, 'turma4'), (5, 'turma5'), (6, 'turma6')], max_length=100, null=True),
        ),
    ]
