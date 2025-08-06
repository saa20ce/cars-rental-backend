from django.contrib import admin
from .models import CustomerReview,ThankYouLetter
from .forms import CustomerReviewAdminForm
# Register your models here.

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    form = CustomerReviewAdminForm
    list_display = ('full_name','rating','status','submited_at','published_at')
    list_filter = ('status','rating')
    search_fields = ('full_name','email','phone')
    actions = ['make_published']

    def make_published(self,request,queryset):
        updated = queryset.update(status = 'published')
        self.message_user(request,f'{updated} отзыв(ов) опубликованно.')
    make_published.short_description = 'Опубликовать выбранные отзывы'

    

@admin.register(ThankYouLetter)
class ThankYouLetterAdmin(admin.ModelAdmin):
    list_display=('description','created_at')

    
