from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.conf import settings
from django_resized import ResizedImageField

# Create your models here.
class Bike(models.Model):
    state_choice = (
        ('BA', 'Bagmati'),
        ('GA', 'Gandaki'),
        ('SP', 'Sudhurpaschim'),
        ('LU', 'Lumbini'),
        ('KA', 'Karnali'),
        ('MD', 'Madhesh'),
        ('P1', 'Province 1'),
    )

    year_choice = []
    for r in range(2022, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('ABS ', 'Anti-Lock Braking System'),
        ('Disc Brake','Disc Brake'),
        ('Off-Road ABS', 'Off-Road ABS'),
        ('Traction Control','Traction Control'),
        ('Rain Mode','Rain Mode'),
        ('Sport Mode', 'Sport Mode'),
        ('Economy Mode','Economy Mode'),
        ('FI-Engine','Fuel Injected Engine'),
        ('Carborator Engine','Carborator Engine'),

    )

    bike_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    rent_price= models.IntegerField(blank=True)
    description = RichTextField()
    bike_photo = ResizedImageField(upload_to='photos/%Y/%m/%d/')
    bike_photo_1 = ResizedImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    bike_photo_2 = ResizedImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    bike_photo_3 = ResizedImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    bike_photo_4 = ResizedImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    for_sale = models.BooleanField(default=False)
    for_rent = models.BooleanField(default=False)

    def __str__(self):
        return self.bike_title

    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"




class BikeOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, related_name='orders',
                                  on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    price = models.IntegerField()
    def __str__(self):
        return str(self.user)+ str(self.bike)

    def save(self, *args, **kwargs):
        self.price = self.bike.price
        super().save(*args, **kwargs)
        

    class Meta:
        verbose_name = "Bike Order"
        verbose_name_plural = "Bikes Orders"