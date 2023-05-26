# Generated by Django 4.2 on 2023-04-29 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0027_rename_nomecompleto_aluno_faltas_nomecompleto_falta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faltas',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='paginas.cadastroaluno'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faltas',
            name='nomecompleto_falta',
            field=models.CharField(max_length=100),
        ),
    ]