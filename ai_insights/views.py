from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from expenses.models import Expense
from .services import generate_insights

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def insights(request):
    expenses = Expense.objects.filter(user=request.user)
    insights_data = generate_insights(expenses)

    return Response({
        "insights": insights_data
    })