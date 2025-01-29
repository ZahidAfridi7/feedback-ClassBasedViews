from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request,"reviews/review.html",{
            "form": form
        })
    def post(self,request):
        form = ReviewForm(request.POST) 
           
        if form.is_valid():
         form.save() 
         return HttpResponseRedirect('/thank-you')
    
    
        return render(request,"reviews/review.html",{
            "form": form
        })

class ThankyouView(View):
    def get(self,request):
     return render(request,"reviews/thankyou.html")   
 

class ReviewlistView(TemplateView):
    template_name = "reviews/review-list.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.all()
        context["reviews"] = review
        return context          
class DetailviewView(TemplateView):
    template_name = "reviews/single-review.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk = review_id)
        context["reviews"] = selected_review
        return context
    
        