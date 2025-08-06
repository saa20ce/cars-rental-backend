from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class CustomerReview(models.Model):
    STATUS_CHOICES = [
            ('pending','на рассмотрении'),
            ('published','Опубликованно'),
    ]

    full_name = models.CharField("ФИО",max_length=100)
    phone = models.CharField("Телефон",max_length=20)
    email=models.EmailField('Email')
    review_text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Оценка',validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    submited_at = models.DateTimeField('Дата прихода отзыва',auto_now=True)
    published_at = models.DateTimeField('Дата публикации отзыва',null=True,blank=True)
    status = models.CharField('Статус',max_length=20,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return f'{self.full_name} ({self.rating}★)'
    
    class Meta:
        verbose_name='Отзыв клиента'
        verbose_name_plural = 'Отзывы клиента'
    
class ThankYouLetter(models.Model):
    image = models.ImageField("Изображение", upload_to='thank_you_letters/')
    description = models.TextField('Описание')
    created_at = models.DateTimeField('Дата создания',auto_now_add=True)

    def __str__(self):
        return f'Письмо от {self.created_at.date()}'
    
    class Meta:
        verbose_name= 'Благодарственное письмо'
        verbose_name_plural = 'Благодарственные письма'
    