from django.shortcuts import render




#from django.http import HttpResponse# pra mandar uma mensagem sem o template escrevendo direto em HTML

def index(request):
    context_dict = {}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/about.html', context=context_dict)