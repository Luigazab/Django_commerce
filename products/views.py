from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator
# Create your views here.
def home(request):
  return render(request, 'home.html')
def browse(request):
  products = Product.objects.filter(is_available=True).prefetch_related('variants', 'images')
  categories = Category.objects.all()

  for product in products:
    images = product.images.all()
    product.main_image = next((img for img in images if img.is_main), images.first() if images else None)

  paginator = Paginator(products, 8)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'browse.html', {
    'products': page_obj.object_list,
    'page_obj': page_obj, 
    'categories': categories
    })
def newArrival(request):
  return render(request, 'new arrival.html')
def about(request):
  return render(request, 'about.html')