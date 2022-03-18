from django.shortcuts import render

# Create your views here.
def frontend(request):
    return render(request, 'index.html')

def result(request):
    stringss = request.POST['inputTT']
    return render(request,"result.html",{"value":stringss[::]+ " "})