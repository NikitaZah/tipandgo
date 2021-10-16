from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_image_file_extension


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'


class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)
    percent = models.PositiveSmallIntegerField(default=20, validators=[MaxValueValidator(limit_value=50)])
    photo = models.ImageField(upload_to='media/staff_photos',
                              validators=[validate_image_file_extension])

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Institution(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey('InstitutionType', on_delete=models.RESTRICT)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=60)
    currency = models.ForeignKey('Currency', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class City(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country}, {self.name}'

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Address(models.Model):
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}, {self.street} {self.building}'

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'


class Tip(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(editable=False)
    client = models.ForeignKey('Client', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.amount


class Position(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class InstitutionType(models.Model):
    type_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'type'
        verbose_name_plural = 'types'


class Client(models.Model):
    pose = models.CharField(verbose_name='position', max_length=15, unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.pose


class Currency(models.Model):
    name = models.CharField(max_length=30, unique=True, default='RUB')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
