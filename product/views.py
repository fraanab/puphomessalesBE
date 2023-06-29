from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def newProduct(request):
    userId = request.data.get('userId')
    user = User.objects.get(id=userId)
    # print('user', userId)
    try:
        if user.is_superuser:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteProduct(request, id):
    userId = request.query_params.get('userId')
    try:
        user = User.objects.get(id=userId)
        if user.is_superuser:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
