from rest_framework import viewsets
from .models import PhoneBook
from .serializers import PhoneBookSerializer

class PhoneBookViewSet(viewsets.ModelViewSet):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer