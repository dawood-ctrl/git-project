from rest_framework import serializers
from projectsapps.models import students ,course
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields ='__all__'

            
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields ='__all__'

