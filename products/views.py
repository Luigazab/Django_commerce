from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')
def browse(request):
  return render(request, 'browse.html')
def newArrival(request):
  return render(request, 'new arrival.html')
def bestCollection(request):
  return render(request, 'best collection.html')
def about(request):
  return render(request, 'about.html')