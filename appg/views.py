from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def shop(request):
    return render(request,'shop.html')
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def news_detail(request,id):
    return render(request,'news_detail.html',{'id':id})
def news_create(request):
    return render(request,'news_create.html')
def news_update(request,id):
    return render(request,'news_update.html',{'id':id})
def news_delete(request,id):
    return render(request,'news_delete.html',{'id':id})
def single_product(request):
    return render(request,'single-product.html')
def checkout(request):
    return render(request,'checkout.html')
def cart(request):
    return render(request,'cart.html')
def error_404(request,exception):
    return render(request,'404.html',status=404)

