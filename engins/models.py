from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.
class Engin(models.Model):
    eng_name = models.CharField(max_length=32)
    eng_code = models.CharField(max_length=32)
    
    def get_absolute_url_index(self):
        return reverse("engins:engin_list_view")
        
        
    def get_absolute_url(self):
        return reverse("engins:engin_single_view", kwargs={'id': self.id})
    
    def get_absolue_url_update(self):
        return reverse("engins:engin_update_view", kwargs={'id': self.id})
    
    def get_absolute_url_del(self):
        return reverse("engins:engin_del_view", kwargs={'id': self.id})
    
    def __str__(self):
        return self.eng_name

# Try to add a second filed for code from Engin code model
class Driver(models.Model):
    driv_eng = models.ForeignKey(Engin, on_delete=models.CASCADE)
    driv_full_name = models.CharField(max_length=32)

    def __str__(self):
        return self.driv_full_name

# devs bransh edit.
# Master bransh edit.
