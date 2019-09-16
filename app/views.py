
import requests

import rest_framework.viewsets
import rest_framework.decorators

from . import serializers, models


PRODUCTS_API_URL = 'http://challenge-api.luizalabs.com/api/product/{}'

class ClientViewSet(rest_framework.viewsets.ModelViewSet):

    serializer_class = serializers.ClientSerializer
    permission_classes = [

    ] 

    def get_queryset(self):
        return models.Client.objects.all()

class FavoriteProductsViewSet(rest_framework.viewsets.ModelViewSet):

    serializer_class = serializers.FavoriteProductsSerializer
    permission_classes = [

    ]

    def get_queryset(self):
        return models.FavoriteProducts.objects.all()

    def create(self, request):
        product_id = request.data.get('product')
        data = {
            'product': PRODUCTS_API_URL.format(product_id),
            'client': request.data.get('client')
        }
        if requests.get(data.get('product')).status_code == 404:
            return rest_framework.response.Response({
                'error': 'product not found'
            }, 404)
        serializer = serializers.FavoriteProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return rest_framework.response.Response({
                'message': 'product {} saved'.format(product_id)
            })
        return rest_framework.response.Response(serializer.errors, 400)

    def get(self, requests):
        products = models.FavoriteProducts.objects.all()
        serializer = serializers.FavoriteProductsSerializer(products, many=True)
        return rest_framework.response.Response({
            'products': serializer.data
        })
    