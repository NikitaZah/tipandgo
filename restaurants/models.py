from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, validate_image_file_extension
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class Applicant(models.Model):
    applicant_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    country = models.CharField(max_length=150, help_text='You can name all countries where you would like to use T&G')
    business_desc = models.TextField(blank=True, help_text='short description of your business will be '
                                                           'greatly appreciated but is not necessary')
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.date}'


class Staff(models.Model):
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)
    percent = models.PositiveSmallIntegerField(default=20, validators=[MaxValueValidator])
    photo = models.ImageField(upload_to='media/staff_photos', validators=[validate_image_file_extension])
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'


class Institution(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey('InstitutionType', on_delete=models.RESTRICT)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    manager = models.OneToOneField('User', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.type} {self.name}'


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


class Tips(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(editable=False)
    client = models.ForeignKey('Client', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = 'tips'
        verbose_name_plural = 'tips'


class Position(models.Model):
    name = models.CharField(max_length=60)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

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


class PreRegisteredUser(models.Model):
    MANAGER = 'man'
    EMPLOYEE = 'staff'
    STATUS_CHOICES = [(MANAGER, 'manager'), (EMPLOYEE, 'staff')]
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.email}'


class User(AbstractUser):
    MANAGER = 'man'
    EMPLOYEE = 'staff'
    ADMIN = 'ad'
    STATUS_CHOICES = [(MANAGER, 'manager'), (EMPLOYEE, 'staff'), (ADMIN, 'admin')]

    username = None

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=16, blank=True)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    registration = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(blank=True)
    staff = models.ForeignKey(Staff, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.rating)
