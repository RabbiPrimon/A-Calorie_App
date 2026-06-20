from django.contrib import admin
from Calorie_App.models import User, BasicInfoModel, ConsumedCaloriesModel 

admin.site.register(User)
admin.site.register(BasicInfoModel)
admin.site.register(ConsumedCaloriesModel)
