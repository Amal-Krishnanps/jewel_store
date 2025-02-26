from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect,render,get_list_or_404
from .forms import RegistrationForm,AddressForm
from store.models import Address,Cart,Category,Order,Product


def home(request):
    categories=Category.objects.filter(is_active=True,is_featured=True)[:3]
    products=Product.objects.filter(is_active=True,is_featured =True)
    context={
        'categories':categories,
        'products':products
    }
    return render(request,'store/index.html',context)
    


# user forms
class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'account/register.html',{'form':form})
    
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations! Registration Successful!")
            form.save()
        return render(request,'account/register.html',{'form':form})
    
def profile(request):
    addresses=Address.objects.filter(user=request.user)
    orders=Order.objects.filter(user=request.user)
    return render(request,'account/profile.html',{'addresses':addresses,'orders':orders})


class AddressView(View):
    def get(self,request):
        form=AddressForm()
        return render(request,'account/add_address.html',{'form':form})
    
    def post(self,request):
        form=AddressForm(request.POST)
        if form.is_valid():
            user=request.user
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            reg=Address(user=user,locality=locality,city=city,state=state)
            reg.save()
            messages.success(request,"New Address added Successfully!!")
        return redirect('store:profile')
    
    
