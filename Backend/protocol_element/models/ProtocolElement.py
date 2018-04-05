# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from protocol.models import Protocol

class ProtocolElement(models.Model):
    protocol        = models.ForeignKey(Protocol)
    title           = models.CharField(max_length=150, unique=True)
    description     = models.CharField(max_length=300)
    removed         = models.BooleanField(default=False)
    hash            = models.CharField(max_length=50, unique=True)
    nextElement     = models.ForeignKey("self", null=True)