# Generated by Django 5.2.1 on 2025-05-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('concluida', models.BooleanField(default=False, verbose_name='Concluída?')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'ordering': ['-data_criacao'],
            },
        ),
    ]
