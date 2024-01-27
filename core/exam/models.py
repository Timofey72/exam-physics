from django.db import models


class TaskCategory(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Название: {self.title}'


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(null=False, verbose_name='Тип задания')
    description = models.TextField(verbose_name='Описание задания')
    image = models.ImageField(upload_to='tasks/', blank=True, null=True, verbose_name='Фотография')
    correct_answer = models.CharField(max_length=128, verbose_name='Правильный ответ')
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE, default=0, verbose_name='Категория задачи')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'Тип: {self.type}. ID: {self.id}'
