from django.shortcuts import render


# Create your views here.
def index(request):
    """the page that learn notes"""
    print("index index")
    return render(request, 'learning_logs/index.html')
