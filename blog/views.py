from django.shortcuts import render

def about_me(request):
    # Puedes pasar información adicional a la plantilla si es necesario
    return render(request, 'blog/about_me.html')

