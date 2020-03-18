from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    nengetu = models.CharField('年月', max_length=6, default=202001)
    dento = models.IntegerField('電灯使用量', default=0)
    kuchou = models.IntegerField('空調使用量', default=0)

    created_date = models.DateTimeField('作成日', default=timezone.now)
    published_date = models.DateTimeField('公開日', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
#        return self.title
        return self.nengetu
#         return str(self.nengetu, self.dento, self.kuchou, self.created_date)
    class Meta:
        verbose_name = 'データ'
        verbose_name_plural = 'データ'
