from django.shortcuts import render, redirect
from apps.miniM.models import miniM
from apps.miniM.forms import miniM

# Create your views here.

def testP_view(request):
	if request.method == 'POST':
		form = miniM(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/miniM/nuevo')
	else:
		form = miniM()
	return render(request, 'miniM/testP_form.html', {'form':form})