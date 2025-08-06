from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import CustomerReview, ThankYouLetter
from .serializers import CustomerReviewSerializer, ThankYouLetterSerializer

class CustomerReviewViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerReviewSerializer

    def get_permissions(self):
        if self.action in ['create', 'list']:
            return [AllowAny()]
        if self.action =='retrieve':
            return [IsAdminUser()]
        return [IsAdminUser()]

    def get_queryset(self):
        queryset = CustomerReview.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def perform_create(self, serializer):
        serializer.save(status='pending', published_at=None)

class ThankYouLetterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ThankYouLetter.objects.all().order_by('-created_at')
    serializer_class = ThankYouLetterSerializer
    permission_classes = [AllowAny]
