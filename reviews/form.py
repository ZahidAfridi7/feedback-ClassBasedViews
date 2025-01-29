from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name",max_length=100, error_messages={
#         "required": "your name can not be empty",
#         "max_length": "name character can not exceed 100 letter"
#     })
#     review_text = forms.CharField(label="your feedback",widget=forms.Textarea,max_length=200)
#     ratting = forms.IntegerField(label="your ratting",min_value=1,max_value=10)
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name" : "Your Name",
            "review_text": "Your Feedback",
            "ratting": "Your Ratings"
        }    
        errors_messages = {
            "user_name": {
                "required": "your name can not be empty",
                "max_length": "name character can not exceed 100 letter"
            }
            
        }