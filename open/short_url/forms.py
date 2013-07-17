from django import forms
from django.forms import ModelForm

from .models import Link

class URLForm(ModelForm):

	url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter a URL'}))
	class Meta:
		model = Link
		#exclude = ('hash_code',)
		fields = ('url',)
		
	def __init__(self, *args, **kwargs):
		super(URLForm, self).__init__(*args, **kwargs)
		self.fields['url'].label = ""
