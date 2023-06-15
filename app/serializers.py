from rest_framework import serializers
from app.models import *

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'