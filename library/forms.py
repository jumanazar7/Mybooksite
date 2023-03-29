from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class Genres(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    slug = forms.SlugField(max_length=100, required=True)
    desc = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.ModelForm):
    check = forms.BooleanField(label="Married", initial=True)

    class Meta:
        model = Author
        fields = ('full_name', 'bio', 'image', 'check', 'birth_date', 'death_date')

        widgets = {
            "bio": forms.Textarea(attrs={
                "placeholder": "Muallifning hayoti"
            }),
            "birth_date": forms.DateInput(  
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "death_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            )
        }

    