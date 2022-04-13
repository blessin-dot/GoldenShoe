from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'users/index.html')

def users(request):
    return HttpResponse('this is are the users')

# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'accounts/register.html', context)

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'accounts/login.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')