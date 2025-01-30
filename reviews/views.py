from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import DetailView

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
             
class DetailviewView(DetailView):
    model = Review  
    template_name = "reviews/single-review.html"
    context_object_name = "reviews"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        favorite_id = request.session.get("favorite_review")  
        context["is_favorite"] = (favorite_id == self.object.id)
        return context
    
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id") 
        
        if review_id:
            try:
                Review.objects.get(pk=review_id)  
                request.session["favorite_review"] = int(review_id)  
                request.session.modified = True  
                return HttpResponseRedirect(f"/reviews/{review_id}")
            except Review.DoesNotExist:
                return HttpResponseRedirect("/reviews/")  

        return HttpResponseRedirect("/reviews/")  
