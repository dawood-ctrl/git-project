from rest_framework import serializers
from models import students ,course
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=students,course
        feilds ='__all__'

