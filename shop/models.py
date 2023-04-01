from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", blank=False, null=False)
    is_active = models.BooleanField(verbose_name="فعال", default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    PRODUCT_CHOICE =(
        ('D','دیجیتال'),
        ('K','کتاب'),
        ('B','بچه گانه')
    )
    COLORS_CHOICE = (
        ('R' , 'قرمز'),
        ('B','آبی'),
        ('G','سبز')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان", blank=False, null=False)
    thumbnail = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name="daste bandi")
    quantity = models.PositiveIntegerField(verbose_name="Tedad")
    price = models.PositiveIntegerField(verbose_name="قیمت", help_text="تومن")
    weight = models.PositiveIntegerField(verbose_name="وزن", help_text="کیلوگرم")
    note = models.TextField(max_length=200, verbose_name="توضیحات")
    discount = models.PositiveIntegerField(verbose_name="تخفیف", default=0, validators=[MinValueValidator(0),MaxValueValidator(100)],help_text="درصد")
    discount_price=models.PositiveIntegerField(verbose_name="مبلغ تخفیف", default=None, null=True, blank=True, editable=False)
    colors=models.CharField(max_length=1,choices=COLORS_CHOICE)
    product_type=models.CharField(max_length=1,choices=PRODUCT_CHOICE)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.discount_price= self.price - (self.price*self.discount)/100
        super(Product, self).save(*args, **kwargs)


class UserManager(models.Manager):
    def admin_users(self):
        return self.filter(access_level=True)

class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    iban_regex = RegexValidator(
        regex=r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$',
        message="IBAN must be a valid International Bank Account Number."
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=17, validators=[phone_regex], blank=True, null=True)
    iban = models.CharField(max_length=34, validators=[iban_regex], blank=True, null=True)
    national_id = models.CharField(max_length=10, unique=True)
    history_of_orders = models.TextField(blank=True, null=True)
    access_level = models.BooleanField(default=False, choices=[(False, 'User'), (True, 'Admin')])

    objects = UserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
    
class Admin(User):
    admin_username = models.CharField(max_length=100, unique=True, verbose_name="نام کاربری مدیر")

    def __str__(self):
        return f"{self.name} ({self.admin_username})"

   