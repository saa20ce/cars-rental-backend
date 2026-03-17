from rest_framework import serializers
from .models import CustomerReview,ThankYouLetter

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = '__all__'
        read_only_fields = ['submitted_at', 'published_at', 'status']

class ThankYouLetterSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = ThankYouLetter
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url if obj.image else None