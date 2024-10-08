from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        moodels = React
        fields = ['employee', 'department']
        
        