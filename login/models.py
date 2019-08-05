from django.db import models
from django.contrib import admin
# Create your models here.
class SignUp(models.Model):
    user_id = models.CharField(max_length=10)
    user_psd = models.CharField(max_length=10)
    user_msg = models.CharField(max_length=20)

    def __str__(self):
            return self.user_id
@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = [field.name for field in 
    SignUp._meta.fields]

    #list_display = ['id','user_id','user_psd']