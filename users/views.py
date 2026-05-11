from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response(
                {"error": "Faltan datos obligatorios"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Este nombre de usuario ya está tomado"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # create_user guarda la contraseña encriptada y activa al usuario automáticamente
        User.objects.create_user(
            username=username, 
            password=password, 
            email=email
        )
        
        return Response(
            {"message": "¡Cuenta creada con éxito!"}, 
            status=status.HTTP_201_CREATED
        )