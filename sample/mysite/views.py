from django.shortcuts import render

def initial(request):
    name = request.GET.get("name")
    return render(request,"main.html",{"name":name})