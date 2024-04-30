from django.shortcuts import render
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase
cred = credentials.Certificate('firebase_credentials/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Django view function
def my_view(request):
    # Your Firebase code here
    return render(request, 'my_template.html', context)

def create(request):

# DRF viewset
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
