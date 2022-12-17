from django import forms
from .models import BlogModel



class BlogForm(forms.ModelForm):
    image=forms.ImageField(widget=forms.FileInput())
    title= forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control my-1',
				   'placeholder':'Title'}))
    # desc=forms.CharField(widget=forms.(attrs={'class':'form-control my-1',
	# 			   'placeholder':'Add your Blog'}))


    class Meta:
        model = BlogModel
        fields = ("image","title",'desc')

        labels = {
            "desc": ''
        }
        # fields = ("image","title",'desc')
        # fields = '__all__'
        



   