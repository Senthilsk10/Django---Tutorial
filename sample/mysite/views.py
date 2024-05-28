from django.shortcuts import render

def initial(request):
    items = ["carrot","beetroot","potato"]
    dict_items = {
        "name":"senthil",
        "age":20
    }
    return render(request,"main.html",{"items":items,"d_items":dict_items})