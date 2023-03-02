# Generated by Django 4.1.7 on 2023-03-02 19:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('quantity', models.PositiveIntegerField(verbose_name='Tedad')),
                ('price', models.PositiveIntegerField(help_text='تومن', verbose_name='قیمت')),
                ('weight', models.PositiveIntegerField(help_text='کیلوگرم', verbose_name='وزن')),
                ('note', models.TextField(max_length=200, verbose_name='توضیحات')),
                ('discount', models.PositiveIntegerField(default=0, help_text='درصد', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='تخفیف')),
                ('discount_price', models.PositiveIntegerField(blank=True, default=None, editable=False, null=True, verbose_name='مبلغ تخفیف')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category', verbose_name='daste bandi')),
            ],
        ),
    ]