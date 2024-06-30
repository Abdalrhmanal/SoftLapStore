from django.shortcuts import render

# Create your views here.
def BASE(request):
    context = {
        'current_path': request.path,
    }
    return render(request, 'index.html',context)
    
    
def Category(request):
    return render(request, 'CategoryCompontents/index.html')

def DetailsProduct(request):
    return render(request, 'Products/index.html')

def Cart(request):
    return render(request, 'Cart/index.html')

def Contact(request):
    return render(request, 'Layout/contact.html')

def Login(request):
    return render(request, 'Auth/login.html')

def Register(request):
    return render(request, 'Auth/register.html')

# end def