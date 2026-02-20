from rest_framework import serializers
from .models import AvailabilitySlot

class AvailabilitySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlot
        fields = ['id', 'day_of_week', 'start_time', 'end_time']
