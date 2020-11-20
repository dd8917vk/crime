from django import forms
from .models import Departments


# RATING_CHOICES= [tuple([x,x]) for x in range(1, 6)]

# class RatingForm(forms.ModelForm):
#     rating = forms.IntegerField(label="Your Rating", widget=forms.Select(choices=RATING_CHOICES))
#     class Meta:
#         model=Rating
#         fields = ('rating',)

class AddDepartment(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ('__all__')
        # widgets = {
        #     'brand_title': forms.TextInput(
        #         attrs={'class': 'brand', 'placeholder':'Enter Brand'}
        #     )
        #}    