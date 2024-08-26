from django.shortcuts import render


def home_page_view(request):
    return render(request, 'homepage.html')
    
def home_page_view2(request):
    return render(request, 'homepage3.html')
