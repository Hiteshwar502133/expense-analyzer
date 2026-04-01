from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Expense
from .serializers import ExpenseSerializer
from .services import detect_category

class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        description = self.request.data.get("description", "")
        category = detect_category(description)

        serializer.save(
            user=self.request.user,
            category=category
        )