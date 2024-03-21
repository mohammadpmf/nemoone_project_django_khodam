from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.validators import MinLengthValidator

from django_jalali.db import models as jmodels

class Estate(models.Model):
    HOUSE_CHOICES = (
        ('a', 'آپارتمانی'),
        ('v', 'ویلایی'),
    )
    type = models.CharField(max_length=1, choices=HOUSE_CHOICES, default='a', verbose_name="نوع منزل")
    state = models.CharField(max_length=100, default='گیلان', verbose_name="استان")
    city = models.CharField(max_length=100, default='رشت', verbose_name="شهر")
    region = models.CharField(max_length=100, blank=True, verbose_name="منطقه")
    street = models.CharField(max_length=100, verbose_name="خیابان")
    main_alley = models.CharField(max_length=100, blank=True, verbose_name="کوچه اصلی")
    side_alley = models.CharField(max_length=100, blank=True, verbose_name="کوچه فرعی")
    building_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], verbose_name="شماره پلاک")
    building_name = models.CharField(max_length=100, blank=True, verbose_name="نام ساختمان")
    postal_code = models.CharField(max_length=10, validators=[MinLengthValidator(10)], blank=True, verbose_name="کد پستی")
    floor = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="طبقه")
    unit = models.PositiveSmallIntegerField(verbose_name="واحد")
    elevator = models.BooleanField(default=True, verbose_name="آسانسور")
    parking = models.BooleanField(default=True, verbose_name="پارکینگ")
    warehouse = models.BooleanField(default=True, verbose_name="انبار")
    swimming_pool = models.BooleanField(default=False, verbose_name="استخر")
    year_created = jmodels.jDateField(verbose_name="سال ساخت")
    datetime_created = jmodels.jDateTimeField(auto_now_add=True)
    area = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(45), MaxValueValidator(900)], verbose_name="مساحت")
    price = models.PositiveBigIntegerField(verbose_name="قیمت")
    description = models.TextField(blank=True, verbose_name="توضیحات بیشتر")
    slug = models.SlugField(default="", unique=True, allow_unicode=True, verbose_name='url')

    class Meta:
        unique_together = ('side_alley', 'building_number', 'building_name', 'floor', 'unit')

    def __str__(self):
        if self.building_name not in ["", None, ()]:
            return f"ساختمان {self.building_name}، واحد {self.unit}"
        return f"ساختمان پلاک {self.building_number}، واقع در خیابان {self.street}، واحد {self.unit}"
            