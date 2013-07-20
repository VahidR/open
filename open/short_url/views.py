from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import URLForm
from .models import Link

class URLCreateView(CreateView):
	model = Link
	form_class = URLForm
	template_name = 'index.html'
	success_url = reverse_lazy('result')

class URLListView(ListView):
	context_object_name = 'links'
	queryset = Link.objects.order_by('-id')[0] if Link.objects.all() else None
	template_name = 'short_url/result.html'

