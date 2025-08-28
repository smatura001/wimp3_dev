from rest_framework import serializers
from . import models as mx

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = mx.District
        fields = '__all__'

class CommodityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = mx.CommodityType
        fields = '__all__'
    
class CommodityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = mx.CommodityCategory
        fields = '__all__'

class PestAlertLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mx.PestAlertLevel
        fields = '__all__'

class PestRiskEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = mx.PestRiskEntry
        fields = '__all__'
