from django.db import models


class MatchLog(models.Model):
    WL_CHOICE = ((False, 'LOSE'), (True, 'WIN'))
    TYPE_CHOICE = ((False, '特殊'), (True, '通常'))

    id = models.AutoField(primary_key=True)
    legion_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    win_lose = models.BooleanField(choices=WL_CHOICE, default=True)
    attack_target = models.CharField(max_length=100)
    debuff_target = models.CharField(max_length=100)
    front_type = models.BooleanField(choices=TYPE_CHOICE, default=True)
    absence = models.CharField(max_length=150)
    detail = models.TextField()
