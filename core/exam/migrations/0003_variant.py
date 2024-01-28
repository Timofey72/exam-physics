# Generated by Django 5.0.1 on 2024-01-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_taskcategory_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_number', models.IntegerField(verbose_name='Номер варианта')),
                ('tasks', models.ManyToManyField(related_name='variants', to='exam.task', verbose_name='Задания')),
            ],
        ),
    ]