from django import forms

from .models import Review

REVIEW_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']

        widgets = {
            'rating': forms.RadioSelect(choices=REVIEW_CHOICES),
            'content': forms.Textarea(attrs={
                'class': 'form-control shadow px-2',
                'rows': 6
            })
        }