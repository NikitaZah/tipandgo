from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_image_file_extension


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)


class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)
    percent = models.PositiveSmallIntegerField(default=20, validators=[MaxValueValidator(limit_value=50)])
    photo = models.ImageField(upload_to='staff_photos/', validators=[validate_image_file_extension])

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Institution(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('InstitutionType', on_delete=models.RESTRICT)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Address(models.Model):
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'


class Position(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class InstitutionType(models.Model):
    type_name = models.CharField

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'
