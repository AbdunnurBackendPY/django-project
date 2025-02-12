from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    user = models.ForeignKey(User,
        verbose_name='Author',
        on_delete=models.CASCADE
    )
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Publication date')


    def get_absolute_url(self):
        return f'/news/{self.id}'

    def __str__(self):
        return self.title
