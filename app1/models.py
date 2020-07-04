from django.db import models
from django.contrib import admin
# Create your models here.

class card(models.Model):
    object = models.Manager()
    cardName = models.CharField(max_length=50, default="몇 번째 카드뉴스인가요?")
    cardExplain = models.CharField(max_length=300, default="카드뉴스 설명을 적어주세요.")
    cardImage = models.ImageField(upload_to="image", blank=True)
    