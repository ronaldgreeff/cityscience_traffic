from traffic.models import Record
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'