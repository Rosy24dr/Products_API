from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def products_lists(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)