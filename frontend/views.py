import os
from django.shortcuts import render

# Create your views here.
def home(request):
    port = os.getenv('PORT', 9000)
    print(port)

    return render(request,'frontend/home.html')