from django.shortcuts import render
def home(request):
    return render(request, 'mine.html')
# Create your views here.