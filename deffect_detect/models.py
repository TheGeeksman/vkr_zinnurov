from django.db import models


class BoardExample(models.Model):
    board_model = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='example_boards/')
