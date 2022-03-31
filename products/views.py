from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def products_lists(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many = True)

    return Response(serializers.data)