from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, default='Jovan')
    last_name = models.CharField(max_length=50, default='Jovanovic')
    email = models.CharField(max_length=50, default='jova@gmail.com')
    phone = models.CharField(max_length=50, default='060-000-000')
    address = models.CharField(max_length=50, default='Sunshine Boulevar no 43')
    city = models.CharField(max_length=50, default='New York')
    state = models.CharField(max_length=50, default='Texas')
    zipcode = models.CharField(max_length=50, default='324')

    def __str__(self):
        return(f'{self.first_name} {self.last_name}')