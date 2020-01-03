from django.shortcuts import render

def home(request):
    template_dir= "index.html"
    datas = {"name":"project"}
    return render(request,template_dir,datas)