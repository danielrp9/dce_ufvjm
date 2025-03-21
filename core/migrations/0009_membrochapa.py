# Generated by Django 5.1.2 on 2025-02-19 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_chapamembro'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembroChapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='chapa/')),
                ('curso', models.CharField(max_length=100)),
                ('campus', models.CharField(choices=[('Diamantina', 'Diamantina'), ('Janaúba', 'Janaúba'), ('Unaí', 'Unaí'), ('Mucuri', 'Mucuri')], max_length=20)),
            ],
        ),
    ]
