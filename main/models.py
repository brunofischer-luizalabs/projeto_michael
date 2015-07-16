# coding: utf-8

from django.db import models


class Sale(models.Model):
	model_pic = models.ImageField(upload_to = 'pic_folder/')
	description = models.CharField(max_length = 300)
	qtd_product = models.IntegerField()


