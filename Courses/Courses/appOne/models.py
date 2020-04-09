from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=128,default='')
    length = models.CharField(max_length=128,default='')
    applied = models.CharField(max_length=128,default='')
    website = models.CharField(max_length=128,default='')
    rating = models.CharField(max_length=128,default='')
    certified = models.CharField(max_length=128,default='')
    price = models.CharField(max_length=128,default=0)

    def __str__(self):
        return self.course_name
