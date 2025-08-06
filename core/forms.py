from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator
from .models import CustomerReview

class CustomerReviewAdminForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = '__all__'
    
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        label='Оценка',
        help_text='Оценка от 1 до 5'
    )