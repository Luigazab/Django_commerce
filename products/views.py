from django.shortcuts import render, get_object_or_404
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
  products = Product.objects.filter(is_available=True).order_by('-created_at')[:8].prefetch_related('images')

  for product in products:
    images = product.images.all()
    product.main_image = next((img for img in images if img.is_main), images.first() if images else None)

  return render(request, 'new arrival.html', {
      'products': products
    })

def product_detail(request, slug):
  product = get_object_or_404(Product, slug=slug)
  images = product.images.all()
  variants = product.variants.all()
  main_image = next((img for img in images if img.is_main), images.first() if images else None)

  return render(request, 'product_detail.html',{
    'product': product,
    'main_image': main_image,
    'images': images,
    'variants': variants,
  })
def about(request):
  return render(request, 'about.html')