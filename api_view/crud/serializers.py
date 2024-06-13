from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

        # FIELD LEVEL VALIDATION
        def validate_name(self,value):
            if len(value) > 8:
                raise serializers.ValidationError('Name should not be greater than 8 characters')
            return value

        # OBJECT LEVEL VALIDATION
        def validate(self,obj):
            roll = obj['roll']
            if roll > 110:
                raise serializers.ValidationError('Batch full')
            return obj