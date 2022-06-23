from rest_framework import serializers
from .models import Category, Item, ItemOrder, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = Category
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["name"]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = Item
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["name", "category", "image_url"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = Order
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["delivery_address", "order_date", "item"]

class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = ItemOrder
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["order", "item", "item_count"]