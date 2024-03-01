from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def update(self, instance, validated_data):
        """
        Update and return an existing `Patient` instance, given the validated data.
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance
