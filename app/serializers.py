
from rest_framework import serializers

from . import models


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    favorite_products = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Client
        fields = [
            'id',
            'email',
            'name',
            'favorite_products',
        ]

class FavoriteProductsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.FavoriteProducts
        fields = [
            'id',
            'client',
            'product'
        ]