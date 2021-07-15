from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import Profile
# Create your views here.

def profile_update_view(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("/login?next=/profile/update") 
	user_ = request.user
	user_data = {
		'first_name': user_.first_name,
		'last_name': user_.last_name,
		'email': user_.email
	}
	my_profile = user_.profile
	form = ProfileForm(request.POST or None, instance=my_profile,initial=user_data)
	if form.is_valid():
		profile_obj = form.save(commit=False)
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		email = form.cleaned_data.get('email')
		user_.first_name = first_name
		user_.last_name = last_name
		user_.email = email
		user_.save()
		profile_obj.save()
	context = {
		'form':form,
		'btn_label':"save",
		'title':"Update profile",
		'username':user_.username
	}
	return render(request, "profiles/form.html", context)





def profile_detail_view(request, username, *args, **kwargs):
	# get the profile for the passed username
	qs = Profile.objects.filter(user__username=username)
	if not qs.exists():
		raise Http404
	profile_ojb = qs.first()
	context = {
		"username":username,
		"profile":profile_ojb
	}
	return render(request, "profiles/detail.html", context)
