# Generated by Django 4.1.7 on 2023-04-08 07:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('iban', models.CharField(blank=True, default=None, max_length=34, null=True, validators=[django.core.validators.RegexValidator(message='IBAN must be a valid International Bank Account Number.', regex='^[A-Z]{2}\\d{2}[A-Z0-9]{1,30}$')])),
                ('national_id', models.CharField(blank=True, default=None, max_length=10, null=True, unique=True)),
                ('history_of_orders', models.TextField(blank=True, default=None, null=True)),
                ('is_admin', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('admin_username', models.CharField(max_length=100, unique=True, verbose_name='نام کاربری مدیر')),
            ],
            options={
                'abstract': False,
            },
            bases=('shop.user',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('quantity', models.PositiveIntegerField(verbose_name='Tedad')),
                ('price', models.PositiveIntegerField(help_text='تومن', verbose_name='قیمت')),
                ('weight', models.PositiveIntegerField(help_text='کیلوگرم', verbose_name='وزن')),
                ('note', models.TextField(max_length=200, verbose_name='توضیحات')),
                ('discount', models.PositiveIntegerField(default=0, help_text='درصد', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='تخفیف')),
                ('discount_price', models.PositiveIntegerField(blank=True, default=None, editable=False, null=True, verbose_name='مبلغ تخفیف')),
                ('colors', models.CharField(choices=[('R', 'قرمز'), ('B', 'آبی'), ('G', 'سبز')], max_length=1)),
                ('product_type', models.CharField(choices=[('D', 'دیجیتال'), ('K', 'کتاب'), ('B', 'بچه گانه')], max_length=1)),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category', verbose_name='daste bandi')),
            ],
        ),
    ]
