from django.shortcuts import render

# Create your views here.
def frontend(request):
    query=""
    if 'clear' in request.POST:
        return render(request, 'index.html', {'querystr':query,'value':query})
    if request.POST.get('query'):
        query = request.POST.get('query')
    return render(request, 'index.html', {'querystr':query,'value':query})