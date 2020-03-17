from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    nengetu = models.CharField(max_length=6, default=202001)
    dento = models.IntegerField(default=100)
    kuchou = models.IntegerField(default=100)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
#        return self.title
#        return self.nengetu
         return '年月:' + str(self.nengetu) 
