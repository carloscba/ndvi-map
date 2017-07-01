# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=65)
    polygon = models.TextField(null=True)
    description = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
