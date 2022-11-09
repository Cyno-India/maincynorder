
from fileinput import filename
from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(max_length=10,required=True)
    itemcode = serializers.CharField(max_length=10,required=True)
    base_item_code = serializers.CharField(max_length=25,required=True)
    qty = serializers.CharField(max_length=10,required=True)
    cust = serializers.CharField(max_length=10,required=True)
    address = serializers.CharField(max_length=50,required=True)
    consignee = serializers.CharField(max_length=50,required=True)
    country = serializers.CharField(max_length=10,required=True)
    phone = serializers.CharField(max_length=20,required=True)
    pincode = serializers.CharField(max_length=10,required=True)

    class Meta:
        model = Order
        fields = ['customer_id','filename','particular','itemcode','base_item_code','qty','cust','address','ship_by','consignee','country','phone','pincode']


from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False)