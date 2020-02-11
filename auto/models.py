from django.db import models

class Seller(models.Model):
    name = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=20)
    address = models.CharField(default='', max_length=400)
    web_site = models.URLField(default='', max_length=100)
    logo = models.URLField(default='', max_length=100)
    
    def __str__(self):
      return self.name

class Car(models.Model):
  make = models.CharField(default='', max_length=200)
  model = models.CharField(default = '', max_length= 100)
  trim = models.CharField(default = '', max_length= 100)
  img_url = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
  milage = models.CharField(default = '', max_length= 100)
  color = models.CharField(default = '', max_length= 100)
  name = models.ForeignKey(Seller, on_delete = models.CASCADE, related_name = 'car')
  
  def __str__(self):
    return self.model
 
