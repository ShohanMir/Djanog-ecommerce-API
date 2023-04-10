from django.shortcuts import redirect, render
# from django.http import HttpResponseBadRequest

from .forms import CreateUserForm

# Create your views here.

def register(request):
    # if request.method != 'POST':
    #     return HttpResponseBadRequest('Bad Request')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
        else:
            # re-render the form with error messages
            context = {'form': form}
            return render(request, 'account/registration/register.html', context=context)   
        
    context = {'form': form}
    return render(request, 'account/registration/register.html', context=context)




def email_verification(request):
    pass

def email_verification_sent(request):
    pass

def email_verification_success(request):
    pass

def email_verification_failed(request):
    pass