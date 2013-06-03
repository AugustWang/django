from django.db import models

# Create your models here.
from django.contrib import admin


class one_article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()

    def __unicode__(self):
        return self.title,self.content



admin.site.register(one_article)
