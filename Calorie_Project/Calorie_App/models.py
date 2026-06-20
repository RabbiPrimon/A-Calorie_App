from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  def __str__(self):
    return f'{self.username}'


class BasicInfoModel(models.Model):
  GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
  name = models.CharField(max_length=100, null=True, blank=True)
  age = models.PositiveIntegerField(null=True, blank=True)
  gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
  weight = models.FloatField(null=True, blank=True)
  height = models.FloatField(null=True, blank=True)

  def __str__(self):
    return f'{self.name} - {self.user.username}'

class ConsumedCaloriesModel(models.Model):
  item_name = models.CharField(max_length=100)
  calorie_consumed = models.FloatField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
  consumed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calorie_consumed')

  def __str__(self):
    return f'{self.item_name} - {self.calorie_consumed} calories'