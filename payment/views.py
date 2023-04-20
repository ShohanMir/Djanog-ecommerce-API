from django.shortcuts import render

from .models import ShippingAddress

# Create your views here.

def checkout(request):
    
    if request.user.is_authenticated:
        try:
            # Authenticate user with shipping information
            shipping_address = ShippingAddress.objects.get(id=request.user.id)
            context = {'shipping': shipping_address}
            return render(request, 'payment/checkout.html', context)
        except:
            return render(request, 'payment/checkout.html')
    
    
    return render(request, 'payment/checkout.html')

def payment_success(request):
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')
    