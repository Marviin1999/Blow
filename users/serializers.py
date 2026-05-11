from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    # Campos requeridos por el usuario
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    birthday = serializers.DateField(write_only=True) # Solo para recibirlo en el registro

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'birthday')

    def create(self, validated_data):
        # Extraemos la fecha de nacimiento (puedes guardarla en un modelo Profile luego)
        birthday = validated_data.pop('birthday') 
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user