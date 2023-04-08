from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from django.core.validators import RegexValidator
#from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", blank=False, null=False)
    is_active = models.BooleanField(verbose_name="فعال", default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    COLOR_CHOICES = (
        ('R', 'قرمز'),
        ('B', 'آبی'),
        ('G', 'سبز')
    )
    '''
    PRODUCT_CHOICES = (
        ('D', 'دیجیتال'),
        ('K', 'کتاب'),
        ('B', 'بچه‌گانه')
    )
    '''
    title = models.CharField(max_length=200, verbose_name='عنوان')
    thumbnail = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name='دسته بندی')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت', help_text='تومان')
    weight = models.PositiveIntegerField(verbose_name='وزن', help_text='کیلوگرم')
    note = models.TextField(max_length=200, verbose_name='توضیحات')
    discount = models.PositiveIntegerField(verbose_name='تخفیف', default=0, validators=[MinValueValidator(0),MaxValueValidator(100)], help_text='درصد')
    discount_price = models.DecimalField(verbose_name='مبلغ تخفیف', max_digits=8, decimal_places=2, default=None, null=True, blank=True, editable=False)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, verbose_name='رنگ')
    #product_type = models.CharField(max_length=1, choices=PRODUCT_CHOICES, verbose_name='نوع محصول')
    is_active = models.BooleanField(verbose_name='فعال', default=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.discount_price = self.price - (self.price * self.discount) / 100
        super(Product, self).save(*args, **kwargs)

