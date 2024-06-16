from rest_framework import serializers
from .models import Student

# VALIDATORS
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name should begin with R')

# DEFAULT SERIALIZER
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[starts_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance

#     # FIELD LEVEL VALIDATION
#     def validate_roll(self,value):
#         if value>200:
#             raise serializers.ValidationError('Batch full')
#         return value
        
#     # OBJECT LEVEL VALIDATION
#     def validate(self, data):
#         if data['roll']>150:
#             raise serializers.ValidationError('Batch full')
#         elif data['city'] in ['Raipur','Nagpur','Udupi']:
#             raise serializers.ValidationError('Not accepted')
#         return data


# MODEL SERIALIZER
class StudentSerializer(serializers.ModelSerializer):
    # explicitly adding argument to a field
    # name = serializers.CharField(read_only=True)


    name = serializers.CharField(validators = [starts_with_r])

    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll']
    
    def validate_roll(self,value):
        if value>200:
            raise serializers.ValidationError('Batch full')
        return value
    
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm == 'veeru' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City is not Ranchi')
        return data