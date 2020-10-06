from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, get_user_model
from store.models import Customer
# Create your views here.

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = get_user_model()
		fields = ['username','email','first_name','last_name','password1','password2',]

def register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			first = form.cleaned_data['first_name']
			last = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			user  = authenticate(username=username,password=password)
			login(request,user)
			usrmodel = get_user_model()
			usrobj = usrmodel.objects.get(username=username)
			Customer.objects.create(user=usrobj,name=first+' '+last,email=email)

			return redirect('store')
	else:
		form = CustomUserCreationForm()
	return render(request,'registration/registration.html',{'form':form})
