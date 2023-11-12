from django.db import models
from datetime import date

class User(models.Model):
    GENDER_CHOICES = (('Парень', 'Парень'), ('Девушка', 'Девушка'),)
    image = models.ImageField(upload_to='myapp/static/img/profile')
    name_surname = models.CharField(max_length=40)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    telegram = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_surname

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

