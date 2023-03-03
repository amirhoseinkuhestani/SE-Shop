from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", blank=False, null=False)
    is_active = models.BooleanField(verbose_name="فعال", default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان", blank=False, null=False)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name="daste bandi")
    quantity = models.PositiveIntegerField(verbose_name="Tedad")
    price = models.PositiveIntegerField(verbose_name="قیمت", help_text="تومن")
    weight = models.PositiveIntegerField(verbose_name="وزن", help_text="کیلوگرم")
    note = models.TextField(max_length=200, verbose_name="توضیحات")
    discount = models.PositiveIntegerField(verbose_name="تخفیف", default=0, validators=[MinValueValidator(0),MaxValueValidator(100)],help_text="درصد")
    discount_price=models.PositiveIntegerField(verbose_name="مبلغ تخفیف", default=None, null=True, blank=True, editable=False)
    COLORS_CHOISE = (
        ('R' , 'قرمز'),
        ('B','آبی'),
        ('G','سبز')
    )
    colors=models.CharField(max_length=1,choices=COLORS_CHOISE)
    PRODUCT_CHOISE =(
        ('D','دیجیتال')
    )
    product_type=models.CharField(max_length=1,choices=PRODUCT_CHOISE)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        self.discount_price= self.price - (self.price*self.discount)/100
        super(Product, self).save(*args, **kwargs)
