from django.db import models
from django.core.urlresolvers import reverse




# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    joining_date = models.DateField('joining date')

    def get_absolute_url(self):
        return reverse('students_edit', kwargs={'pk': self.pk})