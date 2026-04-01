from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from expenses.models import Expense
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def analytics_view(request):
    user = request.user

    expenses = Expense.objects.filter(user=user)

    total = expenses.aggregate(total=Sum('amount'))['total'] or 0

    category_data = expenses.values('category').annotate(total=Sum('amount'))

    return Response({
        "total_spent": total,
        "category_breakdown": list(category_data)
    })