# Generated by Django 5.1.2 on 2025-02-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_imagem_alter_post_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
    ]
