from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_objeect_name = "profiles"
    

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES)  # use 'form' for clarity
#         if form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])  # correctly save the image field
#             profile.save()
#             return HttpResponseRedirect("/profiles")  # Make sure this redirects to the correct place
        
#         # If the form is not valid, re-render the page with the form errors
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
