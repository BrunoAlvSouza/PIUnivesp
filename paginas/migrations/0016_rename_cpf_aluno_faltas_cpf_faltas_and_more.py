# Generated by Django 4.2 on 2023-04-27 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0015_remove_faltas_bimestre1_faltas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faltas',
            old_name='cpf_aluno',
            new_name='cpf_faltas',
        ),
        migrations.RenameField(
            model_name='notas',
            old_name='cpf_aluno',
            new_name='cpf_notas',
        ),
    ]
